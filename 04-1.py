# coding=utf-8
# 一个简单的数据库
# 字典使用人名作为键，每个人用另一个字典来表示，其键‘phone’和‘addr’分别表示他们的电话号码和地址

people={
    'Alice':{'phone':'2341','addr':'Foo drive 23'},
    'Beth':{'phone':'9102','addr':'Berl Street 42'},
    'Cecil':{'phone':'3158','addr':'Baz avenue 90'},
}

# 针对电话号码和地址使用的描述性标签，会在打印输出的时候用到
label = {
    'phone':'phone number',
    'addr':'address'
}

name = raw_input('Plesase input the mame for searching: ')

# 查找电话号码还是地址
request = raw_input('Phone number(p) or address(a): ')

# 判断是p或者是a
if request == 'a': key = 'address'
if request == 'p': key = 'phone'

# 打印
if name in people:print "%s's %s is %s." % (name,label[key],people[name][key])