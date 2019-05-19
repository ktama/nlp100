# -*- Coding: utf-8 -*-
from itertools import groupby
import utility.print_method_result as util

# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，
# その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．

# Unix コマンド
# cut -f 1 hightemp.txt | sort | uniq -c | sort -r


@util.print_result
def sort_count(target_file=''):
    lines = []
    with open(target_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    cells = [x.split('\t') for x in lines]
    columns = [x[0] for x in cells]
    columns.sort()
    dic = [(column, len(list(group))) for column, group in groupby(columns)]
    dic.sort(key=lambda x: x[1], reverse=True)
    return dic


if __name__ == '__main__':
    sort_count('./data/hightemp.txt')
