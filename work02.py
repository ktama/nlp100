# -*- Coding: utf-8 -*-

# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

# zip関数を使う
# https://qiita.com/Ryusei-KAKUBARI/items/b3ab63c2208b654352b9

import utility.print_method_result as util


@util.print_result
def zip_pair(left_target_str='', right_target_str=''):
    zip_str = ''

    for (left, right) in zip(left_target_str, right_target_str):
        zip_str += (left + right)
    return zip_str


if __name__ == '__main__':
    zip_pair('パトカー', 'タクシー')
