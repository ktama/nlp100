# -*- Coding: utf-8 -*-
import re
import utility.print_method_result as util
import utility.extract as ext

# 27. 内部リンクの除去
# 26の処理に加えて，
# テンプレートの値からMediaWikiの内部リンクマークアップを除去し，
# テキストに変換せよ（参考: マークアップ早見表）．


@util.print_result
def extract_remove_markup_internal_link(target_json='', target_content=''):
    extracted1 = ext.extract_template(target_json, target_content)
    extracted2 = ext.remove_markup_emphasis(extracted1)
    extracted3 = ext.remove_markup_internal_link(extracted2)
    return extracted3


if __name__ == '__main__':
    extract_remove_markup_internal_link(
        './data/jawiki-country.json.gz', 'イギリス')
