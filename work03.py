# -*- Coding: utf-8 -*-

# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

def count_alphabet(target_str=''):
    words = target_str.replace(',', '').replace('.', '').split(' ')
    return map(lambda x: len(x), words)

if __name__ == '__main__':
    count_list = count_alphabet('Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.')
    for count in count_list:
        print(count)
