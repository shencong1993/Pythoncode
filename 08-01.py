# coding=utf-8

try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print x/y
except ZeroDivisionError:
    print "The second number can't be zero!"
except TypeError:
    print "That wasn't a number, was it?"


# 或者except (ZeroDivisionError,TypeError,NameError)
#     print .....用一个异常捕捉块可实现