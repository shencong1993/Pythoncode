# coding=utf-8
# 异常机制
class MuffledCalculator:
    muffled = False
    def calc(self,expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print 'Division by zero is illegal'
            else:
                raise


calculator = MuffledCalculator()
print calculator.calc('10/2')
# calculator.calc('10/0')

calculator.muffled = True
calculator.calc('10/0')