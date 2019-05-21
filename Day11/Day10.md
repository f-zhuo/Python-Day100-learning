
              图形用户界面和游戏开发
python的GUI模块：wxPython、PyQt、PyGTK、tkinter（默认）


```python
import tkinter
import tkinter.messagebox

def main():
    flag = True
    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('240x160')
    # 设置窗口标题
    top.title('小游戏')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()

if __name__ == '__main__':
    main()
```


```python
'''使用Pygame进行游戏开发:'''
import pygame

def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == '__main__':
    main()
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-1-6450dd904b45> in <module>
          1 '''使用Pygame进行游戏开发:'''
    ----> 2 import pygame
          3 
          4 def main():
          5     # 初始化导入的pygame中的模块
    

    ModuleNotFoundError: No module named 'pygame'



```python
import pygame

def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    # 设置窗口的背景色(颜色是由红绿蓝三原色构成的元组)
    screen.fill((242, 242, 242))
    # 绘制一个圆(参数分别是: 屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
    pygame.draw.circle(screen, (255, 0, 0,), (100, 100), 30, 0)
    # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
    pygame.display.flip()
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == '__main__':
    main()
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-2-eccb0e0bb54a> in <module>
    ----> 1 import pygame
          2 
          3 def main():
          4     # 初始化导入的pygame中的模块
          5     pygame.init()
    

    ModuleNotFoundError: No module named 'pygame'



```python
import pygame

def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    # 设置窗口的背景色(颜色是由红绿蓝三原色构成的元组)
    screen.fill((255, 255, 255))
    # 通过指定的文件名加载图像
    ball_image = pygame.image.load('./res/ball.png')
    # 在窗口上渲染图像
    screen.blit(ball_image, (50, 50))
    # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
    pygame.display.flip()
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == '__main__':
    main()
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-3-6a72f7667e21> in <module>
    ----> 1 import pygame
          2 
          3 def main():
          4     # 初始化导入的pygame中的模块
          5     pygame.init()
    

    ModuleNotFoundError: No module named 'pygame'



```python
import pygame

def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    # 定义变量来表示小球在屏幕上的位置
    x, y = 50, 50
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0,), (x, y), 30, 0)
        pygame.display.flip()
        # 每隔50毫秒就改变小球的位置再刷新窗口
        pygame.time.delay(50)
        x, y = x + 5, y + 5

if __name__ == '__main__':
    main()
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-4-c3b98a4c2bb5> in <module>
    ----> 1 import pygame
          2 
          3 def main():
          4     # 初始化导入的pygame中的模块
          5     pygame.init()
    

    ModuleNotFoundError: No module named 'pygame'



```python
'''碰撞检测'''
from enum import Enum, unique
from math import sqrt
from random import randint

import pygame

@unique
class Color(Enum):
    """颜色"""
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """获得随机颜色"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)

class Ball(object):
    """球"""
    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        """初始化方法"""
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        """移动"""
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        """吃其他球"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        """在窗口上绘制球"""
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-5-232cfdd4a4a3> in <module>
          4 from random import randint
          5 
    ----> 6 import pygame
          7 
          8 @unique
    

    ModuleNotFoundError: No module named 'pygame'



```python
'''事件处理:type属性判定事件类型，pos属性获得鼠标点击的位置'''
def main():
    # 定义用来装所有球的容器
    balls = []
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # 处理鼠标事件的代码
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 获得点击鼠标的位置
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                # 在点击鼠标的位置创建一个球(大小、速度和颜色随机)
                ball = Ball(x, y, radius, sx, sy, color)
                # 将球添加到列表容器中
                balls.append(ball)
        screen.fill((255, 255, 255))
        # 取出容器中的球 如果没被吃掉就绘制 被吃掉了就移除
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        # 每隔50毫秒就改变球的位置再刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # 检查球有没有吃到其他的球
            for other in balls:
                ball.eat(other)

