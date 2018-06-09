# coding=utf-8
# 以正确的宽度在居中的“盒子”内打印一个句子
# 注意，整数除法运算符（//）只能用在python2.2以后的版本，在之前的版本中统一用（/）

sentence = raw_input('Please enter a sentence: ')

screen_width = 80
text_width = len(sentence)
box_width = text_width+6
left_margin = (box_width-text_width)//2

print
print ' '*left_margin+'+'+(text_width-2)*'-'+'+'
print ' '*left_margin+'|'+' '*text_width+'|'
print ' '*left_margin+'|'+sentence+'|'
print ' '*left_margin+'|'+' '*text_width+'|'
print ' '*left_margin+'+'+(text_width-2)*'-'+'+'