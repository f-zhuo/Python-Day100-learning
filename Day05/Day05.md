

```python
'''寻找水仙花数'''
for n in range(100,1000):
    ones_digit = n % 10
    tens_digit = (n % 100)// 10
    hundreds_digit = n // 100
    if n==ones_digit**3+tens_digit**3+hundreds_digit**3:
        print("{:}为水仙花数！".format(n))
```

    153为水仙花数！
    370为水仙花数！
    371为水仙花数！
    407为水仙花数！
    


```python
'''寻找完美数'''
'''导入时间模块'''
import time
start=time.clock()
for i in range(1,10000):
     k=0
     for j in range(1,i):
        if i % j == 0:
            k += j
     if k == i:
        print('{:}是完美数！'.format(i))
end=time.clock()
lasting_time=end-start
print("开始时间为{:}秒，结束时间为{:}秒，计算时间为{:}秒".format(start,end,lasting_time))
```

    D:\Anaconda\lib\site-packages\ipykernel_launcher.py:3: DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: use time.perf_counter or time.process_time instead
      This is separate from the ipykernel package so we can avoid doing imports until
    

    6是完美数！
    28是完美数！
    496是完美数！
    8128是完美数！
    开始时间为8732.187389461秒，结束时间为8740.419949455秒，计算时间为8.23255999399953秒
    

    D:\Anaconda\lib\site-packages\ipykernel_launcher.py:11: DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: use time.perf_counter or time.process_time instead
      # This is added back by InteractiveShellApp.init_path()
    


```python
'''百钱百鸡'''
for a in range(0,20):
    for b in range(0,33):
        for c in range(0,100):
            if a + b + c ==100 and a * 5 + b * 3 + c / 3 ==100:
                print('一百钱可买{:}只鸡翁，{:}只母鸡，{:}只雏鸡。'.format(a,b,c))
        
```

    一百钱可买0只鸡翁，25只母鸡，75只雏鸡。
    一百钱可买4只鸡翁，18只母鸡，78只雏鸡。
    一百钱可买8只鸡翁，11只母鸡，81只雏鸡。
    一百钱可买12只鸡翁，4只母鸡，84只雏鸡。
    


```python
'''斐波那契数列'''
n_pre=0
n_aft=1
for i in range(20):
    print(n_aft,end=" ")
    n_pre,n_aft=n_aft,n_pre+n_aft    
```

    1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 


```python
'''骰子赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次摇色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
'''
import random
money=1000
number1=random.randint(2,12)
while True:
    dum=int(input('请输入下注数：'))
    if dum > money:
        print('您的下注必须小于等于总资产！请重新下注！')
    else:
        break
if 7==number1 or 11==number1:
    money+=dum
    print('第1次摇出{:}，玩家胜，玩家现有资产为{:}'.format(number1,money))
elif number1==2 or number1==3 or number1==12:
    money-=dum
    print('第1次摇出{:}，庄家胜，玩家现有资产为{:}'.format(number1,money))
else:
    print('第1次摇出{:}，游戏继续，玩家现有资产为{:}'.format(number1,money))
number=number1
count=1
while money>0:  
    number2=random.randint(2,13)
    count+=1
    while True:
        dum=int(input('请输入下注数：'))
        if dum > money:
            print('您的下注必须小于等于总资产！请重新下注！')
        else:
            break
    if number2==7:
        money-=dum
        print('第{:}次摇出{:}，庄家胜，玩家现有资产为{:}'.format(count,number2,money))
    elif number==number2:
        money+=dum
        print('第{:}次摇出{:}，玩家胜，玩家现有资产为{:}'.format(count,number2,money))
    else:
        print('第{:}次摇出{:}，游戏继续，玩家现有资产为{:}'.format(count,number2,money))
    number=number2
print('您已参与{:}次游戏，资产不足，游戏结束'.format(count))
```

    请输入下注数：200
    第1次摇出6，游戏继续，玩家现有资产为1000
    请输入下注数：300
    第2次摇出6，玩家胜，玩家现有资产为1300
    请输入下注数：2000
    您的下注必须小于等于总资产！
    请输入下注数：1000
    第3次摇出9，游戏继续，玩家现有资产为1300
    请输入下注数：300
    第4次摇出5，游戏继续，玩家现有资产为1300
    请输入下注数：500
    第5次摇出8，游戏继续，玩家现有资产为1300
    请输入下注数：1300
    第6次摇出11，游戏继续，玩家现有资产为1300
    请输入下注数：200
    第7次摇出11，玩家胜，玩家现有资产为1500
    请输入下注数：300
    第8次摇出12，游戏继续，玩家现有资产为1500
    请输入下注数：500
    第9次摇出12，玩家胜，玩家现有资产为2000
    请输入下注数：1000
    第10次摇出3，游戏继续，玩家现有资产为2000
    请输入下注数：1000
    第11次摇出11，游戏继续，玩家现有资产为2000
    请输入下注数：1000
    第12次摇出3，游戏继续，玩家现有资产为2000
    请输入下注数：1000
    第13次摇出5，游戏继续，玩家现有资产为2000
    请输入下注数：1000
    第14次摇出13，游戏继续，玩家现有资产为2000
    请输入下注数：1000
    第15次摇出10，游戏继续，玩家现有资产为2000
    请输入下注数：1000
    第16次摇出12，游戏继续，玩家现有资产为2000
    请输入下注数：2000
    第17次摇出4，游戏继续，玩家现有资产为2000
    请输入下注数：2000
    第18次摇出13，游戏继续，玩家现有资产为2000
    请输入下注数：2000
    第19次摇出2，游戏继续，玩家现有资产为2000
    请输入下注数：2000
    第20次摇出13，游戏继续，玩家现有资产为2000
    请输入下注数：2000
    第21次摇出7，庄家胜，玩家现有资产为0
    您已参与21次游戏，资产不足，游戏结束
    


