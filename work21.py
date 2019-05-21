# -*- Coding: utf-8 -*-
import re
import utility.print_method_result as util
import utility.extract as ext

# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．


@util.print_result
def extract_category(target_json='', target_content=''):
    repatter = re.compile(r'''
        ^   # 行頭
        (   # キャプチャ対象のグループ開始
        .*  # 任意の文字0文字以上
        \[\[Category:
        .*  # 任意の文字0文字以上
        \]\]
        .*  # 任意の文字0文字以上
        )   # グループ終了
        $   # 行末
        ''', re.MULTILINE + re.VERBOSE)
    json_contents = ext.extract_content(target_json, target_content)
    extracted = repatter.findall(json_contents[0])
    return 0


if __name__ == '__main__':
    extract_category('./data/jawiki-country.json.gz', 'イギリス')
