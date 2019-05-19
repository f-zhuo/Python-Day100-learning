
                                            面向对象进阶

@property装饰器：使用@property包装器来包装getter（访问器）和setter（修改器）方法，使得对属性的访问既安全又方便


```python
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute

if __name__ == '__main__':
    main()
```

    王大锤正在玩飞行棋.
    王大锤正在玩斗地主.
    

__slots__魔法:只对当前类的对象生效，对子类并不起任何作用


```python
class Person(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

def main():
    person = Person('王大锤', 22)
    person.play()
    person._gender = '男'
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True
if __name__ == '__main__':
    main()
```

    王大锤正在玩斗地主.
    

静态方法: 不确定对象是否存在
类方法


```python
from math import sqrt

class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))

def main():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形.')

if __name__ == '__main__':
    main()
```

    12
    6.0
    

和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，
它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），
通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象


```python
from time import time, localtime, sleep

class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

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
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

if __name__ == '__main__':
    main()
```

    19:31:27
    19:31:28
    19:31:29
    


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-11-324ef1971a19> in <module>
         40 
         41 if __name__ == '__main__':
    ---> 42     main()
    

    <ipython-input-11-324ef1971a19> in main()
         36     while True:
         37         print(clock.show())
    ---> 38         sleep(1)
         39         clock.run()
         40 
    

    KeyboardInterrupt: 


类之间的关系有三种：
is-a: 继承或泛化，比如学生和人的关系、手机和电子产品的关系
has-a: 关联，比如部门和员工的关系，汽车和引擎的关系都属于关联关系；如果是整体和部分的关联，称之为聚合关系；
如果整体进一步负责了部分的生命周期（整体和部分是不可分割的，同时同在也同时消亡），那就是最强的关联关系，合成。
use-a: 依赖

继承:让一个类从另一个类那里将属性和方法直接继承下来，从而减少重复代码的编写。
提供继承信息的称为父类，也叫超类或基类；得到继承信息的称为子类，也叫派生类或衍生类。
子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力，
在实际开发中，经常会用子类对象去替换掉一个父类对象，对应的原则称之为里氏替换原则。


```python
class Person(object):
    """人"""
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)

class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))

class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))

def main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('骆昊', 38, '老叫兽')
    t.teach('Python程序设计')
    t.watch_av()

if __name__ == '__main__':
    main()
```

    初三的王大锤正在学习数学.
    王大锤只能观看《熊出没》.
    骆昊老叫兽正在讲Python程序设计.
    骆昊正在观看爱情动作片.
    

多态：子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写（override）。
通过方法重写可以让父类的同一个行为在子类中拥有不同的实现版本，当调用这个经过子类重写的方法时，
不同的子类对象会表现出不同的行为，这就是多态（poly-morphism）


```python
from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass

class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)

class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)

def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()
```

    旺财: 汪汪汪...
    凯蒂: 喵...喵...
    大黄: 汪汪汪...
    


