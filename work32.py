# -*- Coding: utf-8 -*-
import utility.print_method_result as util
import utility.parser as parser

# 31. 動詞
# 動詞の表層形をすべて抽出せよ．


@util.print_result
def extract_original_verb(target_file=''):
    lines = parser.read_morpheme(target_file)
    verbs = []
    try:
        for line in lines:
            for morpheme in line:
                if morpheme['pos'] == '動詞':
                    verbs.append(morpheme['base'])
    except:
        pass
    return verbs


if __name__ == '__main__':
    extract_original_verb('./data/neko.txt.mecab')
