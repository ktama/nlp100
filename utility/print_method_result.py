# -*- Coding: utf-8 -*-
# https://qiita.com/mtb_beta/items/d257519b018b8cd0cc2e


def print_result(func):
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        print(ret)
        return ret
    return wrapper


@print_result
def test():
    return 'test'


if __name__ == '__main__':
    test()
