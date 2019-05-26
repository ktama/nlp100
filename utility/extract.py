# -*- Coding: utf-8 -*-
import gzip
import json
import re


def extract_content(target_json='', target_content=''):
    target_contents = []
    with gzip.open(target_json, 'rt', encoding='utf-8') as f:
        for line in f:
            json_data = json.loads(line)
            if json_data['title'] == target_content:
                target_contents.append(json_data['text'])
    return target_contents


def extract_template(target_json='', target_content=''):
    repatter1 = re.compile(r'''
        ^\{\{基礎情報.*?$   # 行頭で{基礎情報で始まる行
        (.+?)   # キャプチャ対象、任意の文字が1文字以上、非貪欲（以降の条件の巻き込み防止）
        ^\}\}$
        ''', re.MULTILINE + re.VERBOSE + re.DOTALL)
    json_contents = extract_content(target_json, target_content)
    extracted1 = repatter1.findall(json_contents[0])

    repatter2 = re.compile(r'''
        ^\|         # '|'で始まる行
        (.+?)       # キャプチャ対象（フィールド名）、任意の1文字以上、非貪欲
        \s*         # 空白文字0文字以上
        =
        \s*         # 空白文字0文字以上
        (.+?)       # キャプチャ対象（値）、任意の1文字以上、非貪欲
        (?:         # キャプチャ対象外のグループ開始
            (?=\n\|)    # 改行+'|'の手前（肯定の先読み）
            | (?=\n$)   # または、改行+終端の手前（肯定の先読み）
        )           # グループ終了
        ''', re.MULTILINE + re.VERBOSE + re.DOTALL)
    extracted2 = repatter2.findall(extracted1[0])
    dic = dict(extracted2)

    return dic


if __name__ == '__main__':
    extract_content('./data/jawiki-country.json.gz', 'イギリス')
