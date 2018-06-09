# coding=utf-8
# python的嵌套作用域
def multiplier(factor):
    def multiplyByFactor(number):
        return factor*number
    return multiplyByFactor

double = multiplier(5)
print double(2)

print multiplier(3)(2)
