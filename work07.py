# -*- Coding: utf-8 -*-
import utility.print_method_result as util


@util.print_result
def template(x=10, y='', z=20.0):
    return str(x) + '時の' + str(y) + 'は' + str(z)


if __name__ == '__main__':
    template(x=12, y='気温', z=22.4)
