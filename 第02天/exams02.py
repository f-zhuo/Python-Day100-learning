# -*- coding: utf-8 -*-
"""
Created on Sun May 12 00:08:16 2019

@author: chris
"""

'''华氏温度与摄氏温度的转换'''
F=input("请输入当前温度（华氏温度）：")
c=(float(F)-32)/1.8    # 输入值为字符串类型，应转换为数值型
print("当前温度是：{:.2f}摄氏度".format(c))


'''输入圆半径求周长及面积'''
r=float(input("请输入圆的半径："))
import math
l=2*math.pi*r
s=math.pi*(r**2)
print('圆的周长为：%.2f,圆的面积为：%.2f'%(l,s))


'''判断年份是否为闰年'''

'''方法一：if-else'''

year=int(input("请输入年份："))
if year%4==0 and year%100!=0 or year%400==0:
    print('%d 年是闰年'%year)
else:
    print('%d 年不是闰年'%year)

'''方法二：系统自带calendar模块'''
year=int(input("请输入年份："))    
import calendar
print(calendar.isleap(year))

'''方法三：系统自带isleap函数与f-else结合'''
year=int(input("请输入年份："))    
isleap=(year%4==0 and year%100!=0 or year%400==0)
print(isleap)    

'''字符串的常用操作'''
str1 = 'hello, world!'
print('字符串的长度是:', len(str1))
print('单词首字母大写: ', str1.title())
print('字符串变大写: ', str1.upper())
print('字符串是不是大写: ', str1.isupper())
print('字符串是不是以hello开头: ', str1.startswith('hello'))
print('字符串是不是以hello结尾: ', str1.endswith('hello'))
print('字符串是不是以感叹号开头: ', str1.startswith('!'))
print('字符串是不是一感叹号结尾: ', str1.endswith('!'))
str2='-\u8a86\u760a'
str3 = str1.title() + ' ' + str2.lower()
print(str3)