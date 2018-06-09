# coding=utf-8
# 男生女生的名字配对问题（首字母相同的男女生名字配到一起）

girls = ['alice','bernice','clarice']
boys = ['chirs','arnold','bob']

# case 1: [b+'+'+g for b in boys for g in girls if b[0]==g[0]]

letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0],[],).append(girl)

print [b+'+'+g for b in boys for g in letterGirls[b[0]]]