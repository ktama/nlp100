# -*- Coding: utf-8 -*-

import MeCab


def parse_morpheme(target_file='', parsed_file=''):
    target = []
    with open(target_file, 'r', encoding='utf-8') as f:
        target = f.read()
    m = MeCab.Tagger()
    parsed = m.parse(target)
    with open(parsed_file, 'w', encoding='utf-8') as f:
        f.writelines(parsed)


if __name__ == '__main__':
    parse_morpheme('./data/neko.txt', './data/neko.txt.mecab')
