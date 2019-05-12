# -*- Coding: utf-8 -*-
import utility.print_method_result as util
from work05 import n_gram


@util.print_result
def to_set(target=''):
    return set(n_gram(target, 2))


@util.print_result
def classify_union(x_set, y_set):
    return x_set.union(y_set)


@util.print_result
def classify_intersection(x_set, y_set):
    return x_set.intersection(y_set)


@util.print_result
def classify_difference(x_set, y_set):
    return x_set.difference(y_set)


@util.print_result
def is_include(s, key=''):
    return key in s


if __name__ == '__main__':
    x = to_set('paraparaparadise')
    y = to_set('paragraph')
    classify_union(x, y)
    classify_intersection(x, y)
    classify_difference(x, y)
    is_include(x, 'se')
    is_include(y, 'se')
