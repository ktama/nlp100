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


def remove_markup_emphasis(target_dictionary={}):
    repatter = re.compile(r'''
        (\'{2,5}) # 2～5個の'
        (.*?)
        (\1)
        ''', re.MULTILINE + re.VERBOSE)
    extracted = {}
    for k, v in target_dictionary.items():
        extracted[k] = repatter.sub(r'\2', v)
    return extracted


def remove_markup_internal_link(target_dictionary={}):
    repatter = re.compile(r'''
        \[\[        # '[['（マークアップの開始）
        (?:         # キャプチャ対象外のグループ開始
            [^|]*?  # '|'以外の文字が0文字以上、非貪欲
            \|      # '|'
        )*?         # グループ終了、このグループが0か1出現、非貪欲
        ([^|]*?)    # キャプチャ対象、'|'以外が0文字以上、非貪欲（表示対象の文字列）
        \]\]        # ']]'（マークアップの終了）
        ''', re.MULTILINE + re.VERBOSE)
    extracted = {}
    for k, v in target_dictionary.items():
        extracted[k] = repatter.sub(r'\1', v)
    return extracted


def remove_markup_mediawiki(target_dictionary={}):
    # 内部リンク、ファイルの除去
    repatter1 = re.compile(r'''
        \[\[        # '[['（マークアップの開始）
        (?:         # キャプチャ対象外のグループ開始
            [^|]*?  # '|'以外の文字が0文字以上、非貪欲
            \|      # '|'
        )*?         # グループ終了、このグループが0か1出現、非貪欲
        ([^|]*?)    # キャプチャ対象、'|'以外が0文字以上、非貪欲（表示対象の文字列）
        \]\]        # ']]'（マークアップの終了）
        ''', re.MULTILINE + re.VERBOSE)
    extracted1 = {}
    for k, v in target_dictionary.items():
        extracted1[k] = repatter1.sub(r'\1', v)

    # Template:Langの除去        {{lang|言語タグ|文字列}}
    repatter2 = re.compile(r'''
        \{\{lang    # '{{lang'（マークアップの開始）
        (?:         # キャプチャ対象外のグループ開始
            [^|]*?  # '|'以外の文字が0文字以上、非貪欲
            \|      # '|'
        )*?         # グループ終了、このグループが0以上出現、非貪欲
        ([^|]*?)    # キャプチャ対象、'|'以外が0文字以上、非貪欲（表示対象の文字列）
        \}\}        # '}}'（マークアップの終了）
        ''', re.MULTILINE + re.VERBOSE)
    extracted2 = {}
    for k, v in extracted1.items():
        extracted2[k] = repatter2.sub(r'\1', v)

    # 外部リンクの除去  [http://xxxx] 、[http://xxx xxx]
    repatter3 = re.compile(r'''
        \[http:\/\/ # '[http://'（マークアップの開始）
        (?:         # キャプチャ対象外のグループ開始
            [^\s]*? # 空白以外の文字が0文字以上、非貪欲
            \s      # 空白
        )?          # グループ終了、このグループが0か1出現
        ([^]]*?)    # キャプチャ対象、']'以外が0文字以上、非貪欲（表示対象の文字列）
        \]          # ']'（マークアップの終了）
        ''', re.MULTILINE + re.VERBOSE)
    extracted3 = {}
    for k, v in extracted2.items():
        extracted3[k] = repatter3.sub(r'\1', v)

    # <br>、<ref>の除去
    repatter4 = re.compile(r'''
        <           # '<'（マークアップの開始）
        \/?         # '/'が0か1出現（終了タグの場合は/がある）
        [br|ref]    # 'br'か'ref'
        [^>]*?      # '>'以外が0文字以上、非貪欲
        >           # '>'（マークアップの終了）
        ''', re.MULTILINE + re.VERBOSE)
    extracted4 = {}
    for k, v in extracted3.items():
        extracted4[k] = repatter4.sub('', v)

    return extracted4


if __name__ == '__main__':
    extract_content('./data/jawiki-country.json.gz', 'イギリス')
