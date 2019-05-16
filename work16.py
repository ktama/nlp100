# -*- Coding: utf-8 -*-
import utility.print_method_result as util

# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

# Unix コマンド
# split --lines=3 --numeric-suffixes=1 --additional-suffix=.txt hightemp.txt split


@util.print_result
def split_n_files(target_file='', n=0):
    lines = []
    with open(target_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    file_line_num = len(lines) // n
    end_index = 0
    for i in range(0, n):
        start_index = i*file_line_num
        end_index = start_index+file_line_num
        file_lines = lines[start_index:end_index]
        with open('./data/split' + str(i) + '.txt', mode='w', encoding='utf-8') as f:
            f.writelines(file_lines)
    if end_index < len(lines):
        file_lines = lines[end_index:]
        with open('./data/split' + str(n) + '.txt', mode='w', encoding='utf-8') as f:
            f.writelines(file_lines)


if __name__ == '__main__':
    split_n_files('./data/hightemp.txt', 1)
    split_n_files('./data/hightemp.txt', 2)
    split_n_files('./data/hightemp.txt', 3)
    split_n_files('./data/hightemp.txt', 7)
    split_n_files('./data/hightemp.txt', 24)
