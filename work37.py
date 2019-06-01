# -*- Coding: utf-8 -*-
from matplotlib import pyplot
from matplotlib.font_manager import FontProperties
import utility.print_method_result as util
import utility.parser as parser

# 37. 頻度上位10語
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．


@util.print_result
def plot_word_count_top(target_file=''):
    word_count_list = parser.extract_word_count(target_file)
    top_num = 10
    top_10 = word_count_list[:top_num]
    words, counts = list(zip(*top_10))
    font = FontProperties(fname='C:/Windows/Fonts/HackGen-Regular_0.ttf')
    pyplot.bar(range(0, top_num), counts, align='center')
    pyplot.xticks(range(0, top_num), words, fontproperties=font)
    pyplot.xlim(xmin=-1, xmax=top_num)
    pyplot.title('Word Count Top 10', fontproperties=font)
    pyplot.xlabel('Words', fontproperties=font)
    pyplot.ylabel('Count', fontproperties=font)
    pyplot.grid(axis='y')
    pyplot.show()
    return top_10


if __name__ == '__main__':
    plot_word_count_top('./data/neko.txt.mecab')
