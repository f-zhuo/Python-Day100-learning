
**文件和异常**

|操作模式|具体含义|
|-|-|
|‘r’|    读取（默认）     |
|‘w’| 写入（覆盖之前的内容）|
|‘x’|写入，文件存在则显示异常|
|‘a’| 添加，内容写入文件末尾|
|‘b’|     二进制       |
|‘t’|   文本模式（默认）   |
|‘+’|    更新（可读写）    |



**读写文本文件**:
open函数指定好带路径的文件名（可以使用相对路径或绝对路径）并将文件模式设置为'r'（如果不指定，默认值也是'r'），然后通过encoding参数指定编码（如果不指定，默认值是None，那么在读取文件时使用的是操作系统默认的编码）


```python
'''finally'''
def main():
    f = open('致橡树.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()

if __name__ == '__main__':
    main()
    
    
def main():
    f = None
    try:
        f = open('致橡树.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    main()
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-2-4ad3b62b324f> in <module>
          5 
          6 if __name__ == '__main__':
    ----> 7     main()
          8 
          9 
    

    <ipython-input-2-4ad3b62b324f> in main()
          1 def main():
    ----> 2     f = open('致橡树.txt', 'r', encoding='utf-8')
          3     print(f.read())
          4     f.close()
          5 
    

    FileNotFoundError: [Errno 2] No such file or directory: '致橡树.txt'



```python
'''with'''
def main():
    try:
        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')

if __name__ == '__main__':
    main()
