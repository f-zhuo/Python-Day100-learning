
                     函数和模块的使用


```python
"""
输入M和N计算C(m,n)
"""
m=int(input('请输入m值'))
n=int(input('请输入n值'))
if n>m:
    print('n值必须小于m值！')
elif n==m:
    print('C(m,n)=1')
sub=m-n
m_fac=1
for i in range(1,m+1):
    m_fac*=i 
n_fac=1
for j in range(1,n+1):
    n_fac*=j
sub_fac=1
for k in range(1,sub+1):
    sub_fac*=k
print('m!={:},n!={:},(m-n)!={:},C(m,n)=m!/(n!*(m-n)!)={:}'
      .format(m_fac,n_fac,sub_fac,int(m_fac/(n_fac*sub_fac))))
    
```

    请输入m值6
    请输入n值3
    m!=720,n!=6,(m-n)!=6,C(m,n)=m!/(n!*(m-n)!)=20
    


```python
m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1, m + 1):
    fm *= num
fn = 1
for num in range(1, n + 1):
    fn *= num
fmn = 1
for num in range(1, m - n + 1):
    fmn *= num
print(fm // fn // fmn)     #//结果为int，/结果为float
```

    m = 6
    n = 3
    20
    

函数的作用：可调用，避免重复

函数的定义：def func(parameter)
            expression
            return 


```python
def factorial(x):
    s=1
    for i in range(1,x+1):
        s*=i
    return s
m=int(input('请输入m值'))
n=int(input('请输入n值'))
fm=factorial(m)
fn=factorial(n)
fmn=factorial(m-n)
print(fm//fn//fmn)
'''python存在阶乘内置函数factorial()'''
```

    请输入m值6
    请输入n值3
    20
    


```python
def factorial(x):
    s=1
    for i in range(1,x+1):
        s*=i
    return s
m=int(input('请输入m值'))
n=int(input('请输入n值'))
fm=factorial(m)
fn=factorial(n)
fmn=factorial(m-n)
'''bug-indexerror'''
print('m!={:},n!={:},(m-n)!={:},C(m,n)=m!/(n!*(m-n)!)={:}'.format(fm,fn,fmn))
```

    请输入m值6
    请输入n值3
    


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-9-20c700118523> in <module>
          9 fn=factorial(n)
         10 fmn=factorial(m-n)
    ---> 11 print('m!={:},n!={:},(m-n)!={:},C(m,n)=m!/(n!*(m-n)!)={:}'.format(fm,fn,fmn))
    

    IndexError: tuple index out of range



```python
from random import randint
def roll_dice(n=2):
    """
    摇色子
    parameter n: 色子的个数
    return: n颗色子点数之和
    """
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


'''累加器'''
def add(a=0, b=0, c=0):
    return a + b + c

# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
'''没有指定参数，使用默认值a=0,b=0,c=0'''
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))
```

    7
    11
    0
    1
    3
    6
    350
    

函数的参数:位置参数
        可变参数
        关键字参数
        命名关键字参数
1.设置默认值，若调用时参数赋值，则使用赋值参数，否则使用默认值
2.可变参数（*args）和（**）args


```python
def add(*list):
    sum=0
    for item in list:
        sum+=item
    return sum
list1=[1,5,9,10]
print(add(*list1))
list2=[]
print(add(*list2))


def add(**dict):
    sum=0
    for key,value in dict.items():
        sum+=value
    return sum
dict1={'1':2,'5':9,'8':7}
print(add(**dict1))
dict2={}
print(add(**dict2))
```

    25
    0
    18
    0
    

                       用模块管理函数
python无函数重载，同一.py文件中的同名函数，后者会覆盖前者。


```python
def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')

foo()
```

    goodbye, world!
    

解决同名函数覆盖的方法：import 模块，一个.py文件即为一个模块。


```python
import test1
test1.test()
import test2
test2.test()


from test1 import test
test()
from test2 import test
test()


from test1 import test
from test2 import test
test()
test()
```

    hello world
    goodbye world
    hello world
    goodbye world
    goodbye world
    goodbye world
    

引入了新的问题：该模块的函数只需调用一部分，不需执行全部。
解决办法：用if条件，__name__=='__main__'才执行代码


```python
import test1
test1.test()
import test2
test2.test()

```

    hello world
    goodbye world
    hello world
    goodbye world
    


```python
'''__name__='__main__'bug'''
import test1
test1.test()
import test2
test2.test()
```

    hello world
    goodbye world
    


```python
'''实现计算求最大公约数和最小公倍数的函数。'''
def factor1(x,y):
    if x > y:
        x, y = y, x
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def factor2(x,y):
    return x * y //factor1(x, y)

```


