# -*- coding: utf-8 -*-
"""
Created on Sat May 11 00:11:42 2019

@author: chris
"""
# random 模块的四种函数
import random
print(random.random()) #产生一个[0,1)的随机数
print(random.randint(1,99)) #生成一个[a,b]的整数
print(random.randrange(1,100,2))#在以1开始，100结束（不包括100），步长为2的数组中挑选一个随机数
print(random.Random())   #生成类的实例，输出结果：<random.Random object at 0x0000018D8FAAB588>
print(random.Random().random()) # 等同于random.random()