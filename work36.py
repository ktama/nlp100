# -*- Coding: utf-8 -*-
from collections import Counter
import utility.print_method_result as util
import utility.parser as parser

# 36. 単語の出現頻度
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．


@util.print_result
def extract_verb(target_file=''):
    lines = parser.read_morpheme(target_file)
    word_counter = Counter()
    try:
        for line in lines:
            word_counter.update([morpheme['surface'] for morpheme in line])
    except:
        pass
    return word_counter.most_common()


if __name__ == '__main__':
    extract_verb('./data/neko.txt.mecab')
