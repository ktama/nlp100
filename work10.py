# -*- Coding: utf-8 -*-
import utility.print_method_result as util

# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

# Unix コマンド wc --line hightemp.txt


@util.print_result
def count_line(target_file=''):
    with open(target_file, encoding='utf-8') as f:
        return len(f.readlines())


if __name__ == '__main__':
    count_line('./data/hightemp.txt')
