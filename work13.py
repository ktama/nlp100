# -*- Coding: utf-8 -*-
import utility.print_method_result as util

# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，
# 元のファイルの1列目と2列目をタブ区切りで
# 並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．

# Unix コマンド
# paste col1.txt col2.txt


@util.print_result
def merge_column(left_file='', right_file='', merged_file=''):
    left = []
    with open(left_file, 'r', encoding='utf-8') as f:
        left = f.readlines()
    right = []
    with open(right_file, 'r', encoding='utf-8') as f:
        right = f.readlines()
    merged = [l.replace('\n', '') + '\t' + r for (l, r) in zip(left, right)]
    with open(merged_file, 'w', encoding='utf-8') as f:
        f.writelines(merged)


if __name__ == '__main__':
    merge_column('./data/col1.txt', './data/col2.txt', './data/merged.txt')
