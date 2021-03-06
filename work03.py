# -*- Coding: utf-8 -*-

# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

import utility.print_method_result as util


@util.print_result
def count_alphabet(target_str=''):
    words = target_str.strip(',.').split(' ')
    return list(map(lambda x: len(x), words))


if __name__ == '__main__':
    count_alphabet(
        'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.')