```python
'''实现判断一个数是不是回文数的函数'''
def is_palindrome(num): 
    temp = num
    num2 = 0
    while temp > 0:
        num2 *= 10
        num2 += temp % 10
        temp //= 10
    if num == num2:
        return True
    else:
        return False

```


```python
'''实现判断一个数是不是素数的函数'''
def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True if num != 1 else False
        
```


```python
'''写一个程序判断输入的正整数是不是回文素数'''
def is_prime_palindrome(num):
    temp = num
    num2 = 0
    while temp > 0:
        num2 *= 10
        num2 += temp % 10
        temp //= 10
    if num == num2:
        for x in range(2, num):
            if num % x == 0:
                return False
        return True if num != 1 else False
    else:
        return False
```


```python
if __name__=='__main__':
    if is_palindrome(num) and is_prime(num):
        return True
    else:
        return False
```

函数作用域：局部作用域，嵌套作用域，全局作用域，内置作用域
函数的全局变量与局部变量不相关，不能互相访问。调用函数，局部变量只在函数内部起作用，不能影响全局结果。
local:定义全局变量
nonlocal：定义嵌套作用域的变量          

python中函数的规范写法：
def main():
    coding
    pass
if__name__=='__main()__':
    main()


```python
'''常用内置函数'''
def myfilter(mystr):
    return len(mystr) == 6
print(chr(0x9a86))
print(hex(ord('骆')))
print(abs(-1.2345))
print(round(-1.2345))
print(pow(1.2345, 5))
fruits = ['orange', 'peach', 'durian', 'watermelon']
print(fruits[slice(1,3)])
fruits2 = filter(myfilter, fruits)
print(fruits)
print(fruits2)
for items in fruits2:
    print(items)
```

    骆
    0x9a86
    1.2345
    -1
    2.8671833852463537
    ['peach', 'durian']
    ['orange', 'peach', 'durian', 'watermelon']
    <filter object at 0x000001B95997FAC8>
    orange
    durian
    


```python
'''常用模块
Python常用模块
- 运行时服务相关模块: copy / pickle / sys / ...
- 数学相关模块: decimal / math / random / ...
- 字符串处理模块: codecs / re / ...
- 文件处理相关模块: shutil / gzip / ...
- 操作系统服务相关模块: datetime / os / time / logging / io / ...
- 进程和线程相关模块: multiprocessing / threading / queue
- 网络应用相关模块: ftplib / http / smtplib / urllib / ...
- Web编程相关模块: cgi / webbrowser
- 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...'''
import time
import shutil
import os

seconds = time.time()
print(seconds)
localtime = time.localtime(seconds)
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
asctime = time.asctime(localtime)
print(asctime)
strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
print(strtime)
mydate = time.strptime('2018-1-1', '%Y-%m-%d')
print(mydate)

shutil.copy('/Users/chris/test1.py', '/Users/chris/test2.py')
os.system('ls -l')
os.chdir('/Users/chris')
os.system('ls -l')
os.mkdir('test')
```

    1557942446.25141
    time.struct_time(tm_year=2019, tm_mon=5, tm_mday=16, tm_hour=1, tm_min=47, tm_sec=26, tm_wday=3, tm_yday=136, tm_isdst=0)
    2019
    5
    16
    Thu May 16 01:47:26 2019
    2019-05-16 01:47:26
    time.struct_time(tm_year=2018, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
    


```python
def f1(a, b=5, c=10):
    return a + b * 2 + c * 3
print(f1(1, 2, 3))
print(f1(100, 200))
print(f1(100))
print(f1(c=2, b=3, a=1))

def f2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum
print(f2(1, 2, 3))
print(f2(1, 2, 3, 4, 5))
print(f2())

def f3(**kw):
    if 'name' in kw:
        print('欢迎你%s!' % kw['name'])
    elif 'tel' in kw:
        print('你的联系电话是: %s!' % kw['tel'])
    else:
        print('没找到你的个人信息!')


param = {'name': '骆昊', 'age': 38}
f3(**param)
f3(name='骆昊', age=38, tel='13866778899')
f3(user='骆昊', age=38, tel='13866778899')
f3(user='骆昊', age=38, mobile='13866778899')
```

    14
    530
    140
    13
    6
    15
    0
    欢迎你骆昊!
    欢迎你骆昊!
    你的联系电话是: 13866778899!
    没找到你的个人信息!
    


```python
"""
作用域问题
"""
# 局部作用域
def foo1():
    a = 5

foo1()
# print(a)  # NameError

# 全局作用域
b = 10
def foo2():
    print(b)
foo2()

def foo3():
    b = 100     # 局部变量
    print(b)
foo3()
print(b)

def foo4():
    global b
    b = 200     # 全局变量
    print(b)
foo4()
print(b)
```

    10
    100
    10
    200
    200
    


```python

```
