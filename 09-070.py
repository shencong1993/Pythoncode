# coding=utf-8
# 生成器  包含yeild的函数称为生成器
# 创建生成器


nested = [[1,2],[3,4],[5]]

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

print list(flatten(nested))