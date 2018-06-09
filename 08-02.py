# coding=utf-8
# 捕捉对象

try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print x/y
except (ZeroDivisionError,TypeError),e:
    print e


# 万事大吉，循环直到顺利运行
while True:
    try:
        x = input('Enter the first number: ')
        y = input('Enter the second number: ')
        value = x/y
        print 'x/y is ',value
    except Exception, e:
        print 'Invalid input: ',e
        print 'Please tyr again'
    else:
        break