```python
'''奥特曼打小怪兽'''
from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(object, metaclass=ABCMeta):
    """战斗者"""

    # 通过__slots__魔法限定对象可以绑定的成员变量
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """初始化方法
        param name: 名字
        param hp: 生命值
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """攻击
        param other: 被攻击的对象
        """
        pass

class Ultraman(Fighter):
    """奥特曼"""

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        """初始化方法
        param name: 名字
        param hp: 生命值
        param mp: 魔法值
        """
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """究极必杀技(打掉对方至少50点或四分之三的血)
        param other: 被攻击的对象
        return: 使用成功返回True否则返回False
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """魔法攻击
        param others: 被攻击的群体
        return: 使用魔法成功返回True否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        """恢复魔法值"""
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值: %d\n' % self._hp + \
            '魔法值: %d\n' % self._mp


class Monster(Fighter):
    """小怪兽"""

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
            '生命值: %d\n' % self._hp

def is_any_alive(monsters):
    """判断有没有小怪兽是活着的"""
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False

def select_alive_one(monsters):
    """选中一只活着的小怪兽"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster

def display_info(ultraman, monsters):
    """显示奥特曼和小怪兽的信息"""
    print(ultraman)
    for monster in monsters:
        print(monster, end='')

def main():
    u = Ultraman('骆昊', 1000, 120)
    m1 = Monster('狄仁杰', 250)
    m2 = Monster('李元芳', 500)
    m3 = Monster('王大锤', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('========第%02d回合========' % fight_round)
        m = select_alive_one(ms)  # 选中一只小怪兽
        skill = randint(1, 10)   # 通过随机数选择使用哪种技能
        if skill <= 6:  # 60%的概率使用普通攻击
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        elif skill <= 9:  # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败.' % u.name)
        else:  # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive > 0:  # 如果选中的小怪兽没有死就回击奥特曼
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪兽的信息
        fight_round += 1
    print('\n========战斗结束!========\n')
    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')

if __name__ == '__main__':
    main()
```

    ========第01回合========
    骆昊使用普通攻击打了王大锤.
    骆昊的魔法值恢复了3点.
    王大锤回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 982
    魔法值: 123
    
    ~~~狄仁杰小怪兽~~~
    生命值: 250
    ~~~李元芳小怪兽~~~
    生命值: 500
    ~~~王大锤小怪兽~~~
    生命值: 725
    ========第02回合========
    骆昊使用了魔法攻击.
    李元芳回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 971
    魔法值: 103
    
    ~~~狄仁杰小怪兽~~~
    生命值: 237
    ~~~李元芳小怪兽~~~
    生命值: 487
    ~~~王大锤小怪兽~~~
    生命值: 713
    ========第03回合========
    骆昊使用普通攻击打了狄仁杰.
    骆昊的魔法值恢复了4点.
    狄仁杰回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 951
    魔法值: 107
    
    ~~~狄仁杰小怪兽~~~
    生命值: 218
    ~~~李元芳小怪兽~~~
    生命值: 487
    ~~~王大锤小怪兽~~~
    生命值: 713
    ========第04回合========
    骆昊使用了魔法攻击.
    王大锤回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 933
    魔法值: 87
    
    ~~~狄仁杰小怪兽~~~
    生命值: 207
    ~~~李元芳小怪兽~~~
    生命值: 474
    ~~~王大锤小怪兽~~~
    生命值: 701
    ========第05回合========
    骆昊使用普通攻击打了李元芳.
    骆昊的魔法值恢复了9点.
    李元芳回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 913
    魔法值: 96
    
    ~~~狄仁杰小怪兽~~~
    生命值: 207
    ~~~李元芳小怪兽~~~
    生命值: 449
    ~~~王大锤小怪兽~~~
    生命值: 701
    ========第06回合========
    骆昊使用普通攻击打了王大锤.
    骆昊的魔法值恢复了6点.
    王大锤回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 895
    魔法值: 102
    
    ~~~狄仁杰小怪兽~~~
    生命值: 207
    ~~~李元芳小怪兽~~~
    生命值: 449
    ~~~王大锤小怪兽~~~
    生命值: 680
    ========第07回合========
    骆昊使用普通攻击打了王大锤.
    骆昊的魔法值恢复了9点.
    王大锤回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 885
    魔法值: 111
    
    ~~~狄仁杰小怪兽~~~
    生命值: 207
    ~~~李元芳小怪兽~~~
    生命值: 449
    ~~~王大锤小怪兽~~~
    生命值: 660
    ========第08回合========
    骆昊使用普通攻击打了王大锤.
    骆昊的魔法值恢复了9点.
    王大锤回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 871
    魔法值: 120
    
    ~~~狄仁杰小怪兽~~~
    生命值: 207
    ~~~李元芳小怪兽~~~
    生命值: 449
    ~~~王大锤小怪兽~~~
    生命值: 638
    ========第09回合========
    骆昊使用普通攻击打了狄仁杰.
    骆昊的魔法值恢复了8点.
    狄仁杰回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 857
    魔法值: 128
    
    ~~~狄仁杰小怪兽~~~
    生命值: 185
    ~~~李元芳小怪兽~~~
    生命值: 449
    ~~~王大锤小怪兽~~~
    生命值: 638
    ========第10回合========
    骆昊使用究极必杀技虐了李元芳.
    李元芳回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 837
    魔法值: 78
    
    ~~~狄仁杰小怪兽~~~
    生命值: 185
    ~~~李元芳小怪兽~~~
    生命值: 113
    ~~~王大锤小怪兽~~~
    生命值: 638
    ========第11回合========
    骆昊使用了魔法攻击.
    李元芳回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 826
    魔法值: 58
    
    ~~~狄仁杰小怪兽~~~
    生命值: 170
    ~~~李元芳小怪兽~~~
    生命值: 101
    ~~~王大锤小怪兽~~~
    生命值: 626
    ========第12回合========
    骆昊使用究极必杀技虐了王大锤.
    王大锤回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 810
    魔法值: 8
    
    ~~~狄仁杰小怪兽~~~
    生命值: 170
    ~~~李元芳小怪兽~~~
    生命值: 101
    ~~~王大锤小怪兽~~~
    生命值: 157
    ========第13回合========
    骆昊使用普通攻击打了狄仁杰.
    骆昊的魔法值恢复了3点.
    狄仁杰回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 795
    魔法值: 11
    
    ~~~狄仁杰小怪兽~~~
    生命值: 148
    ~~~李元芳小怪兽~~~
    生命值: 101
    ~~~王大锤小怪兽~~~
    生命值: 157
    ========第14回合========
    骆昊使用魔法失败.
    王大锤回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 779
    魔法值: 11
    
    ~~~狄仁杰小怪兽~~~
    生命值: 148
    ~~~李元芳小怪兽~~~
    生命值: 101
    ~~~王大锤小怪兽~~~
    生命值: 157
    ========第15回合========
    骆昊使用普通攻击打了狄仁杰.
    骆昊的魔法值恢复了8点.
    狄仁杰回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 759
    魔法值: 19
    
    ~~~狄仁杰小怪兽~~~
    生命值: 128
    ~~~李元芳小怪兽~~~
    生命值: 101
    ~~~王大锤小怪兽~~~
    生命值: 157
    ========第16回合========
    骆昊使用普通攻击打了李元芳.
    骆昊的魔法值恢复了9点.
    李元芳回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 741
    魔法值: 28
    
    ~~~狄仁杰小怪兽~~~
    生命值: 128
    ~~~李元芳小怪兽~~~
    生命值: 85
    ~~~王大锤小怪兽~~~
    生命值: 157
    ========第17回合========
    骆昊使用普通攻击打了王大锤.
    骆昊的魔法值恢复了8点.
    王大锤回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 721
    魔法值: 36
    
    ~~~狄仁杰小怪兽~~~
    生命值: 128
    ~~~李元芳小怪兽~~~
    生命值: 85
    ~~~王大锤小怪兽~~~
    生命值: 133
    ========第18回合========
    骆昊使用了魔法攻击.
    王大锤回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 704
    魔法值: 16
    
    ~~~狄仁杰小怪兽~~~
    生命值: 114
    ~~~李元芳小怪兽~~~
    生命值: 75
    ~~~王大锤小怪兽~~~
    生命值: 122
    ========第19回合========
    骆昊使用普通攻击打了王大锤.
    骆昊的魔法值恢复了8点.
    王大锤回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 686
    魔法值: 24
    
    ~~~狄仁杰小怪兽~~~
    生命值: 114
    ~~~李元芳小怪兽~~~
    生命值: 75
    ~~~王大锤小怪兽~~~
    生命值: 100
    ========第20回合========
    骆昊使用普通攻击打了狄仁杰.
    骆昊的魔法值恢复了10点.
    狄仁杰回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 673
    魔法值: 34
    
    ~~~狄仁杰小怪兽~~~
    生命值: 96
    ~~~李元芳小怪兽~~~
    生命值: 75
    ~~~王大锤小怪兽~~~
    生命值: 100
    ========第21回合========
    骆昊使用普通攻击打了李元芳.
    骆昊的魔法值恢复了7点.
    李元芳回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 663
    魔法值: 41
    
    ~~~狄仁杰小怪兽~~~
    生命值: 96
    ~~~李元芳小怪兽~~~
    生命值: 60
    ~~~王大锤小怪兽~~~
    生命值: 100
    ========第22回合========
    骆昊使用普通攻击打了狄仁杰.
    骆昊的魔法值恢复了1点.
    狄仁杰回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 649
    魔法值: 42
    
    ~~~狄仁杰小怪兽~~~
    生命值: 72
    ~~~李元芳小怪兽~~~
    生命值: 60
    ~~~王大锤小怪兽~~~
    生命值: 100
    ========第23回合========
    骆昊使用普通攻击打了李元芳.
    骆昊的魔法值恢复了3点.
    李元芳回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 634
    魔法值: 45
    
    ~~~狄仁杰小怪兽~~~
    生命值: 72
    ~~~李元芳小怪兽~~~
    生命值: 36
    ~~~王大锤小怪兽~~~
    生命值: 100
    ========第24回合========
    骆昊使用了魔法攻击.
    王大锤回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 620
    魔法值: 25
    
    ~~~狄仁杰小怪兽~~~
    生命值: 59
    ~~~李元芳小怪兽~~~
    生命值: 23
    ~~~王大锤小怪兽~~~
    生命值: 89
    ========第25回合========
    骆昊使用了魔法攻击.
    狄仁杰回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 600
    魔法值: 5
    
    ~~~狄仁杰小怪兽~~~
    生命值: 47
    ~~~李元芳小怪兽~~~
    生命值: 9
    ~~~王大锤小怪兽~~~
    生命值: 79
    ========第26回合========
    骆昊使用普通攻击打了狄仁杰.
    骆昊的魔法值恢复了6点.
    狄仁杰回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 590
    魔法值: 11
    
    ~~~狄仁杰小怪兽~~~
    生命值: 28
    ~~~李元芳小怪兽~~~
    生命值: 9
    ~~~王大锤小怪兽~~~
    生命值: 79
    ========第27回合========
    骆昊使用魔法失败.
    狄仁杰回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 576
    魔法值: 11
    
    ~~~狄仁杰小怪兽~~~
    生命值: 28
    ~~~李元芳小怪兽~~~
    生命值: 9
    ~~~王大锤小怪兽~~~
    生命值: 79
    ========第28回合========
    骆昊使用普通攻击打了李元芳.
    骆昊的魔法值恢复了8点.
    ~~~骆昊奥特曼~~~
    生命值: 576
    魔法值: 19
    
    ~~~狄仁杰小怪兽~~~
    生命值: 28
    ~~~李元芳小怪兽~~~
    生命值: 0
    ~~~王大锤小怪兽~~~
    生命值: 79
    ========第29回合========
    骆昊使用魔法失败.
    王大锤回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 559
    魔法值: 19
    
    ~~~狄仁杰小怪兽~~~
    生命值: 28
    ~~~李元芳小怪兽~~~
    生命值: 0
    ~~~王大锤小怪兽~~~
    生命值: 79
    ========第30回合========
    骆昊使用普通攻击打了狄仁杰.
    骆昊的魔法值恢复了9点.
    狄仁杰回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 539
    魔法值: 28
    
    ~~~狄仁杰小怪兽~~~
    生命值: 10
    ~~~李元芳小怪兽~~~
    生命值: 0
    ~~~王大锤小怪兽~~~
    生命值: 79
    ========第31回合========
    骆昊使用普通攻击打了狄仁杰.
    骆昊的魔法值恢复了6点.
    ~~~骆昊奥特曼~~~
    生命值: 539
    魔法值: 34
    
    ~~~狄仁杰小怪兽~~~
    生命值: 0
    ~~~李元芳小怪兽~~~
    生命值: 0
    ~~~王大锤小怪兽~~~
    生命值: 79
    ========第32回合========
    骆昊使用普通攻击打了王大锤.
    骆昊的魔法值恢复了7点.
    王大锤回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 527
    魔法值: 41
    
    ~~~狄仁杰小怪兽~~~
    生命值: 0
    ~~~李元芳小怪兽~~~
    生命值: 0
    ~~~王大锤小怪兽~~~
    生命值: 57
    ========第33回合========
    骆昊使用普通攻击打了王大锤.
    骆昊的魔法值恢复了10点.
    王大锤回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 514
    魔法值: 51
    
    ~~~狄仁杰小怪兽~~~
    生命值: 0
    ~~~李元芳小怪兽~~~
    生命值: 0
    ~~~王大锤小怪兽~~~
    生命值: 36
    ========第34回合========
    骆昊使用普通攻击打了王大锤.
    骆昊的魔法值恢复了4点.
    王大锤回击了骆昊.
    ~~~骆昊奥特曼~~~
    生命值: 498
    魔法值: 55
    
    ~~~狄仁杰小怪兽~~~
    生命值: 0
    ~~~李元芳小怪兽~~~
    生命值: 0
    ~~~王大锤小怪兽~~~
    生命值: 17
    ========第35回合========
    骆昊使用普通攻击打了王大锤.
    骆昊的魔法值恢复了10点.
    ~~~骆昊奥特曼~~~
    生命值: 498
    魔法值: 65
    
    ~~~狄仁杰小怪兽~~~
    生命值: 0
    ~~~李元芳小怪兽~~~
    生命值: 0
    ~~~王大锤小怪兽~~~
    生命值: 0
    
    ========战斗结束!========
    
    骆昊奥特曼胜利!
    


