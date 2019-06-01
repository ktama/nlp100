# -*- Coding: utf-8 -*-
import utility.print_method_result as util
import utility.parser as parser

# 34. 「AのB」
# 2つの名詞が「の」で連結されている名詞句を抽出せよ．


@util.print_result
def extract_noum_phrase(target_file=''):
    lines = parser.read_morpheme(target_file)
    noun_phrases = []
    try:
        for line in lines:
            if len(line) > 2:
                for i in range(1, len(line) - 1):
                    if line[i]['surface'] == 'の' and line[i-1]['pos'] == '名詞' and line[i+1]['pos'] == '名詞':
                        noun_phrases.append(
                            line[i-1]['surface']+line[i]['surface']+line[i+1]['surface'])
    except:
        pass
    return noun_phrases


if __name__ == '__main__':
    extract_noum_phrase('./data/neko.txt.mecab')
