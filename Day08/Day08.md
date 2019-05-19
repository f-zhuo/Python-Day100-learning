
               面向对象编程基础

面向对象的三大要素：封装，继承，多态

类与对象：
类是具有相同或相似属性与行为的对象的集合，对象是类的实例。


```python
'''定义类'''
class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是很多程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_av(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情动作片.' % self.name)
st1=Student('王莽',12)
st1.study('数学')
st1.watch_av()
```

    王莽正在学习数学.
    王莽只能观看《熊出没》.
    


```python
'''创建和使用对象'''
def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('骆昊', 38)
    # 给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_av()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_av()
    
if __name__ == '__main__':
    main()
```

    骆昊正在学习Python程序设计.
    骆昊正在观看岛国爱情动作片.
    王大锤正在学习思想品德.
    王大锤只能观看《熊出没》.
    


```python
'''访问可见性问题（访问权限）：公开，私有。
如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头。'''
class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

def main():
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    print(test.__foo)


if __name__ == "__main__":
    main()
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-16-8d0e4185d17c> in <module>
         18 
         19 if __name__ == "__main__":
    ---> 20     main()
    

    <ipython-input-16-8d0e4185d17c> in main()
         12     test = Test('hello')
         13     # AttributeError: 'Test' object has no attribute '__bar'
    ---> 14     test.__bar()
         15     # AttributeError: 'Test' object has no attribute '__foo'
         16     print(test.__foo)
    

    AttributeError: 'Test' object has no attribute '__bar'



```python
'''如果知道更换名字的规则仍然可以访问私有的属性,
遵循一种命名惯例:让属性名以单下划线开头来表示属性是受保护的'''
class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)

if __name__ == "__main__":
    main()
```

    hello
    __bar
    hello
    


```python
'''定义一个类描述数字时钟'''
class Clock(object):
    
    def __init__(self,hour=0,minute=0,second=0):
        self._hour=hour
        self._minute=minute
        self._second=second
        
    def run(self):
        self._second+=1
        if self._second==60:
            self._second=0
            self._minute+=1
            if self._minute==60:
                self._minute=0
                self._hour+=1
                if self._hour==24:
                    self._hour=0
                    
    def show(self):
        print('%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)) 
    
def main():
    import time
    clock=Clock(0,0,0)
    while True:
        clock.run()
        clock.show()
        time.sleep(1)
    
if __name__=='__main__':
    main()
```

    00:00:01
    00:00:02
    00:00:03
    00:00:04
    00:00:05
    00:00:06
    00:00:07
    00:00:08
    00:00:09
    00:00:10
    00:00:11
    00:00:12
    00:00:13
    00:00:14
    00:00:15
    


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-10-1b8eb9b6583f> in <module>
         31 
         32 if __name__=='__main__':
    ---> 33     main()
    

    <ipython-input-10-1b8eb9b6583f> in main()
         28         clock.run()
         29         clock.show()
    ---> 30         time.sleep(1)
         31 
         32 if __name__=='__main__':
    

    KeyboardInterrupt: 



```python
class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    import time
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        time.sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
```

    23:59:58
    23:59:59
    00:00:00
    00:00:01
    00:00:02
    00:00:03
    00:00:04
    00:00:05
    00:00:06
    00:00:07
    00:00:08
    00:00:09
    00:00:10
    00:00:11
    00:00:12
    00:00:13
    00:00:14
    00:00:15
    


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-31-917e1231105b> in <module>
         41 
         42 if __name__ == '__main__':
    ---> 43     main()
    

    <ipython-input-31-917e1231105b> in main()
         36     while True:
         37         print(clock.show())
    ---> 38         time.sleep(1)
         39         clock.run()
         40 
    

    KeyboardInterrupt: 



```python
'''定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法'''
from math import sqrt
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self,delt_x,delt_y):
        self.x2=delt_x+self.x
        self.y2=delt_y+self.y
    def calculate(self,x2,y2):
        self.x2=x2
        self.y2=y2
        dist_x=self.x2-self.x
        dist_y=self.y2-self.y
        dist=sqrt(dist_x**2+dist_y**2)
        return '{:.2f}'.format(dist)
    def __str__(self):
        return ('({:s},{:s})'.format(str(self.x),str(self.y)))
        return ('({:s},{:s})'.format(str(self.x2),str(self.y2)))