```python
'''扑克游戏'''
import random

class Card(object):
    """一张牌"""
    def __init__(self, suite, face):
        self._suite = suite
        self._face = face
        
    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, face_str)
    
    def __repr__(self):
        return self.__str__()

class Poker(object):
    """一副牌"""

    def __init__(self):
        self._cards = [Card(suite, face) 
                       for suite in '♠♥♣♦'
                       for face in range(1, 14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """洗牌(随机乱序)"""
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌"""
        return self._current < len(self._cards)

class Player(object):
    """玩家"""

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        """摸牌"""
        self._cards_on_hand.append(card)

    def arrange(self, card_key):
        """玩家整理手上的牌"""
        self._cards_on_hand.sort(key=card_key)

# 排序规则-先根据花色再根据点数排序
def get_key(card):
    return (card.suite, card.face)

def main():
    p = Poker()
    p.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    for _ in range(13):
        for player in players:
            player.get(p.next)
    for player in players:
        print(player.name + ':', end=' ')
        player.arrange(get_key)
        print(player.cards_on_hand)

if __name__ == '__main__':
    main()
```

    东邪: [♠A, ♠5, ♠8, ♠K, ♣3, ♣9, ♣10, ♥5, ♥8, ♥9, ♦10, ♦Q, ♦K]
    西毒: [♠2, ♠7, ♠J, ♣8, ♥6, ♥7, ♥J, ♥Q, ♦2, ♦6, ♦7, ♦8, ♦9]
    南帝: [♠6, ♠10, ♠Q, ♣5, ♣6, ♣7, ♣Q, ♣K, ♥4, ♦A, ♦3, ♦4, ♦J]
    北丐: [♠3, ♠4, ♠9, ♣A, ♣2, ♣4, ♣J, ♥A, ♥2, ♥3, ♥10, ♥K, ♦5]
    


