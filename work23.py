# -*- Coding: utf-8 -*-
import re
import utility.print_method_result as util
import utility.extract as ext


# 23. セクション構造
# 記事中に含まれるセクション名と
# そのレベル（例えば"== セクション名 =="なら1）を表示せよ．


@util.print_result
def extract_section(target_json='', target_content=''):
    repatter = re.compile(r'''
        ^       # 行頭
        (={2,}) # キャプチャ対象、2個以上の'='
        \s*     # 余分な0個以上の空白（'哲学'や'婚姻'の前後に余分な空白があるので除去）
        (.+?)   # キャプチャ対象、任意の文字が1文字以上、非貪欲（以降の条件の巻き込み防止）
        \s*     # 余分な0個以上の空白
        \1      # 後方参照、1番目のキャプチャ対象と同じ内容
        .*      # 任意の文字が0文字以上
        $       # 行末
        ''', re.MULTILINE + re.VERBOSE)
    json_contents = ext.extract_content(target_json, target_content)
    extracted = repatter.findall(json_contents[0])

    levels = []
    for line in extracted:
        level = len(line[0]) - 1
        levels.append(str(level) + ':' + line[1])
    return levels


if __name__ == '__main__':
    extract_section('./data/jawiki-country.json.gz', 'イギリス')
