# coding=utf-8
name1 = raw_input('plsase enter the name: ') or 'unknown' # 如果不输入就直接复制unknown给name

name2 = 'a' if (1<2) else 'c'   # a if b else c 如果b为真，则返回啊，否则返回c

age = 10
assert 0<age<100, 'The age must be realistic'  # 断言语句，用来确保语句中某些条件为真，可添加解释语句

range(0,10,step=1)  # 包括0，不包括10，步长为1~可用在 for each in range(0,10),若下限为0，则可省略

name = ['a','b','c']
age = [12,34,23]
zip(name,age) # 并行迭代，能用来把name和age并行打印，并且是元祖的形式，并且还能处理不等长的
zip(range(10),xrange(100000))  # xrange只计算前10个数字，后面的不算，和range(直接计算所有的数字)不同

for index,string in enumerate(strings):
    if 'xxx' in string:
        strings[index] = '[censored]'   # 这个函数可以在提供索引的地方迭代索引-值对