```python
'''工资结算系统
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
'''
from abc import ABCMeta, abstractmethod

class Employee(object, metaclass=ABCMeta):
    """员工"""
    def __init__(self, name):
        """
        初始化方法
        param name: 姓名
        """
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        """
        获得月薪
        return: 月薪
        """
        pass

class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return 150.0 * self._working_hour

class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200.0 + self._sales * 0.05

def main():
    emps = [
        Manager('刘备'), Programmer('诸葛亮'),
        Manager('曹操'), Salesman('荀彧'),
        Salesman('吕布'), Programmer('张辽'),
        Programmer('赵云')
    ]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = int(input('请输入%s本月工作时间: ' % emp.name))
        elif isinstance(emp, Salesman):
            emp.sales = float(input('请输入%s本月销售额: ' % emp.name))
        # 同样是接收get_salary这个消息但是不同的员工表现出了不同的行为(多态)
        print('%s本月工资为: ￥%s元' %
              (emp.name, emp.get_salary()))

if __name__ == '__main__':
    main()
```

    刘备本月工资为: ￥15000.0元
    请输入诸葛亮本月工作时间: 360
    诸葛亮本月工资为: ￥54000.0元
    曹操本月工资为: ￥15000.0元
    请输入荀彧本月销售额: 300
    荀彧本月工资为: ￥1215.0元
    请输入吕布本月销售额: 20
    吕布本月工资为: ￥1201.0元
    请输入张辽本月工作时间: 240
    张辽本月工资为: ￥36000.0元
    请输入赵云本月工作时间: 300
    赵云本月工资为: ￥45000.0元
    


