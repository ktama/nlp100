# -*- Coding: utf-8 -*-
import utility.print_method_result as util

# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．
# 確認にはsort, uniqコマンドを用いよ．

# Unix コマンド
# cut -f 1 hightemp.txt | sort | uniq


@util.print_result
def count_unique(target_file=''):
    target = []
    with open(target_file, encoding='utf-8') as f:
        target = f.readlines()
    cells = [x.split('\t') for x in target]
    columns = [x[0] for x in cells]
    return set(columns)


if __name__ == '__main__':
    count_unique('./data/hightemp.txt')
