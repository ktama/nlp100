# -*- Coding: utf-8 -*-
from matplotlib import pyplot
from matplotlib.font_manager import FontProperties
import utility.print_method_result as util
import utility.parser as parser

# 38. ヒストグラム
# 単語の出現頻度のヒストグラム
# （横軸に出現頻度，縦軸に出現頻度をとる
# 単語の種類数を棒グラフで表したもの）
# を描け．


@util.print_result
def plot_word_count_histogram(target_file=''):
    word_count_list = parser.extract_word_count(target_file)
    words, counts = list(zip(*word_count_list))
    font = FontProperties(fname='C:/Windows/Fonts/HackGen-Regular_0.ttf')
    pyplot.hist(counts, bins=50, range=(1, 50))
    pyplot.xlim(xmin=1, xmax=50)
    pyplot.title('Word Count Histogram', fontproperties=font)
    pyplot.xlabel('出現頻度', fontproperties=font)
    pyplot.ylabel('単語の種類数', fontproperties=font)
    pyplot.grid(axis='y')
    pyplot.show()
    return word_count_list


if __name__ == '__main__':
    plot_word_count_histogram('./data/neko.txt.mecab')
