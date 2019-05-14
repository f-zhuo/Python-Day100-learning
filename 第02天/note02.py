# -*- coding: utf-8 -*-
"""
Created on Sat May 11 21:31:50 2019

@author: chris
"""
'''算术运算'''
a=321
b=123
print(a+b)   #a+b
print(a-b)   #a-b
print(a*b)   #a*b
print(a/b)   #a/b
print(a//b)  #a整除b
print(a%b)   #a除以b的余数
print(a**b)  #a的b次方

'''input函数输入
  int()进行类型转换
占位符格式化输出的字符串/format格式化字符串'''
a=int(input('a='))
b=int(input('b='))
print('%d + %d=%d'%(a,b,a+b))
print('%d - %d=%d'%(a,b,a-b))
print('%d * %d=%d'%(a,b,a*b))
print('%d / %d=%.2f'%(a,b,a/b)) #整数除以整数可能为小数，默认小数部分6位，故类型设为%.2f。
print('%d // %d=%d'%(a,b,a//b))
print('%d %% %d=%d'%(a,b,a%b))
print('%d ** %d=%d'%(a,b,a**b))

print('{:d}+{:d}={:d}'.format(a,b,a+b))
print('{:d}-{:d}={:d}'.format(a,b,a-b))
print('{:d}*{:d}={:d}'.format(a,b,a*b))
print('{:d}/{:d}={:.2f}'.format(a,b,a/b))
print('{:d}//{:d}={:d}'.format(a,b,a//b))
print('{:d}**{:d}={:d}'.format(a,b,a**b))

'''type()检查变量类型'''
a=1
b=1.2
c='1'
d=1+1j            #表示复数时虚部前必须有数字，不可只有j。
e=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

'''运算符及优先级'''
a = 5
b = 10
c = 3
d = 4
e = 5
a += b
a -= c
a *= d
a /= e
print("a = ", a)   # a为9.6

flag1 = 3 > 2      #flag1=True
flag2 = 2 < 1      #flag2=False
flag3 = flag1 and flag2 #flag3=False
flag4 = flag1 or flag2  #flag4=True
flag5 = not flag1       #flag5=False
print("flag1 = ", flag1) 
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)    #括号内无引号，输出判断结果
print(flag2 is not False)