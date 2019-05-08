# -*- Coding: utf-8 -*-

# 01. 「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

# https://qiita.com/Ryusei-KAKUBARI/items/b3ab63c2208b654352b9
# スライス
# word[(始点):(終点):(ステップ数)] 
def slice_pair(target_str=''):
    
    return (target_str[::2], target_str[1::2])

if __name__ == '__main__':
    (left, right) = slice_pair('パタトクカシーー')
    print(left)
    print(right)