def main():
    p1=point(1,1)
    print(p1)
    p2=p1.move(1,1)
    dist=p1.calculate(3,3)
    print(dist)
    #print(p2)
if __name__=='__main__':
    main()
```

    (1,1)
    2.83
    


```python
from math import sqrt
class Point(object):

    def __init__(self, x=0, y=0):
        """初始化方法
        param x: 横坐标
        param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """移动到指定位置
        param x: 新的横坐标
        param y: 新的纵坐标
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """移动指定的增量
        param dx: 横坐标的增量
        param dy: 纵坐标的增量
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """计算与另一个点的距离
        param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    # print(p2.move_by(-1, 2)) 结果为None
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()
```

    (3, 5)
    (0, 0)
    (-1, 2)
    5.0
    


```python
'''修一个游泳池 半径(以米为单位)在程序运行时输入 游泳池外修一条3米宽的过道
过道的外侧修一圈围墙 已知过道的造价为25元每平米 围墙的造价为32.5元每米
输出围墙和过道的总造价分别是多少钱(精确到小数点后2位)'''
import math 
class cost:
    def __init__(self,r):
        self.r=r
    def area_path(self):
        return math.pi*((self.r+3)**2-self.r**2)
    def area_wall(self,h):
        self.h=h
        return 2*math.pi*(self.r+3)*self.h
def main():
    r=int(input('请输入游泳池半径：'))
    sw_pol=cost(r)
    sw_pol.cost_path=sw_pol.area_path()*25
    sw_pol.cost_wall=sw_pol.area_wall(6)*32.5
    print('{:.2f}'.format(sw_pol.cost_path+sw_pol.cost_wall))
if __name__=='__main__':
    main()
```

    请输入游泳池半径：5
    12864.82
    


```python
import math

class Circle(object):

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius if radius > 0 else 0

    @property
    def perimeter(self):
        return 2 * math.pi * self._radius

    @property
    def area(self):
        return math.pi * self._radius * self._radius

if __name__ == '__main__':  
    radius = float(input('请输入游泳池的半径: '))
    small = Circle(radius)
    big = Circle(radius + 3)
    print('围墙的造价为: ￥%.1f元' % (big.perimeter * 115))
    print('过道的造价为: ￥%.1f元' % ((big.area - small.area) * 65))
```

    请输入游泳池的半径: 5
    围墙的造价为: ￥5780.5元
    过道的造价为: ￥7963.9元
    


```python
import time
import os

class Clock(object):
    # Python中的函数是没有重载的概念的
    # 因为Python中函数的参数没有类型而且支持缺省参数和可变参数
    # 用关键字参数让构造器可以传入任意多个参数来实现其他语言中的构造器重载
    def __init__(self, **kw):
        if 'hour' in kw and 'minute' in kw and 'second' in kw:
            self._hour = kw['hour']
            self._minute = kw['minute']
            self._second = kw['second']
        else:
            tm = time.localtime(time.time())
            self._hour = tm.tm_hour
            self._minute = tm.tm_min
            self._second = tm.tm_sec

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

if __name__ == '__main__':
    # clock = Clock(hour=10, minute=5, second=58)
    clock = Clock()
    while True:
        os.system('clear')
        print(clock.show())
        time.sleep(1)
        clock.run()
