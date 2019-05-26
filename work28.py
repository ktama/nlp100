# -*- Coding: utf-8 -*-
import utility.print_method_result as util
import utility.extract as ext

# 28. MediaWikiマークアップの除去
# 27の処理に加えて，
# テンプレートの値からMediaWikiマークアップを可能な限り除去し，
# 国の基本情報を整形せよ．


@util.print_result
def extract_remove_markup_mediawiki(target_json='', target_content=''):
    extracted1 = ext.extract_template(target_json, target_content)
    extracted2 = ext.remove_markup_emphasis(extracted1)
    extracted3 = ext.remove_markup_internal_link(extracted2)
    extracted4 = ext.remove_markup_mediawiki(extracted3)
    return extracted4


if __name__ == '__main__':
    extract_remove_markup_mediawiki('./data/jawiki-country.json.gz', 'イギリス')
