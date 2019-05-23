
**使用正则表达式**

《正则表达式30分钟入门教程》:https://deerchao.net/tutorials/regex/regex.htm
![title](1.png)
![title](2.png)
![title](3.png)
![title](4.png)


```python
"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12位的数字且首位不能为0
"""
import re

def main():
    username = input('请输入用户名: ')
    qq = input('请输入QQ号: ')
    # match函数的第一个参数是正则表达式字符串或正则表达式对象
    # 第二个参数是要跟正则表达式做匹配的字符串对象
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    # m1=re.match(r'^\b\w{6,20}\b$',username)
    if not m1:
        print('请输入有效的用户名.')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效的QQ号.')
    if m1 and m2:
        print('你输入的信息是有效的!')

if __name__ == '__main__':
    main()
```

    请输入用户名: 156231
    请输入QQ号: 8956231
    你输入的信息是有效的!
    

**从一段文字中提取出国内手机号码**
![title](tel-start-number.png)


```python
import re
def main():
    # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
    pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    # 查找所有匹配并保存到一个列表中
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------华丽的分隔线--------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    for temp in pattern.finditer(sentence):
        print(temp)
        print(temp.group())
    print('--------华丽的分隔线--------')
    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m)
        print(m.group())
        m = pattern.search(sentence, m.end())

if __name__ == '__main__':
    main()
```

    ['13512346789', '15600998765', '15600998765']
    --------华丽的分隔线--------
    <re.Match object; span=(32, 43), match='13512346789'>
    13512346789
    <re.Match object; span=(55, 66), match='15600998765'>
    15600998765
    <re.Match object; span=(86, 97), match='15600998765'>
    15600998765
    --------华丽的分隔线--------
    <re.Match object; span=(32, 43), match='13512346789'>
    13512346789
    <re.Match object; span=(55, 66), match='15600998765'>
    15600998765
    <re.Match object; span=(86, 97), match='15600998765'>
    15600998765
    


```python
'''替换字符串中的不良内容'''
import re
def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)  # 你丫是*吗? 我*你大爷的. * you.

if __name__ == '__main__':
    main()
'''e模块的正则表达式相关函数中都有一个flags参数，它代表了正则表达式的匹配标记，
可以通过该标记来指定匹配时是否忽略大小写、是否进行多行匹配、是否显示调试信息等。
如果需要为flags参数指定多个值，可以使用按位或运算符进行叠加，如flags=re.I | re.M。'''
```

    你丫是*吗? 我*你大爷的. * you.
    


```python
'''拆分长字符串'''
import re
def main():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)  

if __name__ == '__main__':
    main()
```

    ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']
    


```python
import re
def main():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    print(sentence_list)  

if __name__ == '__main__':
    main()
```

    ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡', '']
    


```python
"""
字符串常用操作
"""
import pyperclip
# 转义字符
print('My brother\'s name is \'007\'')
# 原始字符串
print(r'My brother\'s name is \'007\'')

str = 'hello123world'
print('he' in str)
print('her' in str)
# 字符串是否只包含字母
print(str.isalpha())
# 字符串是否只包含字母和数字
print(str.isalnum())
# 字符串是否只包含数字
print(str.isdecimal())

print(str[0:5].isalpha())
print(str[5:8].isdecimal())

list = ['床前明月光', '疑是地上霜', '举头望明月', '低头思故乡']
print('-'.join(list))
sentence = 'You go your way I will go mine'
words_list = sentence.split()
print(words_list)
email = '     jackfrued@126.com          '
print(email)
print(email.strip())
print(email.lstrip())

# 将文本放入系统剪切板中
pyperclip.copy('老虎不发猫你当我病危呀')
# 从系统剪切板获得文本
print(pyperclip.paste())
```

    My brother's name is '007'
    My brother\'s name is \'007\'
    True
    False
    False
    True
    False
    True
    True
    床前明月光-疑是地上霜-举头望明月-低头思故乡
    ['You', 'go', 'your', 'way', 'I', 'will', 'go', 'mine']
         jackfrued@126.com          
    jackfrued@126.com
    jackfrued@126.com          
    


```python
"""
字符串常用操作 - 实现字符串倒转的方法
"""
from io import StringIO

def reverse_str1(str):
    return str[::-1]

def reverse_str2(str):
    if len(str) <= 1:
        return str
    return reverse_str2(str[1:]) + str[0:1]

def reverse_str3(str):
    # StringIO对象是Python中的可变字符串
    # 不应该使用不变字符串做字符串连接操作 因为会产生很多无用字符串对象
    rstr = StringIO()
    str_len = len(str)
    for index in range(str_len - 1, -1, -1):
        rstr.write(str[index])
    return rstr.getvalue()

def reverse_str4(str):
    return ''.join(str[index] for index in range(len(str) - 1, -1, -1))

def reverse_str5(str):
    # 将字符串处理成列表
    str_list = list(str)
    str_len = len(str)
    # 使用zip函数将两个序列合并成一个产生元组的迭代器
    # 每次正好可以取到一前一后两个下标来实现元素的交换
    for i, j in zip(range(str_len // 2), range(str_len - 1, str_len // 2, -1)):
        str_list[i], str_list[j] = str_list[j], str_list[i]
    # 将列表元素连接成字符串
    return ''.join(str_list)

if __name__ == '__main__':
    str = 'I love Python'
    print(reverse_str1(str))
    print(str)
    print(reverse_str2(str))
    print(str)
    print(reverse_str3(str))
    print(str)
    print(reverse_str4(str))
    print(str)
    print(reverse_str5(str))
    print(str)
```

    nohtyP evol I
    I love Python
    nohtyP evol I
    I love Python
    nohtyP evol I
    I love Python
    nohtyP evol I
    I love Python
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-50-f2f968e29a5d> in <module>
         46     print(reverse_str4(str))
         47     print(str)
    ---> 48     print(reverse_str5(str1))
         49     print(str1)
    

    <ipython-input-50-f2f968e29a5d> in reverse_str5(str1)
         26 def reverse_str5(str1):
         27     # 将字符串处理成列表
    ---> 28     str_list = list(str1)
         29     str_len = len(str1)
         30     # 使用zip函数将两个序列合并成一个产生元组的迭代器
    

    TypeError: 'list' object is not callable



```python
'''递归'''
def reverse_str2(str):
    if len(str) <= 1:
        return str
    return reverse_str2(str[1:]) + str[0:1]
reverse_str2('123456')
```




    '654321'


