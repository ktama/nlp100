# -*- Coding: utf-8 -*-
import utility.print_method_result as util

# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ
# （注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ
# （この問題はコマンドで実行した時の結果と合わなくてもよい）．

# Unix コマンド
# sort hightemp.txt -k 3 --numeric-sort --reverse


@util.print_result
def sort_int(target_file='', key_index=2):
    lines = []
    with open(target_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    lines.sort(key=lambda x: float(x.split('\t')[key_index]), reverse=True)
    return lines


if __name__ == '__main__':
    sort_int('./data/hightemp.txt')
