# -*- Coding: utf-8 -*-
import re
import utility.print_method_result as util
import utility.extract as ext

# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．


@util.print_result
def extract_media(target_json='', target_content=''):
    repatter = re.compile(r'''
        (?:File|ファイル) # キャプチャ対象、
        :
        (.+?)   # キャプチャ対象、任意の文字が1文字以上、非貪欲（以降の条件の巻き込み防止）
        \|
        ''', re.MULTILINE + re.VERBOSE)
    json_contents = ext.extract_content(target_json, target_content)
    extracted = repatter.findall(json_contents[0])

    return extracted


if __name__ == '__main__':
    extract_media('./data/jawiki-country.json.gz', 'イギリス')
