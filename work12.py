# -*- Coding: utf-8 -*-
import utility.print_method_result as util

# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，
# 2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．


# Unix コマンド
# cut -f 1 hightemp.txt
# cut -f 2 hightemp.txt


@util.print_result
def split_column(target_file=''):
    target = []
    with open(target_file, encoding='utf-8') as f:
        target = f.readlines()
    cells = [x.split('\t') for x in target]
    for i in range(2):
        with open('./data/col' + str(i + 1) + '.txt', mode='w', encoding='utf-8') as f:
            columns = [x[i] for x in cells]
            f.write('\n'.join(columns))
    print()


if __name__ == '__main__':
    split_column('./data/hightemp.txt')