```python
"""
对象之间的关联关系
"""
from math import sqrt

class Point(object):

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def move_to(self, x, y):
        self._x = x
        self._y = y

    def move_by(self, dx, dy):
        self._x += dx
        self._y += dy

    def distance_to(self, other):
        dx = self._x - other._x
        dy = self._y - other._y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self._x), str(self._y))

class Line(object):

    def __init__(self, start=Point(0, 0), end=Point(0, 0)):
        self._start = start
        self._end = end

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        self._start = start

    @property
    def end(self):
        return self.end

    @end.setter
    def end(self, end):
        self._end = end

    @property
    def length(self):
        return self._start.distance_to(self._end)

if __name__ == '__main__':
    p1 = Point(3, 5)
    print(p1)
    p2 = Point(-2, -1.5)
    print(p2)
    line = Line(p1, p2)
    print(line.length)
    line.start.move_to(2, 1)
    line.end = Point(1, 2)
    print(line.length)
```

    (3, 5)
    (-2, -1.5)
    8.200609733428363
    1.4142135623730951
    


```python
"""
属性的使用
- 访问器/修改器/删除器
- 使用__slots__对属性加以限制
"""
class Car(object):
    __slots__ = ('_brand', '_max_speed')

    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @brand.deleter
    def brand(self):
        del self._brand

    @property
    def max_speed(self):
        return self._max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        if max_speed < 0:
            raise ValueError('Invalid max speed for car')
        self._max_speed = max_speed

    def __str__(self):
        return 'Car: [品牌=%s, 最高时速=%d]' % (self._brand, self._max_speed)

car = Car('QQ', 120)
print(car)
# ValueError
# car.max_speed = -100
car.max_speed = 320
car.brand = "Benz"
# 使用__slots__属性限制后下面的代码将产生异常
# car.current_speed = 80
print(car)
# 如果提供了删除器可以执行下面的代码
# del car.brand
# 属性的实现
print(Car.brand)
print(Car.brand.fget)
print(Car.brand.fset)
print(Car.brand.fdel)

```

    Car: [品牌=QQ, 最高时速=120]
    Car: [品牌=Benz, 最高时速=320]
    <property object at 0x000001CC5DE180E8>
    <function Car.brand at 0x000001CC5DE040D0>
    <function Car.brand at 0x000001CC5DE04158>
    <function Car.brand at 0x000001CC5DE041E0>
    


