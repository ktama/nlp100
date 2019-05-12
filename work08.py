# -*- Coding: utf-8 -*-
import utility.print_method_result as util

# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．


@util.print_result
def cipher(target=''):
    s = []
    for x in target:
        if x.islower():
            s.append(chr(219 - ord(x)))
        else:
            s.append(x)
    return ''.join(s)


if __name__ == '__main__':
    ret = cipher('Hello world')
    cipher(ret)
