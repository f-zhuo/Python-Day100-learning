# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:05:52 2019

@author: chris
"""

'''case1'''
''' 如果输入口令时,终端没有回显,可以使用getpass模块的getpass函数'''
import getpass
''' Warning: QtConsole does not support password mode, the text you type will be visible
    这是spyder自身平台的原因'''
username=getpass.getpass('请输入用户名:')
password=getpass.getpass('请输入口令:')  
if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')
    
'''case2
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
'''
x=float(input('请输入x的值：'))
if x>1:
    f=3*x-5
elif -1<=x<=1:  # 可简化为：-1<=x,因x必然小于等于1
    f=x+2
else:
    f=5*x+3
print('函数的值为：{:.3f}'.format(f))

x=float(input('请输入x的值：'))
if x>1:
    f=3*x-5
else:
    if -1<=x:  # 可简化为：-1<=x,因x必然小于等于1
        f=x+2
    else:
        f=5*x+3
print('f({:.3f})={:.3f}'.format(x,f))