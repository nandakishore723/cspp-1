# # -*- coding: utf-8 -*-
# """
# Created on Wed Jun  8 11:07:33 2016

# @author: ericgrimson
# """

# if x%2 == 0:
#     if x%3 == 0:
#         print('Divisible by 2 and 3')
#     else:
#         print('Divisible by 2 and not by 3')
# elif x%3 == 0:
#     print('Divisible by 3 and not by 2')
# import operator
# t = ()
# print(t)
# t = ('me','u')
# print(t)
# print(t)
# s= set([1,2,2,3,4,4,5,'me',6])
# print(s)
# d = {}
# print(d)
# d = dict([(1, 'me'),(2,'u')])
# print(d)
# d = {1:'me',2:'u'}
# print(d)
# d = {1:'me',2:'u',3:{1:'me',2:'u'}}
# print(d)
# d1 = d.copy()
# print(d1)
# #type(d1)
# print(type(d1))

# x = 100
# y = 4000
# x, y = y, x
# print(x,y)

# a = 4; b =2
# print(a+b)
# print(a*b)
# print(a>b)
# print(a<b)
# print(a==b)
# print(a/b)
# print(a//b)
# print(a%b)

# print(a is not b)
# max = a if a>b else b
# print(max)
# print(any ([False,False]))
# print(any ([False,False,True]))
# print(any ([True,False,False]))
# print(all ([False,False]))
# print(all ([False,False,True]))
# print(all ([True,True]))

# print(operator.add(a, b))
# print(operator.sub(a, b))
# print(operator.mul(a, b))
# print(operator.truediv(a, b))
# print(operator.floordiv(a, b))
# print(operator.mod(a, b))

# import array
# count = 0
# arr1 = array.array('i', [1,2,2,3,5,8])
# print(arr1.count(2))

# for _ in range(0,6):
# 	print(arr1[_], end = " ")

import re
p = re.compile('\d+')
print(p.findall("rabcdeefgyYhFjkIoomnpOeorteeeeet 11 22222-1256-226-1-0-2"))
