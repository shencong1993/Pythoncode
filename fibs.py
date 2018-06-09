# coding=utf-8
# 定义函数计算斐波那契数列
def fibs(num):
    'calculate the fibs :'
    result = [0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result


print fibs(10)