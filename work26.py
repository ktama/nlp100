# -*- Coding: utf-8 -*-
import re
import utility.print_method_result as util
import utility.extract as ext


# 26. 強調マークアップの除去
# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
# （弱い強調，強調，強い強調のすべて）
# を除去してテキストに変換せよ（参考: マークアップ早見表）．


@util.print_result
def extract_remove_markup_emphasis(target_json='', target_content=''):
    extracted1 = ext.extract_template(target_json, target_content)
    extracted2 = ext.remove_markup_emphasis(extracted1)
    return extracted2


if __name__ == '__main__':
    extract_remove_markup_emphasis('./data/jawiki-country.json.gz', 'イギリス')
