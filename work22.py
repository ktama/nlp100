# -*- Coding: utf-8 -*-
import re
import utility.print_method_result as util
import utility.extract as ext

# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

# 難しすぎてカンニングした……。 「|*」 が取れんかった


@util.print_result
def extract_category_name(target_json='', target_content=''):
    repatter = re.compile(r'''
        ^   # 行頭
        .*  # 任意の文字0文字以上
        \[\[Category:
        (   # キャプチャ対象のグループ開始
        .*?  # 任意の文字0文字以上
        )   # グループ終了
        (?:   # キャプチャ対象のグループ開始
        \|.*  # '|'に続く0文字以上
        )?   # グループ終了
        \]\]
        .*  # 任意の文字0文字以上
        $   # 行末
        ''', re.MULTILINE + re.VERBOSE)
    json_contents = ext.extract_content(target_json, target_content)
    extracted = repatter.findall(json_contents[0])
    return 0


if __name__ == '__main__':
    extract_category_name('./data/jawiki-country.json.gz', 'イギリス')