if __name__ == '__main__':
    main()
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-1a9c4f3c5e86> in <module>
         44 
         45 if __name__ == '__main__':
    ---> 46     main()
    

    <ipython-input-6-1a9c4f3c5e86> in main()
          4     balls = []
          5     # 初始化导入的pygame中的模块
    ----> 6     pygame.init()
          7     # 初始化用于显示的窗口并设置窗口尺寸
          8     screen = pygame.display.set_mode((800, 600))
    

    NameError: name 'pygame' is not defined



```python

```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-7-6c98e2b35e8e> in <module>
          3 from random import randint
          4 
    ----> 5 import pygame
          6 
          7 
    

    ModuleNotFoundError: No module named 'pygame'



```python
"""
使用tkinter创建GUI
- 使用画布绘图
- 处理鼠标事件
"""
import tkinter

def mouse_evt_handler(evt=None):
    row = round((evt.y - 20) / 40)
    col = round((evt.x - 20) / 40)
    pos_x = 40 * col
    pos_y = 40 * row
    canvas.create_oval(pos_x, pos_y, 40 + pos_x, 40 + pos_y, fill='black')

top = tkinter.Tk()
# 设置窗口尺寸
top.geometry('620x620')
# 设置窗口标题
top.title('五子棋')
# 设置窗口大小不可改变
top.resizable(False, False)
# 设置窗口置顶
top.wm_attributes('-topmost', 1)
canvas = tkinter.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)
canvas.bind('<Button-1>', mouse_evt_handler)
canvas.create_rectangle(0, 0, 600, 600, fill='yellow', outline='white')
for index in range(15):
    canvas.create_line(20, 20 + 40 * index, 580, 20 + 40 * index, fill='black')
    canvas.create_line(20 + 40 * index, 20, 20 + 40 * index, 580, fill='black')
canvas.create_rectangle(15, 15, 585, 585, outline='black', width=4)
canvas.pack()
tkinter.mainloop()

```


```python
"""
使用tkinter创建GUI
- 在窗口上制作动画
"""
import tkinter
import time

# 播放动画效果的函数
def play_animation():
    canvas.move(oval, 2, 2)
    canvas.update()
    top.after(50, play_animation)

x = 10
y = 10
top = tkinter.Tk()
top.geometry('600x600')
top.title('动画效果')
top.resizable(False, False)
top.wm_attributes('-topmost', 1)
canvas = tkinter.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, 600, 600, fill='gray')
oval = canvas.create_oval(10, 10, 60, 60, fill='red')
canvas.pack()
top.update()
play_animation()
tkinter.mainloop()

```


```python
import pygame

EMPTY = 0
BLACK = 1
WHITE = 2

black_color = [0, 0, 0]
white_color = [255, 255, 255]

class RenjuBoard(object):

    def __init__(self):
        self._board = [[]] * 15
        self.reset()

    def reset(self):
        for row in range(len(self._board)):
            self._board[row] = [EMPTY] * 15

    def move(self, row, col, is_black):
        if self._board[row][col] == EMPTY:
            self._board[row][col] = BLACK if is_black else WHITE
            return True
        return False

    def draw(self, screen):
        for index in range(1, 16):
            pygame.draw.line(screen, black_color,
                             [40, 40 * index], [600, 40 * index], 1)
            pygame.draw.line(screen, black_color,
                             [40 * index, 40], [40 * index, 600], 1)
        pygame.draw.rect(screen, black_color, [36, 36, 568, 568], 4)
        pygame.draw.circle(screen, black_color, [320, 320], 5, 0)
        pygame.draw.circle(screen, black_color, [160, 160], 5, 0)
        pygame.draw.circle(screen, black_color, [480, 480], 5, 0)
        pygame.draw.circle(screen, black_color, [480, 160], 5, 0)
        pygame.draw.circle(screen, black_color, [160, 480], 5, 0)
        for row in range(len(self._board)):
            for col in range(len(self._board[row])):
                if self._board[row][col] != EMPTY:
                    ccolor = black_color \
                        if self._board[row][col] == BLACK else white_color
                    pos = [40 * (col + 1), 40 * (row + 1)]
                    pygame.draw.circle(screen, ccolor, pos, 20, 0)

def main():
    board = RenjuBoard()
    is_black = True
    pygame.init()
    pygame.display.set_caption('五子棋')
    screen = pygame.display.set_mode([640, 640])
    screen.fill([255, 255, 0])
    board.draw(screen)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                pass
            elif event.type == pygame.MOUSEBUTTONDOWN\
                    and event.button == 1:
                x, y = event.pos
                row = round((y - 40) / 40)
                col = round((x - 40) / 40)
                if board.move(row, col, is_black):
                    is_black = not is_black
                    screen.fill([255, 255, 0])
                    board.draw(screen)
                    pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-10-717b885c3111> in <module>
    ----> 1 import pygame
          2 
          3 EMPTY = 0
          4 BLACK = 1
          5 WHITE = 2
    

    ModuleNotFoundError: No module named 'pygame'



```python
from abc import ABCMeta, abstractmethod
from enum import Enum, unique
from random import randrange
from threading import Thread

