# -*- Coding: utf-8 -*-
import utility.print_method_result as util
import utility.parser as parser

# 35. 名詞の連接
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．


@util.print_result
def extract_compound_noum(target_file=''):
    lines = parser.read_morpheme(target_file)
    compound_noums = []
    try:
        for line in lines:
            noums = []
            for morpheme in line:
                if morpheme['pos'] == '名詞':
                    noums.append(morpheme['surface'])
                else:
                    if len(noums) > 1:
                        compound_noums.append(''.join(noums))
                    noums = []
    except Exception:
        pass
    return set(compound_noums)


if __name__ == '__main__':
    extract_compound_noum('./data/neko.txt.mecab')