```python
"""
属性的使用
- 使用已有方法定义访问器/修改器/删除器
"""
class Car(object):

    def __init__(self, brand, max_speed):
        self.set_brand(brand)
        self.set_max_speed(max_speed)

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

    def get_max_speed(self):
        return self._max_speed

    def set_max_speed(self, max_speed):
        if max_speed < 0:
            raise ValueError('Invalid max speed for car')
        self._max_speed = max_speed

    def __str__(self):
        return 'Car: [品牌=%s, 最高时速=%d]' % (self._brand, self._max_speed)

    # 用已有的修改器和访问器定义属性
    brand = property(get_brand, set_brand)
    max_speed = property(get_max_speed, set_max_speed)

car = Car('QQ', 120)
print(car)
# ValueError
# car.max_speed = -100
car.max_speed = 320
car.brand = "Benz"
print(car)
print(Car.brand)
print(Car.brand.fget)
print(Car.brand.fset)
```

    Car: [品牌=QQ, 最高时速=120]
    Car: [品牌=Benz, 最高时速=320]
    <property object at 0x000001CC5DE184A8>
    <function Car.get_brand at 0x000001CC5DE04950>
    <function Car.set_brand at 0x000001CC5DE048C8>
    


```python
"""
对象之间的依赖关系和运算符重载
"""
class Car(object):

    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed
        self._current_speed = 0

    @property
    def brand(self):
        return self._brand

    def accelerate(self, delta):
        self._current_speed += delta
        if self._current_speed > self._max_speed:
            self._current_speed = self._max_speed

    def brake(self):
        self._current_speed = 0

    def __str__(self):
        return '%s当前时速%d' % (self._brand, self._current_speed)

class Student(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    # 学生和车之间存在依赖关系 - 学生使用了汽车
    def drive(self, car):
        print('%s驾驶着%s欢快的行驶在去西天的路上' % (self._name, car._brand))
        car.accelerate(30)
        print(car)
        car.accelerate(50)
        print(car)
        car.accelerate(50)
        print(car)

    def study(self, course_name):
        print('%s正在学习%s.' % (self._name, course_name))

    def watch_av(self):
        if self._age < 18:
            print('%s只能观看《熊出没》.' % self._name)
        else:
            print('%s正在观看岛国爱情动作片.' % self._name)

    # 重载大于(>)运算符
    def __gt__(self, other):
        return self._age > other._age

    # 重载小于(<)运算符
    def __lt__(self, other):
        return self._age < other._age

if __name__ == '__main__':
    stu1 = Student('骆昊', 38)
    stu1.study('Python程序设计')
    stu1.watch_av()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_av()
    car = Car('QQ', 120)
    stu2.drive(car)
    print(stu1 > stu2)
    print(stu1 < stu2)
```

    骆昊正在学习Python程序设计.
    骆昊正在观看岛国爱情动作片.
    王大锤正在学习思想品德.
    王大锤只能观看《熊出没》.
    王大锤驾驶着QQ欢快的行驶在去西天的路上
    QQ当前时速30
    QQ当前时速80
    QQ当前时速120
    True
    False
    


