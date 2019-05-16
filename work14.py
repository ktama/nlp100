# -*- Coding: utf-8 -*-
import utility.print_method_result as util

# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．

# Unix コマンド
# head -n 0 hightemp.txt
# head -n 3 hightemp.txt
# head -n 5 hightemp.txt
# head -n 7 hightemp.txt


@util.print_result
def print_n_top_lines(target_file='', n=0):
    with open(target_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return [line for (index, line) in enumerate(lines) if index < n]


if __name__ == '__main__':
    print_n_top_lines('./data/hightemp.txt', 0)
    print_n_top_lines('./data/hightemp.txt', 3)
    print_n_top_lines('./data/hightemp.txt', 5)
    print_n_top_lines('./data/hightemp.txt', 7)
