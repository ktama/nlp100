# -*- Coding: utf-8 -*-

import MeCab
from collections import Counter


def parse_morpheme(target_file='', parsed_file=''):
    target = []
    with open(target_file, 'r', encoding='utf-8') as f:
        target = f.read()
    m = MeCab.Tagger()
    parsed = m.parse(target)
    with open(parsed_file, 'w', encoding='utf-8') as f:
        f.writelines(parsed)


def read_morpheme(target_file=''):
    parsed_morphemes = []
    with open(target_file, 'r', encoding='utf-8') as f:
        parsed_morphemes = f.readlines()
    morphems = []
    for parsed_morpheme in parsed_morphemes:
        if 'EOS' in parsed_morpheme:
            raise StopIteration
        parsed_tabs = parsed_morpheme.split('\t')
        parsed_commas = parsed_tabs[1].split(',')
        morphem = {
            'surface': parsed_tabs[0],
            'base': parsed_commas[6],
            'pos': parsed_commas[0],
            'pos1': parsed_commas[1]
        }
        morphems.append(morphem)

        if parsed_commas[1] == '句点':
            yield morphems
            morphems = []


def extract_word_count(target_file=''):
    lines = read_morpheme(target_file)
    word_counter = Counter()
    try:
        for line in lines:
            word_counter.update([morpheme['surface'] for morpheme in line])
    except:
        pass
    return word_counter.most_common()


if __name__ == '__main__':
    parse_morpheme('./data/neko.txt', './data/neko.txt.mecab')
