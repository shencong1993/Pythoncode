# coding=utf-8
# 静态方法和类成员方法

__metaclass__ = type

class MyClass:
    @staticmethod
    def smeth():
        print 'This is a static method'

    @classmethod
    def cmeth(cls):
        print 'This is a class method of',cls