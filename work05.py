# -*- Coding: utf-8 -*-

# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）から
# n-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

# https://qiita.com/kazmaw/items/4df328cba6429ec210fb


def n_gram(target_str='', n=1):
    return [target_str[index: index + n] for index in range(len(target_str) - n + 1)]


if __name__ == '__main__':
    dic = n_gram('I am an NLPer', 1)
    print(dic)
    dic = n_gram('I am an NLPer', 2)
    print(dic)
    dic = n_gram('I am an NLPer', 3)
    print(dic)
    words = 'I am an NLPer'.split(' ')
    dic = n_gram(words, 1)
    print(dic)
    dic = n_gram(words, 2)
    print(dic)
    dic = n_gram(words, 3)
    print(dic)
