# -*- Coding: utf-8 -*-
import gzip
import json
import utility.print_method_result as util

# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，
# 「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．

# ファイルを取得
# wget http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz
# 解凍
# gzip -d jawiki-country.json.gz


@util.print_result
def read_json(target_json='', target_content=''):
    target_contents = []
    with gzip.open(target_json, 'rt', encoding='utf-8') as f:
        for line in f:
            json_data = json.loads(line)
            if json_data['title'] == target_content:
                target_contents.append(json_data['text'])
    return target_contents


if __name__ == '__main__':
    read_json('./data/jawiki-country.json.gz', 'イギリス')