```

    无法打开指定的文件!
    


```python
'''用for-in循环逐行读取或者用readlines方法将文件按行读取到一个列表容器中'''
import time
def main():
    # 一次性读取整个文件内容
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('致橡树.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('致橡树.txt') as f:
        lines = f.readlines()
    print(lines)  

if __name__ == '__main__':
    main()
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-4-124f3244031d> in <module>
         19 
         20 if __name__ == '__main__':
    ---> 21     main()
    

    <ipython-input-4-124f3244031d> in main()
          3 def main():
          4     # 一次性读取整个文件内容
    ----> 5     with open('致橡树.txt', 'r', encoding='utf-8') as f:
          6         print(f.read())
          7 
    

    FileNotFoundError: [Errno 2] No such file or directory: '致橡树.txt'



```python
from math import sqrt
def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False

def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成!')

if __name__ == '__main__':
    main()
```

    操作完成!
    

**读写二进制文件**



```python
def main():
    try:
        with open('guido.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('吉多.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束.')


if __name__ == '__main__':
    main()
```

    指定的文件无法打开.
    程序执行结束.
    

**读写JSON文件**:JavaScript Object Notation(纯文本)


```python
{
    'name': '骆昊',
    'age': 38,
    'qq': 957658,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BYD', 'max_speed': 180},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 320}
    ]
}
```




    {'name': '骆昊',
     'age': 38,
     'qq': 957658,
     'friends': ['王大锤', '白元芳'],
     'cars': [{'brand': 'BYD', 'max_speed': 180},
      {'brand': 'Audi', 'max_speed': 280},
      {'brand': 'Benz', 'max_speed': 320}]}



ISON与python的对应关系

|ISON    |python|
|- |-|
|object   |dict |
|array   |list  |
|string   |str  |
|int/real|int/float|
|true/false|True/False|
|null     |None  |



```python
import json
def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')

if __name__ == '__main__':
    main()
```

    保存数据完成!
    

**json模块主要有四个比较重要的函数，分别是：**

dump - 将Python对象按照JSON格式序列化到文件中

dumps - 将Python对象处理成JSON格式的字符串

load - 将文件中的JSON数据反序列化成对象

loads - 将字符串的内容反序列化成Python对象

**序列化（serialization）：**

在计算机科学的数据处理中，是指将数据结构或对象状态转换为可以存储或传输的形式，这样在需要的时候能够恢复到原先的状态，而且通过序列化的数据重新获取字节时，可以利用这些字节来产生原始对象的副本（拷贝）

**反序列化（deserialization）：**

从一系列字节中提取数据结构的操作


```python
import requests
import json

def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])

if __name__ == '__main__':
    main()
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-16-3bafae503abb> in <module>
          9 
         10 if __name__ == '__main__':
    ---> 11     main()
    

    <ipython-input-16-3bafae503abb> in main()
          5     resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
          6     data_model = json.loads(resp.text)
    ----> 7     for news in data_model['newslist']:
          8         print(news['title'])
          9 
    

    KeyError: 'newslist'



```python
"""
读取CSV文件
"""
import csv
filename = 'example.csv'
try:
    with open(filename) as f:
        reader = csv.reader(f)
        data = list(reader)
except FileNotFoundError:
    print('无法打开文件:', filename)
else:
    for item in data:
        print('%-30s%-20s%-10s' % (item[0], item[1], item[2]))
```

    无法打开文件: example.csv
    


```python
"""
写入CSV文件
"""
import csv

class Teacher(object):

    def __init__(self, name, age, title):
        self.__name = name
        self.__age = age
        self.__title = title
        self.__index = -1

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def title(self):
        return self.__title

filename = 'teacher.csv'
teachers = [Teacher('骆昊', 38, '叫兽'), Teacher('狄仁杰', 25, '砖家')]

try:
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for teacher in teachers:
            writer.writerow([teacher.name, teacher.age, teacher.title])
except BaseException as e:
    print('无法写入文件:', filename)
else:
    print('保存数据完成!')
```

    保存数据完成!
    


```python
"""
异常机制 - 处理程序在运行时可能发生的状态
"""
input_again = True
while input_again:
    try:
        a = int(input('a = '))
        b = int(input('b = '))
        print('%d / %d = %f' % (a, b, a / b))
        input_again = False
    except ValueError:
        print('请输入整数')
    except ZeroDivisionError:
        print('除数不能为0')
```

    a = 2.3
    请输入整数
    a = 3
    b = 0
    除数不能为0
    a = 3
    b = 2
    3 / 2 = 1.500000
    


```python
"""
异常机制 - 处理程序在运行时可能发生的状态
"""
input_again = True
while input_again:
    try:
        a = int(input('a = '))
        b = int(input('b = '))
        print('%d / %d = %f' % (a, b, a / b))
        input_again = False
    except (ValueError, ZeroDivisionError) as msg:
        print(msg)
```

    a = 5
    b = 0
    division by zero
    a = 5.3
    invalid literal for int() with base 10: '5.3'
    a = 2
    b = 3
    2 / 3 = 0.666667
    


```python
"""
异常机制 - 处理程序在运行时可能发生的状态
"""
import time
import sys

filename = input('请输入文件名: ')
try:
    with open(filename) as f:
        lines = f.readlines()
except FileNotFoundError as msg:
    print('无法打开文件:', filename)
    print(msg)
except UnicodeDecodeError as msg:
    print('非文本文件无法解码')
    sys.exit()
else:
    for line in lines:
        print(line.rstrip())
        time.sleep(0.5)
finally:
    # 此处最适合做善后工作
    print('不管发生什么我都会执行')
```

    请输入文件名: 2333.p
    无法打开文件: 2333.p
    [Errno 2] No such file or directory: '2333.p'
    不管发生什么我都会执行
    


```python
"""
引发异常和异常栈
"""
def f1():
    raise AssertionError('发生异常')

def f2():
    f1()

def f3():
    f2()

f3()
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-22-e9b39a006e1a> in <module>
         11     f2()
         12 
    ---> 13 f3()
    

    <ipython-input-22-e9b39a006e1a> in f3()
          9 
         10 def f3():
    ---> 11     f2()
         12 
         13 f3()
    

    <ipython-input-22-e9b39a006e1a> in f2()
          6 
          7 def f2():
    ----> 8     f1()
          9 
         10 def f3():
    

    <ipython-input-22-e9b39a006e1a> in f1()
          3 """
          4 def f1():
    ----> 5     raise AssertionError('发生异常')
          6 
          7 def f2():
    

    AssertionError: 发生异常



```python
"""
读取圆周率文件判断其中是否包含自己的生日
"""
birth = input('请输入你的生日: ')
with open('pi_million_digits.txt') as f:
    lines = f.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    if birth in pi_string:
        print('Bingo!!!')
```

    请输入你的生日: 20500101
    


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-24-88dd1c0f9fc6> in <module>
          3 """
          4 birth = input('请输入你的生日: ')
    ----> 5 with open('pi_million_digits.txt') as f:
          6     lines = f.readlines()
          7     pi_string = ''
    

    FileNotFoundError: [Errno 2] No such file or directory: 'pi_million_digits.txt'



```python
"""
写文本文件
将100以内的素数写入到文件中
"""
from math import sqrt

def is_prime(n):
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True

# 试一试有什么不一样
# with open('prime.txt', 'a') as f:
with open('prime.txt', 'w') as f:
    for num in range(2, 100):
        if is_prime(num):
            f.write(str(num) + '\n')
print('写入完成!')
```

    写入完成!
    


```python
"""
读写二进制文件
"""
import base64
with open('mm.jpg', 'rb') as f:
    data = f.read()
    # print(type(data))
    # print(data)
    print('字节数:', len(data))
    # 将图片处理成BASE-64编码
    print(base64.b64encode(data))
with open('girl.jpg', 'wb') as f:
    f.write(data)
print('写入完成!')
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-27-b378b1901f50> in <module>
          3 """
          4 import base64
    ----> 5 with open('mm.jpg', 'rb') as f:
          6     data = f.read()
          7     # print(type(data))
    

    FileNotFoundError: [Errno 2] No such file or directory: 'mm.jpg'



```python
"""
读取JSON数据

"""
import json
import csv2
json_str = '{"name": "骆昊", "age": 38, "title": "叫兽"}'
result = json.loads(json_str)
print(result)
print(type(result))
print(result['name'])
print(result['age'])

# 把转换得到的字典作为关键字参数传入Teacher的构造器
teacher = csv2.Teacher(**result)
print(teacher)
print(teacher.name)
print(teacher.age)
print(teacher.title)

{
     "wendu": "29",
     "ganmao": "各项气象条件适宜，发生感冒机率较低。但请避免长期处于空调房间中，以防感冒。",
      "forecast": [
        {
            "fengxiang": "南风",
            "fengli": "3-4级",
            "high": "高温 32℃",
            "type": "多云",
            "low": "低温 17℃",
            "date": "16日星期二"
        },
        {
            "fengxiang": "南风",
            "fengli": "微风级",
            "high": "高温 34℃",
            "type": "晴",
            "low": "低温 19℃",
            "date": "17日星期三"
        },
        {
            "fengxiang": "南风",
            "fengli": "微风级",
            "high": "高温 35℃",
            "type": "晴",
            "low": "低温 22℃",
            "date": "18日星期四"
        },
        {
            "fengxiang": "南风",
            "fengli": "微风级",
            "high": "高温 35℃",
            "type": "多云",
            "low": "低温 22℃",
            "date": "19日星期五"
        },
        {
            "fengxiang": "南风",
            "fengli": "3-4级",
            "high": "高温 34℃",
            "type": "晴",
            "low": "低温 21℃",
            "date": "20日星期六"
        }
    ],
    "yesterday": {
        "fl": "微风",
        "fx": "南风",
        "high": "高温 28℃",
        "type": "晴",
        "low": "低温 15℃",
        "date": "15日星期一"
    },
    "aqi": "72",
    "city": "北京"
}

```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-29-16cd780d6882> in <module>
          4 """
          5 import json
    ----> 6 import csv2
          7 json_str = '{"name": "骆昊", "age": 38, "title": "叫兽"}'
          8 result = json.loads(json_str)
    

    ModuleNotFoundError: No module named 'csv2'



```python
"""
写入JSON文件

"""
import json

teacher_dict = {'name': '白元芳', 'age': 25, 'title': '讲师'}
json_str = json.dumps(teacher_dict)
print(json_str)
print(type(json_str))
fruits_list = ['apple', 'orange', 'strawberry', 'banana', 'pitaya']
json_str = json.dumps(fruits_list)
print(json_str)
print(type(json_str))
```

    {"name": "\u767d\u5143\u82b3", "age": 25, "title": "\u8bb2\u5e08"}
    <class 'str'>
    ["apple", "orange", "strawberry", "banana", "pitaya"]
    <class 'str'>
    
