# -*- Coding: utf-8 -*-
import urllib.request
import json
import utility.print_method_result as util
import utility.extract as ext

# 29. 国旗画像のURLを取得する
# テンプレートの内容を利用し，
# 国旗画像のURLを取得せよ．
# （ヒント: MediaWiki APIのimageinfoを呼び出して，
# ファイル参照をURLに変換すればよい）

# https://www.mediawiki.org/wiki/API:Properties/ja
# https://www.mediawiki.org/wiki/API:Images


@util.print_result
def extract_flag_image_url(target_json='', target_content=''):
    extracted1 = ext.extract_template(target_json, target_content)
    extracted2 = ext.remove_markup_emphasis(extracted1)
    extracted3 = ext.remove_markup_internal_link(extracted2)
    extracted4 = ext.remove_markup_mediawiki(extracted3)
    source = extracted4['国旗画像']

    url = 'https://www.mediawiki.org/w/api.php' \
        + '?action=query' \
        + '&titles=File:' + urllib.parse.quote(source) \
        + '&format=json' \
        + '&prop=imageinfo' \
        + '&iiprop=url'

    request = urllib.request.Request(
        url, headers={'User-Agent': 'NLP100(@ktama06)'})
    connection = urllib.request.urlopen(request)
    data = json.loads(connection.read().decode())
    image_url = data['query']['pages'].popitem()[1]['imageinfo'][0]['url']
    return image_url


if __name__ == '__main__':
    extract_flag_image_url('./data/jawiki-country.json.gz', 'イギリス')