import pygame

class Color(object):
    """颜色"""

    GRAY = (242, 242, 242)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    PINK = (255, 20, 147)

@unique
class Direction(Enum):
    """方向"""
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class GameObject(object, metaclass=ABCMeta):
    """游戏中的对象"""

    def __init__(self, x=0, y=0, color=Color.BLACK):
        """
        初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        :param color: 颜色
        """
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @abstractmethod
    def draw(self, screen):
        """
        绘制
        :param screen: 屏幕
        """
        pass

class Wall(GameObject):
    """围墙"""

    def __init__(self, x, y, width, height, color=Color.BLACK):
        """
        初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        :param width: 宽度
        :param height: 高度
        :param color: 颜色
        """
        super().__init__(x, y, color)
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def draw(self, screen):
        pygame.draw.rect(screen, self._color,
                         (self._x, self._y, self._width, self._height), 4)

class Food(GameObject):
    """食物"""

    def __init__(self, x, y, size, color=Color.PINK):
        """
        初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        :param size: 大小
        :param color: 颜色
        """
        super().__init__(x, y, color)
        self._size = size
        self._hidden = False

    def draw(self, screen):
        if not self._hidden:
            pygame.draw.circle(screen, self._color,
                               (self._x + self._size // 2, self._y + self._size // 2),
                               self._size // 2, 0)
        self._hidden = not self._hidden

class SnakeNode(GameObject):
    """蛇身上的节点"""

    def __init__(self, x, y, size, color=Color.GREEN):
        """
        初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        :param size: 大小
        :param color: 颜色
        """
        super().__init__(x, y, color)
        self._size = size

    @property
    def size(self):
        return self._size

    def draw(self, screen):
        pygame.draw.rect(screen, self._color,
                         (self._x, self._y, self._size, self._size), 0)
        pygame.draw.rect(screen, Color.BLACK,
                         (self._x, self._y, self._size, self._size), 1)

class Snake(GameObject):
    """蛇"""
    def __init__(self, x, y, size=20, length=5):
        """
        初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        :param size: 大小
        :param length: 初始长度
        """
        super().__init__()
        self._dir = Direction.LEFT
        self._nodes = []
        self._alive = True
        self._new_dir = None
        for index in range(length):
            node = SnakeNode(x + index * size, y, size)
            self._nodes.append(node)

    @property
    def dir(self):
        return self._dir

    @property
    def alive(self):
        return self._alive

    @property
    def head(self):
        return self._nodes[0]

    def change_dir(self, new_dir):
        """
        改变方向
        :param new_dir: 新方向
        """
        if new_dir != self._dir and \
                (self._dir.value + new_dir.value) % 2 != 0:
            self._new_dir = new_dir

    def move(self):
        """移动"""
        if self._new_dir:
            self._dir, self._new_dir = self._new_dir, None
        snake_dir = self._dir
        x, y, size = self.head.x, self.head.y, self.head.size
        if snake_dir == Direction.UP:
            y -= size
        elif snake_dir == Direction.RIGHT:
            x += size
        elif snake_dir == Direction.DOWN:
            y += size
        else:
            x -= size
        new_head = SnakeNode(x, y, size)
        self._nodes.insert(0, new_head)
        self._nodes.pop()

    def collide(self, wall):
        """
        撞墙
        :param wall: 围墙
        """
        head = self.head
        if head.x < wall.x or head.x + head.size > wall.x + wall.width \
                or head.y < wall.y or head.y + head.size > wall.y + wall.height:
            self._alive = False

    def eat_food(self, food):
        """
        吃食物
        :param food: 食物
        :return: 吃到食物返回True否则返回False
        """
        if self.head.x == food.x and self.head.y == food.y:
            tail = self._nodes[-1]
            self._nodes.append(tail)
            return True
        return False

    def eat_self(self):
        """咬自己"""
        for index in range(4, len(self._nodes)):
            node = self._nodes[index]
            if node.x == self.head.x and node.y == self.head.y:
                self._alive = False

    def draw(self, screen):
        for node in self._nodes:
            node.draw(screen)
def main():

    def refresh():
        """刷新游戏窗口"""
        screen.fill(Color.GRAY)
        wall.draw(screen)
        food.draw(screen)
        snake.draw(screen)
        pygame.display.flip()

    def handle_key_event(key_event):
        """处理按键事件"""
        key = key_event.key
        if key == pygame.K_F2:
            reset_game()
        elif key in (pygame.K_a, pygame.K_w, pygame.K_d, pygame.K_s):
            if snake.alive:
                if key == pygame.K_w:
                    new_dir = Direction.UP
                elif key == pygame.K_d:
                    new_dir = Direction.RIGHT
                elif key == pygame.K_s:
                    new_dir = Direction.DOWN
                else:
                    new_dir = Direction.LEFT
                snake.change_dir(new_dir)

    def create_food():
        """创建食物"""
        unit_size = snake.head.size
        max_row = wall.height // unit_size
        max_col = wall.width // unit_size
        row = randrange(0, max_row)
        col = randrange(0, max_col)
        return Food(wall.x + unit_size * col, wall.y + unit_size * row, unit_size)

    def reset_game():
        """重置游戏"""
        nonlocal food, snake
        food = create_food()
        snake = Snake(250, 290)

    def background_task():
        nonlocal running, food
        while running:
            if snake.alive:
                refresh()
            clock.tick(10)
            if snake.alive:
                snake.move()
                snake.collide(wall)
                if snake.eat_food(food):
                    food = create_food()
                snake.eat_self()
    """
    class BackgroundTask(Thread):
        def run(self):
            nonlocal running, food
            while running:
                if snake.alive:
                    refresh()
                clock.tick(10)
                if snake.alive:
                    snake.move()
                    snake.collide(wall)
                    if snake.eat_food(food):
                        food = create_food()
                    snake.eat_self()
    """
    wall = Wall(10, 10, 600, 600)
    snake = Snake(250, 290)
    food = create_food()
    pygame.init()
    screen = pygame.display.set_mode((620, 620))
    pygame.display.set_caption('贪吃蛇')
    # 创建控制游戏每秒帧数的时钟
    clock = pygame.time.Clock()
    running = True
    # 启动后台线程负责刷新窗口和让蛇移动
    # BackgroundTask().start()
    Thread(target=background_task).start()
    # 处理事件的消息循环
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                handle_key_event(event)
    pygame.quit()

if __name__ == '__main__':
    main()
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-11-cffe90e44a9e> in <module>
          4 from threading import Thread
          5 
    ----> 6 import pygame
          7 
          8 class Color(object):
    

    ModuleNotFoundError: No module named 'pygame'



```python
"""
用turtle模块绘图
"""
import turtle
turtle.pensize(3)
turtle.penup()
turtle.goto(-180, 150)
turtle.pencolor('red')
turtle.fillcolor('yellow')
turtle.pendown()
turtle.begin_fill()
for _ in range(36):
    turtle.forward(200)
    turtle.right(170)
turtle.end_fill()
turtle.mainloop()
```


```python

```
