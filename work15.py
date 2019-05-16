# -*- Coding: utf-8 -*-
import utility.print_method_result as util

# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．

# Unix コマンド
# tail -n 0 hightemp.txt
# tail -n 3 hightemp.txt
# tail -n 5 hightemp.txt
# tail -n 7 hightemp.txt


@util.print_result
def print_n_bottom_lines(target_file='', n=0):
    with open(target_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        tails = [line for (index, line) in enumerate(lines[::-1]) if index < n]
        return tails[::-1]


if __name__ == '__main__':
    print_n_bottom_lines('./data/hightemp.txt', 0)
    print_n_bottom_lines('./data/hightemp.txt', 3)
    print_n_bottom_lines('./data/hightemp.txt', 5)
    print_n_bottom_lines('./data/hightemp.txt', 7)
