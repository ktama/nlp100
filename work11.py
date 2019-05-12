# -*- Coding: utf-8 -*-
import utility.print_method_result as util

# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

# Unix コマンド
# sed 's/\t/ /g' hightemp.txt
# tr '\t' ' ' < hightemp.txt
# expand --tabs=1 hightemp.txt


@util.print_result
def replace_space(target_file=''):
    with open(target_file, encoding='utf-8') as f:
        target = f.readlines()
        return [x.replace('\t', ' ') for x in target]


if __name__ == '__main__':
    replace_space('./data/hightemp.txt')
