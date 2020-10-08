# -*- encoding: utf-8 -*-
# @Time   : 2020/9/21 19:06
# @Author : Peter young
# @File   : 1.py

# def Join(List, sep=None):
#     return (sep or ',').join(List)
# print(Join(['a','b','c']))
# print(Join(['a','b','c'],':'))

class Test(object):
    def __init__(self,a=''):
        self.a = a
    def __getattr__(self, a):
        return Test('{0}/{1}'.format(self.a,a))
    def __str__(self):
        return self.a
obj = Test()
print(str(obj.a123.b456.c789))