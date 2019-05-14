# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:45:47 2019

@author: chris
"""

'''英制英寸与公制厘米的互换'''
unit=input('您输入的长度单位是（英寸或厘米）：')
if unit!='英寸' and unit!='厘米':
    print('请输入有效的单位')
else:
    value=float(input('请输入长度：'))
    if unit=='英寸':
        change_value=2.54*value
        print('{:.2f}英寸={:.2f}厘米'.format(value,change_value))
    else :
        change_value=value/2.54
        print('{:.2f}厘米={:.2f}英寸'.format(value,change_value))
        

'''掷骰子决定真心话和大冒险'''
'''引入模块及函数的另一种表示方法：
   from random import randint
   randint(a,b) 产生的随机数为[a,b]
   randrange(a,b) 产生的随机数为[a,b)
    '''
import random
rand_number=random.randrange(1,7)
if rand_number==1:
    case='真心话：初恋是什么时候？'
elif rand_number==2:
    case='真心话：对在场的哪一个异性最有好感？'
elif rand_number==3:
    case='真心话：对女/男朋友说过的最肉麻的话是什么？'
elif rand_number==4:
    case='大冒险：去敲邻居的门，对他/她说：“我喜欢你很久了。”'
elif rand_number==5:
    case='大冒险：任选现场一位同性，用嘴传递小酒杯。'
elif rand_number==6:
    case='大冒险：打电话给父母/朋友：“我/我女票怀孕了，但我不知道孩子的父亲是谁。”'
print('掷得的骰子数是：{:}'.format(rand_number),case)


'''
百分制成绩转等级制成绩
90分以上    --> A
80分~89分   --> B
70分~79分	--> C
60分~69分   --> D
60分以下    --> E
'''
score=float(input('请输入考试成绩：'))
if score>=90:
    print('得分为：A')
elif score>=80:
    print('得分为：B')
elif score>=70:
    print('得分为：C')
elif score>=60:
    print('得分为：D')
else:
    print('得分为：E')
    
    
"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积
"""
edge1=float(input('请输入三角形的边长1：'))
edge2=float(input('请输入三角形的边长2：'))
edge3=float(input('请输入三角形的边长3：'))
from math import sqrt
if edge1+edge2>edge3 and edge1+edge3>edge2 and edge3+edge2>edge1:
        print('三角形的周长为：',edge1+edge2+edge3)
        print('三角形的面积为：',sqrt(1/16*(edge1+edge2+edge3)*(edge1+edge2-edge3)
        *(edge1-edge2+edge3)*(-edge1+edge2+edge3)))
else:
    print('不能构成三角形')
    
    
"""
输入月收入和五险一金计算个人所得税
"""
salary=float(input('请输入您的月收入：'))
insurance=float(input('请输入您的五险一金：'))
diff = salary - insurance - 5000
if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 1500:
    rate = 0.03
    deduction = 0
elif diff < 4500:
    rate = 0.1
    deduction = 105
elif diff < 9000:
    rate = 0.2
    deduction = 555
elif diff < 35000:
    rate = 0.25
    deduction = 1005
elif diff < 55000:
    rate = 0.3
    deduction = 2755
elif diff < 80000:
    rate = 0.35
    deduction = 5505
else:
    rate = 0.45
    deduction = 13505
tax = abs(diff * rate - deduction)
print('个人所得税: ￥{:.2f}元'.format(tax))
print('实际到手收入: ￥{:.2f}元'.format(diff + 5000 - tax))