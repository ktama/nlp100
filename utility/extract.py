# -*- Coding: utf-8 -*-
import gzip
import json


def extract_content(target_json='', target_content=''):
    target_contents = []
    with gzip.open(target_json, 'rt', encoding='utf-8') as f:
        for line in f:
            json_data = json.loads(line)
            if json_data['title'] == target_content:
                target_contents.append(json_data['text'])
    return target_contents


if __name__ == '__main__':
    extract_content('./data/jawiki-country.json.gz', 'イギリス')
