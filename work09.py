# -*- Coding: utf-8 -*-
import numpy

import utility.print_method_result as util

# 09. Typoglycemia
# スペースで区切られた単語列に対して，
# 各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文
# （例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，
# その実行結果を確認せよ．


@util.print_result
def typoglycemia(target=''):
    words = target.split(' ')
    s = []
    for word in words:
        if 4 < len(word):
            part = [w for w in word[1:-1]]
            numpy.random.shuffle(part)
            s.append(''.join([word[0]] + part + [word[-1]]))
        else:
            s.append(word)
    return ' '.join(s)


if __name__ == '__main__':
    typoglycemia(
        'I couldn\'t believe that I could actually understand what I was reading: the phenomenal power of the human mind .')