```python
"""
多重继承
- 菱形继承(钻石继承)
- C3算法(替代DFS的算法)
"""
class A(object):

    def foo(self):
        print('foo of A')

class B(A):
    pass

class C(A):

    def foo(self):
        print('foo fo C')

class D(B, C):
    pass

class E(D):

    def foo(self):
        print('foo in E')
        super().foo()
        super(B, self).foo()
        super(C, self).foo()

if __name__ == '__main__':
    d = D()
    d.foo()
    e = E()
    e.foo()
```

    foo fo C
    foo in E
    foo fo C
    foo fo C
    foo of A
    


```python
"""
多重继承
- 通过多重继承可以给一个类的对象具备多方面的能力
- 这样在设计类的时候可以避免设计太多层次的复杂的继承关系

"""
class Father(object):

    def __init__(self, name):
        self._name = name

    def gamble(self):
        print('%s在打麻将.' % self._name)

    def eat(self):
        print('%s在大吃大喝.' % self._name)

class Monk(object):

    def __init__(self, name):
        self._name = name

    def eat(self):
        print('%s在吃斋.' % self._name)

    def chant(self):
        print('%s在念经.' % self._name)

class Musician(object):

    def __init__(self, name):
        self._name = name

    def eat(self):
        print('%s在细嚼慢咽.' % self._name)

    def play_piano(self):
        print('%s在弹钢琴.' % self._name)

# 试一试下面的代码看看有什么区别
# class Son(Monk, Father, Musician):
# class Son(Musician, Father, Monk):

class Son(Father, Monk, Musician):

    def __init__(self, name):
        Father.__init__(self, name)
        Monk.__init__(self, name)
        Musician.__init__(self, name)

son = Son('王大锤')
son.gamble()
# 调用继承自Father的eat方法
son.eat()
son.chant()
son.play_piano()
```

    王大锤在打麻将.
    王大锤在大吃大喝.
    王大锤在念经.
    王大锤在弹钢琴.
    


