# coding=utf-8
# 检查用户名和PIN码

database = [
    ['aaaa','1234'],
    ['bbbb','2345'],
    ['cccc','3456'],
    ['dddd','4567']
]

username = raw_input('Plsease enter the username: ')
pin = raw_input('PIN code: ')
if[username,pin] in database:print 'Access granted'