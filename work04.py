# -*- Coding: utf-8 -*-

# 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，
# 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
# それ以外の単語は先頭に2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

import utility.print_method_result as util


@util.print_result
def count_dic(target_str=''):
    words = target_str.strip(',.').split(' ')
    dic = {}
    for index, word in enumerate(words, 1):
        if index in (1, 5, 6, 7, 8, 9, 15, 16, 19):
            dic[word[:1]] = index
        else:
            dic[word[:2]] = index

    return dic


if __name__ == '__main__':
    count_dic(
        'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.')