```python
"""
运算符重载 - 自定义分数类
"""
from math import gcd

class Rational(object):

    def __init__(self, num, den=1):
        if den == 0:
            raise ValueError('分母不能为0')
        self._num = num
        self._den = den
        self.normalize()

    def simplify(self):
        x = abs(self._num)
        y = abs(self._den)
        factor = gcd(x, y)
        if factor > 1:
            self._num //= factor
            self._den //= factor
        return self

    def normalize(self):
        if self._den < 0:
            self._den = -self._den
            self._num = -self._num
        return self

    def __add__(self, other):
        new_num = self._num * other._den + other._num * self._den
        new_den = self._den * other._den
        return Rational(new_num, new_den).simplify().normalize()

    def __sub__(self, other):
        new_num = self._num * other._den - other._num * self._den
        new_den = self._den * other._den
        return Rational(new_num, new_den).simplify().normalize()

    def __mul__(self, other):
        new_num = self._num * other._num
        new_den = self._den * other._den
        return Rational(new_num, new_den).simplify().normalize()

    def __truediv__(self, other):
        new_num = self._num * other._den
        new_den = self._den * other._num
        return Rational(new_num, new_den).simplify().normalize()

    def __str__(self):
        if self._num == 0:
            return '0'
        elif self._den == 1:
            return str(self._num)
        else:
            return '(%d/%d)' % (self._num, self._den)

if __name__ == '__main__':
    r1 = Rational(2, 3)
    print(r1)
    r2 = Rational(6, -8)
    print(r2)
    print(r2.simplify())
    print('%s + %s = %s' % (r1, r2, r1 + r2))
    print('%s - %s = %s' % (r1, r2, r1 - r2))
    print('%s * %s = %s' % (r1, r2, r1 * r2))
    print('%s / %s = %s' % (r1, r2, r1 / r2))
```

    (2/3)
    (-6/8)
    (-3/4)
    (2/3) + (-3/4) = (-1/12)
    (2/3) - (-3/4) = (17/12)
    (2/3) * (-3/4) = (-1/2)
    (2/3) / (-3/4) = (-8/9)
    


```python
"""
继承的应用
- 抽象类
- 抽象方法
- 方法重写
- 多态
"""
from abc import ABCMeta, abstractmethod
from math import pi

class Shape(object, metaclass=ABCMeta):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    def perimeter(self):
        return 2 * pi * self._radius

    def area(self):
        return pi * self._radius ** 2

    def __str__(self):
        return '我是一个圆'

class Rect(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __str__(self):
        return '我是一个矩形'

if __name__ == '__main__':
    shapes = [Circle(5), Circle(3.2), Rect(3.2, 6.3)]
    for shape in shapes:
        print(shape)
        print('周长:', shape.perimeter())
        print('面积:', shape.area())
```

    我是一个圆
    周长: 31.41592653589793
    面积: 78.53981633974483
    我是一个圆
    周长: 20.106192982974676
    面积: 32.169908772759484
    我是一个矩形
    周长: 19.0
    面积: 20.16
    


```python
"""
实例方法和类方法的应用
"""
from math import sqrt

class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # 静态方法
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and c + a > b

    # 实例方法
    def perimeter(self):
        return self._a + self._b + self._c

    # 实例方法
    def area(self):
        p = self.perimeter() / 2
        return sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))

if __name__ == '__main__':
    # 用字符串的split方法将字符串拆分成一个列表
    # 再通过map函数对列表中的每个字符串进行映射处理成小数
    a, b, c = map(float, input('请输入三条边: ').split())
    # 先判断给定长度的三条边能否构成三角形
    # 如果能才创建三角形对象
    if Triangle.is_valid(a, b, c):
        tri = Triangle(a, b, c)
        print('周长:', tri.perimeter())
        print('面积:', tri.area())
        # 如果传入对象作为方法参数也可以通过类调用实例方法
        # print('周长:', Triangle.perimeter(tri))
        # print('面积:', Triangle.area(tri))
        # 看看下面的代码就知道其实二者本质上是一致的
        # print(type(tri.perimeter))
        # print(type(Triangle.perimeter))
    else:
        print('不能构成三角形.')
```

    请输入三条边: 3 4 5
    周长: 12.0
    面积: 6.0
    


```python

```


```python

```
