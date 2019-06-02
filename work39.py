# -*- Coding: utf-8 -*-
from matplotlib import pyplot
from matplotlib.font_manager import FontProperties
import utility.print_method_result as util
import utility.parser as parser

# 39. Zipfの法則
# 単語の出現頻度順位を横軸，
# その出現頻度を縦軸として，
# 両対数グラフをプロットせよ．


@util.print_result
def plot_word_count_top(target_file=''):
    word_count_list = parser.extract_word_count(target_file)
    counts = list(zip(*word_count_list))[1]
    font = FontProperties(fname='C:/Windows/Fonts/HackGen-Regular_0.ttf')
    pyplot.scatter(range(1, len(counts) + 1), counts)
    pyplot.xlim(xmin=1, xmax=len(counts) + 1)
    pyplot.ylim(ymin=1, ymax=counts[0])
    pyplot.xscale('log')
    pyplot.yscale('log')
    pyplot.title('Word Count Zipf\'s law', fontproperties=font)
    pyplot.xlabel('出現度順位', fontproperties=font)
    pyplot.ylabel('出現頻度', fontproperties=font)
    pyplot.grid(axis='both')
    pyplot.show()
    return word_count_list


if __name__ == '__main__':
    plot_word_count_top('./data/neko.txt.mecab')