```

    16:29:23
    16:29:24
    16:29:25
    16:29:26
    16:29:27
    16:29:28
    16:29:29
    16:29:30
    16:29:31
    16:29:32
    16:29:33
    16:29:34
    16:29:35
    16:29:36
    16:29:37
    16:29:38
    16:29:39
    16:29:40
    16:29:41
    16:29:42
    16:29:43
    16:29:44
    16:29:45
    16:29:46
    16:29:47
    16:29:48
    16:29:49
    16:29:50
    16:29:51
    16:29:52
    16:29:53
    16:29:54
    16:29:55
    16:29:56
    16:29:57
    16:29:58
    16:29:59
    16:30:00
    16:30:01
    


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-48-70b132d80405> in <module>
         38         os.system('clear')
         39         print(clock.show())
    ---> 40         time.sleep(1)
         41         clock.run()
    

    KeyboardInterrupt: 



```python
"""
面向对象版本的猜数字游戏
"""
from random import randint
class GuessMachine(object):

    def __init__(self):
        self._answer = None
        self._counter = None
        self._hint = None

    def reset(self):
        self._answer = randint(1, 100)
        self._counter = 0
        self._hint = None

    def guess(self, your_answer):
        self._counter += 1
        if your_answer > self._answer:
            self._hint = '小一点'
        elif your_answer < self._answer:
            self._hint = '大一点'
        else:
            self._hint = '恭喜你猜对了'
            return True
        return False

    @property
    def counter(self):
        return self._counter

    @property
    def hint(self):
        return self._hint

if __name__ == '__main__':
    gm = GuessMachine()
    play_again = True
    while play_again:
        game_over = False
        gm.reset()
        while not game_over:
            your_answer = int(input('请输入: '))
            game_over = gm.guess(your_answer)
            print(gm.hint)
        if gm.counter > 7:
            print('智商余额不足!')
        play_again = input('再玩一次?(yes|no)') == 'yes'
```

    请输入: 50
    小一点
    请输入: 25
    大一点
    请输入: 37
    小一点
    请输入: 30
    小一点
    请输入: 27
    大一点
    请输入: 28
    大一点
    请输入: 29
    恭喜你猜对了
    再玩一次?(yes|no)yes
    请输入: 50
    小一点
    请输入: 25
    小一点
    请输入: 36
    小一点
    请输入: 30
    小一点
    请输入: 27
    小一点
    请输入: 26
    小一点
    请输入: 12
    小一点
    请输入: 8
    小一点
    请输入: 6
    小一点
    请输入: 4
    小一点
    请输入: 2
    小一点
    请输入: 1
    恭喜你猜对了
    智商余额不足!
    再玩一次?(yes|no)yes
    请输入: 50
    小一点
    请输入: 25
    小一点
    请输入: 12
    大一点
    请输入: 18
    小一点
    请输入: 15
    大一点
    请输入: 17
    恭喜你猜对了
    再玩一次?(yes|no)no
    


```python
"""
另一种创建类的方式

"""

def bar(self, name):
    self._name = name

def foo(self, course_name):
    print('%s正在学习%s.' % (self._name, course_name))

def main():
    Student = type('Student', (object,), dict(__init__=bar, study=foo))
    stu1 = Student('骆昊')
    stu1.study('Python程序设计')

if __name__ == '__main__':
    main()  
```

    骆昊正在学习Python程序设计.
    


```python
"""
定义和使用矩形类
"""
class Rect(object):
    """矩形类"""
    
    def __init__(self, width=0, height=0):
        """初始化方法"""
        self.__width = width
        self.__height = height

    def perimeter(self):
        """计算周长"""
        return (self.__width + self.__height) * 2

    def area(self):
        """计算面积"""
        return self.__width * self.__height

    def __str__(self):
        """矩形对象的字符串表达式"""
        return '矩形[%f,%f]' % (self.__width, self.__height)

    def __del__(self):
        """析构器"""
        print('销毁矩形对象')

if __name__ == '__main__':
    rect1 = Rect()
    print(rect1)
    print(rect1.perimeter())
    print(rect1.area())
    rect2 = Rect(3.5, 4.5)
    print(rect2)
    print(rect2.perimeter())
    print(rect2.area())
```

    销毁矩形对象
    矩形[0.000000,0.000000]
    0
    0
    销毁矩形对象
    矩形[3.500000,4.500000]
    16.0
    15.75
    


```python

```