```python
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
```

    公鸡: 0只, 母鸡: 25只, 小鸡: 75只
    公鸡: 4只, 母鸡: 18只, 小鸡: 78只
    公鸡: 8只, 母鸡: 11只, 小鸡: 81只
    公鸡: 12只, 母鸡: 4只, 小鸡: 84只
    


```python
from random import randint

money = 1000
while money > 0:
    print('你的总资产为:', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注: '))
        if debt > 0 and debt <= money:
            break
        else:
            print('您的下注必须小于等于总资产！请重新下注！')
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True

    while needs_go_on:
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
            needs_go_on = False
        elif current == first:
            print('玩家胜')
            money += debt
            needs_go_on = False

print('你破产了, 游戏结束!')
```


```python
a =  0
b =  1
for _ in  range(20):
    (a,b)=(b,a + b)
    print(a,end = '  ')
```

    1  1  2  3  5  8  13  21  34  55  89  144  233  377  610  987  1597  2584  4181  6765  


```python
'''
判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数'''
n=input('请输入一个正整数：')
l=int(len(n))
if l % 2==0:
    for i in range(l//2):
        if n[i]!=n[l-1-i]:
            print('{:}不是回文数'.format(n))
            break
        elif n[l//2-1]==n[l//2]:
            print('{:}是回文数'.format(n))
        '''bug重复输入'''
else:
    for i in range((l-1)//2):
        if n[i]!=n[l-1-i]:
            print('{:}不是回文数!'.format(n))
            break
        elif n[(l-1)//2-1]==n[l-(l-1)//2]:
            print('{:}是回文数!'.format(n))
```

    请输入一个正整数：123454321
    123454321是回文数!
    123454321是回文数!
    123454321是回文数!
    123454321是回文数!
    


```python
num = int(input('请输入一个正整数: '))
temp = num
num2 = 0
while temp > 0:
    num2 *= 10
    num2 += temp % 10
    temp //= 10
if num == num2:
    print('%d是回文数' % num)
else:
    print('%d不是回文数' % num)

```

    请输入一个正整数: 1123211
    1123211是回文数
    


```python
import time
import math

start = time.clock()
for num in range(1, 10000):
    sum = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            sum += factor
            if factor > 1 and num / factor != factor:
                sum += num / factor
    if sum == num:
        print(num)
end = time.clock()
print("执行时间:", (end - start), "秒")
```

    1
    6
    28
    496
    8128
    执行时间: 0.11500333299954946 秒
    

    D:\Anaconda\lib\site-packages\ipykernel_launcher.py:4: DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: use time.perf_counter or time.process_time instead
      after removing the cwd from sys.path.
    D:\Anaconda\lib\site-packages\ipykernel_launcher.py:14: DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: use time.perf_counter or time.process_time instead
      
    


```python

```
