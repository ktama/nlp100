# -*- Coding: utf-8 -*-

# 00. 文字列の逆順
# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

# 参考
# 配列反転させるだけ
# https://qiita.com/Hawk84/items/ecd0c7239e490ea22308

import utility.print_method_result as util


@util.print_result
def reverse(target_str=''):
    return target_str[::-1]


if __name__ == '__main__':
    reverse('stressed')
