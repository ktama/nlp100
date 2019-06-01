# -*- Coding: utf-8 -*-
import utility.print_method_result as util
import utility.parser as parser

# 33. サ変名詞
# サ変接続の名詞をすべて抽出せよ．


@util.print_result
def extract_sa_line(target_file=''):
    lines = parser.read_morpheme(target_file)
    noun = []
    try:
        for line in lines:
            for morpheme in line:
                if morpheme['pos'] == '名詞' and morpheme['pos1'] == 'サ変接続':
                    noun.append(morpheme['base'])
    except:
        pass
    return noun


if __name__ == '__main__':
    extract_sa_line('./data/neko.txt.mecab')
