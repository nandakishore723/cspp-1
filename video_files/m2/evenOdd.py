# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:03:23 2016

@author: ericgrimson
"""

# x = int(input('Enter an integer: '))
# if x%2 == 0:
#     print('')
#     print('Even')
# else:
#     print('')
#     print('Odd')
# print('Done with conditional')

# print("hai", end = "@")
# print('olo')

# x = "str"
# print(x)

# i = 10.001
# type(i)

List = []
#print(List)
List.append(1)
List.append(5)
List.append(123.22)
#List.append('me')
List2 = [1, 2]
List.append(List2)
List.insert(2, 8)
List2.insert(2, 8)
#List.pop()
List.remove(8)
print(List)
List.extend([100])
print(List)
List.reverse()
print(List)
Set = set(["me" , "u"])
print(Set)
Dict = {}
Dict['name'] = 'ab, bc, cd'
Dict['val'] =  2, 3, 4
print(Dict.keys())
print(Dict)
print(100%100)
x = 5
y = 10
x, y = y, x
print(x, y)