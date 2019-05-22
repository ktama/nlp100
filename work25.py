# -*- Coding: utf-8 -*-
import re
import utility.print_method_result as util
import utility.extract as ext

# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
# 辞書オブジェクトとして格納せよ．


@util.print_result
def extract_template(target_json='', target_content=''):
    repatter1 = re.compile(r'''
        ^\{\{基礎情報.*?$   # 行頭で{基礎情報で始まる行
        (.+?)   # キャプチャ対象、任意の文字が1文字以上、非貪欲（以降の条件の巻き込み防止）
        ^\}\}$
        ''', re.MULTILINE + re.VERBOSE + re.DOTALL)
    json_contents = ext.extract_content(target_json, target_content)
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
    extract_template('./data/jawiki-country.json.gz', 'イギリス')
