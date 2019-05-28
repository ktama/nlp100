# -*- Coding: utf-8 -*-
import utility.print_method_result as util

# 30. 形態素解析結果の読み込み
# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
# ただし，各形態素は表層形（surface），基本形（base），
# 品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
# 1文を形態素（マッピング型）のリストとして表現せよ．
# 第4章の残りの問題では，ここで作ったプログラムを活用せよ．

# MeCab： https://taku910.github.io/mecab/
# 出力フォーマット： 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音

# 使う列は
# 表層形（surface）： タブ区切りの index 0
# 基本形（base）： タブ区切りの index 1 の カンマ区切りの index 6
# 品詞（pos）： タブ区切りの index 1 の カンマ区切りの index 0
# 品詞細分類1（pos1）： タブ区切りの index 1 の カンマ区切りの index 1


# @util.print_result
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


if __name__ == '__main__':
    lines = read_morpheme('./data/neko.txt.mecab')
    try:
        for line in lines:
            print(morphem)
    except:
        pass
