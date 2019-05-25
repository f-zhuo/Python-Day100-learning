
# 进程和线程

   计算机进入多CPU或多核时代，操作系统也是支持“多任务”的操作系统，这使得我们可以同时运行多个程序，也可以将一个程序分解为若干个相对独立的子任务，让多个子任务并发的执行，从而缩短程序的执行时间，实现让程序同时执行多个任务，就是常说的“并发编程”
## 进程

   进程就是操作系统中执行的一个程序，操作系统以进程为单位分配存储空间，每个进程都有自己的地址空间、数据栈以及其他用于跟踪进程执行的辅助数据，操作系统管理所有进程的执行，为它们合理的分配资源。进程可以通过fork或spawn的方式来创建新的进程来执行其他的任务，不过新的进程也有自己独立的内存空间，因此必须通过进程间通信机制（IPC，Inter-Process Communication）来实现数据共享，具体的方式包括管道、信号、套接字、共享内存区等。
   一个进程还可以拥有多个并发的执行线索，简单的说就是拥有多个可以获得CPU调度的执行单元，这就是所谓的线程。由于线程在同一个进程下，它们可以共享相同的上下文，因此相对于进程而言，线程间的信息共享和通信更加容易。当然在单核CPU系统中，真正的并发是不可能的，因为在某个时刻能够获得CPU的只有唯一的一个线程，多个线程共享了CPU的执行时间。可以利用系统自带的进程监控工具（如macOS中的“活动监视器”、Windows中的“任务管理器”）来证实多线程多进程并发的优点。
   当然多线程也并不是没有坏处，站在其他进程的角度，多线程的程序对其他程序并不友好，因为它占用了更多的CPU执行时间，导致其他程序无法获得足够的CPU执行时间；另一方面，站在开发者的角度，编写和调试多线程的程序都对开发者有较高的要求，对于初学者来说更加困难。
   Python既支持多进程又支持多线程，因此使用Python实现并发编程主要有3种方式：多进程、多线程、多进程+多线程。
## Python中的多进程

   Unix和Linux操作系统上提供了fork()系统调用来创建进程，调用fork()函数的是父进程，创建出的是子进程，子进程是父进程的一个拷贝，但是子进程拥有自己的PID。fork()函数非常特殊它会返回两次，父进程中可以通过fork()函数的返回值得到子进程的PID，而子进程中的返回值永远都是0。Python的os模块提供了fork()函数。由于Windows系统没有fork()调用，因此要实现跨平台的多进程编程，可以使用multiprocessing模块的Process类来创建子进程，而且该模块还提供了更高级的封装，例如批量启动进程的进程池（Pool）、用于进程间通信的队列（Queue）和管道（Pipe）等。
   


```python
from random import randint
from time import time, sleep

def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))

def main():
    start = time()
    download_task('Python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))

if __name__ == '__main__':
    main()
```

    开始下载Python从入门到住院.pdf...
    Python从入门到住院.pdf下载完成! 耗费了9秒
    开始下载Peking Hot.avi...
    Peking Hot.avi下载完成! 耗费了8秒
    总共耗费了17.00秒.
    

   从上面的例子可以看出，如果程序中的代码只能按顺序一点点的往下执行，那么即使执行两个毫不相关的下载任务，
也需要先等待一个文件下载完成后才能开始下一个下载任务。接下来使用多进程的方式将两个下载任务放到不同的进程中。


```python
from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))

def main():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))

if __name__ == '__main__':
    main()
```

    总共耗费了1.37秒.
    

在上面的代码中，通过Process类创建了进程对象，通过target参数传入一个函数
来表示进程启动后要执行的代码，args是一个元组，它代表了传递给函数的参数。
Process对象的start方法用来启动进程，而join方法表示等待进程执行结束。
运行上面的代码可以明显发现两个下载任务“同时”启动了，下面是程序的一次执行结果。

启动下载进程，进程号[1530].
开始下载Python从入门到住院.pdf...
启动下载进程，进程号[1531].
开始下载Peking Hot.avi...
Peking Hot.avi下载完成! 耗费了7秒
Python从入门到住院.pdf下载完成! 耗费了10秒
总共耗费了10.01秒.

我们也可以使用subprocess模块中的类和函数来创建和启动子进程，然后通过管道来和子进程通信


```python
from multiprocessing import Process
from time import sleep

counter = 0
def sub_task(string):
    global counter
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)
        
def main():
    Process(target=sub_task, args=('Ping', )).start()
    Process(target=sub_task, args=('Pong', )).start()

if __name__ == '__main__':
    main()
```

# Python中的多线程




```python
from random import randint
from threading import Thread
from time import time, sleep

def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))

def main():
    start = time()
    t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('Peking Hot.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))

if __name__ == '__main__':
    main()
```

    开始下载Python从入门到住院.pdf...
    开始下载Peking Hot.avi...
    Peking Hot.avi下载完成! 耗费了7秒
    Python从入门到住院.pdf下载完成! 耗费了10秒
    总共耗费了10.010秒
    


```python
class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))

def main():
    start = time()
    t1 = DownloadTask('Python从入门到住院.pdf')
    t1.start()
    t2 = DownloadTask('Peking Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))

if __name__ == '__main__':
    main()
```

    开始下载Python从入门到住院.pdf...开始下载Peking Hot.avi...
    
    Python从入门到住院.pdf下载完成! 耗费了5秒
    Peking Hot.avi下载完成! 耗费了9秒
    总共耗费了9.01秒.
    

当多个线程共享同一个变量（我们通常称之为“资源”）的时候，很有可能产生不可控的结果从而导致程序失效甚至崩溃。如果一个资源被多个线程竞争使用，那么我们通常称之为“临界资源”，对“临界资源”的访问需要加上保护，否则资源会处于“混乱”的状态。


```python
from time import sleep
from threading import Thread

class Account(object):

    def __init__(self):
        self._balance = 0

    def deposit(self, money):
        # 计算存款后的余额
        new_balance = self._balance + money
        # 模拟受理存款业务需要0.01秒的时间
        sleep(0.01)
        # 修改账户余额
        self._balance = new_balance

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)

if __name__ == '__main__':
    main()
```

    账户余额为: ￥3元
    

运行上面的程序，100个线程分别向账户中转入1元钱，结果居然远远小于100元。之所以出现这种情况是因为我们没有对银行账户这个“临界资源”加以保护，多个线程同时向账户中存钱时，会一起执行到new_balance = self._balance + money 
这行代码，多个线程得到的账户余额都是初始状态下的0，所以都是0上面做了+1的操作，因此得到了错误的结果。可以通过“锁”来保护“临界资源”，只有获得“锁”的线程才能访问“临界资源”，而其他没有得到“锁”的线程只能被阻塞起来，直到获得“锁”的线程释放了“锁”，其他线程才有机会获得“锁”，进而访问被保护的“临界资源”。


```python
from time import sleep
from threading import Thread, Lock

class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)

if __name__ == '__main__':
    main()
```

    账户余额为: ￥100元
    

Python的解释器有一个“全局解释器锁”（GIL）的东西，任何线程执行前必须先获得GIL锁，然后每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行


```python
import time
import tkinter
import tkinter.messagebox

def download():
    # 模拟下载任务需要花费10秒钟时间
    time.sleep(10)
    tkinter.messagebox.showinfo('提示', '下载完成!')

def show_about():
    tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')

def main():
    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()

if __name__ == '__main__':
    main()
```


```python
import time
import tkinter
import tkinter.messagebox
from threading import Thread

def main():
    class DownloadTaskHandler(Thread):
        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('提示', '下载完成!')
            # 启用下载按钮
            button1.config(state=tkinter.NORMAL)

    def download():
        # 禁用下载按钮
        button1.config(state=tkinter.DISABLED)
        # 通过daemon参数将线程设置为守护线程(主程序退出就不再保留执行)
        # 在线程中处理耗时间的下载任务
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')

    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()

if __name__ == '__main__':
    main()
```


```python
from time import time

def main():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('Execution time: %.3fs' % (end - start))

if __name__ == '__main__':
    main()
```

    5000000050000000
    Execution time: 6.905s
    


```python
from multiprocessing import Process, Queue
from random import randint
from time import time

def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)

def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')

if __name__ == '__main__':
    main()
```


    ---------------------------------------------------------------------------

    BrokenPipeError                           Traceback (most recent call last)

    <ipython-input-12-c92b1ce55c69> in <module>
         34 
         35 if __name__ == '__main__':
    ---> 36     main()
    

    <ipython-input-12-c92b1ce55c69> in main()
         20         index += 12500000
         21         processes.append(p)
    ---> 22         p.start()
         23     # 开始记录所有进程执行完成花费的时间
         24     start = time()
    

    D:\Anaconda\lib\multiprocessing\process.py in start(self)
        110                'daemonic processes are not allowed to have children'
        111         _cleanup()
    --> 112         self._popen = self._Popen(self)
        113         self._sentinel = self._popen.sentinel
        114         # Avoid a refcycle if the target function holds an indirect
    

    D:\Anaconda\lib\multiprocessing\context.py in _Popen(process_obj)
        221     @staticmethod
        222     def _Popen(process_obj):
    --> 223         return _default_context.get_context().Process._Popen(process_obj)
        224 
        225 class DefaultContext(BaseContext):
    

    D:\Anaconda\lib\multiprocessing\context.py in _Popen(process_obj)
        320         def _Popen(process_obj):
        321             from .popen_spawn_win32 import Popen
    --> 322             return Popen(process_obj)
        323 
        324     class SpawnContext(BaseContext):
    

    D:\Anaconda\lib\multiprocessing\popen_spawn_win32.py in __init__(self, process_obj)
         87             try:
         88                 reduction.dump(prep_data, to_child)
    ---> 89                 reduction.dump(process_obj, to_child)
         90             finally:
         91                 set_spawning_popen(None)
    

    D:\Anaconda\lib\multiprocessing\reduction.py in dump(obj, file, protocol)
         58 def dump(obj, file, protocol=None):
         59     '''Replacement for pickle.dump() using ForkingPickler.'''
    ---> 60     ForkingPickler(file, protocol).dump(obj)
         61 
         62 #
    

    BrokenPipeError: [Errno 32] Broken pipe



```python
"""
异步I/O操作 - asyncio模块
"""
import asyncio
import threading
# import time

@asyncio.coroutine
def hello():
    print('%s: hello, world!' % threading.current_thread())
    # 休眠不会阻塞主线程因为使用了异步I/O操作
    # 注意有yield from才会等待休眠操作执行完成
    yield from asyncio.sleep(2)
    # asyncio.sleep(1)
    # time.sleep(1)
    print('%s: goodbye, world!' % threading.current_thread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 等待两个异步I/O操作执行结束
loop.run_until_complete(asyncio.wait(tasks))
print('game over!')
loop.close()
```


    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    <ipython-input-13-dad424025ecf> in <module>
         19 tasks = [hello(), hello()]
         20 # 等待两个异步I/O操作执行结束
    ---> 21 loop.run_until_complete(asyncio.wait(tasks))
         22 print('game over!')
         23 loop.close()
    

    D:\Anaconda\lib\asyncio\base_events.py in run_until_complete(self, future)
        569         future.add_done_callback(_run_until_complete_cb)
        570         try:
    --> 571             self.run_forever()
        572         except:
        573             if new_task and future.done() and not future.cancelled():
    

    D:\Anaconda\lib\asyncio\base_events.py in run_forever(self)
        524         self._check_closed()
        525         if self.is_running():
    --> 526             raise RuntimeError('This event loop is already running')
        527         if events._get_running_loop() is not None:
        528             raise RuntimeError(
    

    RuntimeError: This event loop is already running


    <_MainThread(MainThread, started 5780)>: hello, world!
    <_MainThread(MainThread, started 5780)>: hello, world!
    <_MainThread(MainThread, started 5780)>: goodbye, world!
    <_MainThread(MainThread, started 5780)>: goodbye, world!
    


```python
"""
异步I/O操作 - async和await
"""
import asyncio
import threading

# 通过async修饰的函数不再是普通函数而是一个协程
# 注意async和await将在Python 3.7中作为关键字出现
async def hello():
    print('%s: hello, world!' % threading.current_thread())
    await asyncio.sleep(2)
    print('%s: goodbye, world!' % threading.current_thread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 等待两个异步I/O操作执行结束
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
```


    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    <ipython-input-14-f52eca97b23b> in <module>
         15 tasks = [hello(), hello()]
         16 # 等待两个异步I/O操作执行结束
    ---> 17 loop.run_until_complete(asyncio.wait(tasks))
         18 loop.close()
    

    D:\Anaconda\lib\asyncio\base_events.py in run_until_complete(self, future)
        569         future.add_done_callback(_run_until_complete_cb)
        570         try:
    --> 571             self.run_forever()
        572         except:
        573             if new_task and future.done() and not future.cancelled():
    

    D:\Anaconda\lib\asyncio\base_events.py in run_forever(self)
        524         self._check_closed()
        525         if self.is_running():
    --> 526             raise RuntimeError('This event loop is already running')
        527         if events._get_running_loop() is not None:
        528             raise RuntimeError(
    

    RuntimeError: This event loop is already running


    <_MainThread(MainThread, started 5780)>: hello, world!
    <_MainThread(MainThread, started 5780)>: hello, world!
    <_MainThread(MainThread, started 5780)>: goodbye, world!
    <_MainThread(MainThread, started 5780)>: goodbye, world!
    


```python
"""
异步I/O操作 - asyncio模块
"""
import asyncio

async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    # 异步方式等待连接结果
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    # 异步I/O方式执行写操作
    await writer.drain()
    while True:
        # 异步I/O方式执行读操作
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
# 通过生成式语法创建一个装了三个协程的列表
hosts_list = ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']
tasks = [wget(host) for host in hosts_list]
# 下面的方法将异步I/O操作放入EventLoop直到执行完毕
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
```


    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    <ipython-input-15-8f2640a30e0d> in <module>
         26 tasks = [wget(host) for host in hosts_list]
         27 # 下面的方法将异步I/O操作放入EventLoop直到执行完毕
    ---> 28 loop.run_until_complete(asyncio.wait(tasks))
         29 loop.close()
    

    D:\Anaconda\lib\asyncio\base_events.py in run_until_complete(self, future)
        569         future.add_done_callback(_run_until_complete_cb)
        570         try:
    --> 571             self.run_forever()
        572         except:
        573             if new_task and future.done() and not future.cancelled():
    

    D:\Anaconda\lib\asyncio\base_events.py in run_forever(self)
        524         self._check_closed()
        525         if self.is_running():
    --> 526             raise RuntimeError('This event loop is already running')
        527         if events._get_running_loop() is not None:
        528             raise RuntimeError(
    

    RuntimeError: This event loop is already running


    wget www.sina.com.cn...
    wget www.sohu.com...
    wget www.163.com...
    www.sohu.com header > HTTP/1.1 200 OK
    www.sohu.com header > Content-Type: text/html;charset=UTF-8
    www.sohu.com header > Connection: close
    www.sohu.com header > Server: nginx
    www.sohu.com header > Date: Sat, 25 May 2019 14:04:09 GMT
    www.sohu.com header > Cache-Control: max-age=60
    www.sohu.com header > X-From-Sohu: X-SRC-Cached
    www.sohu.com header > Content-Encoding: gzip
    www.sohu.com header > FSS-Cache: HIT from 4140856.5844802.5915474
    www.sohu.com header > FSS-Proxy: Powered by 3878708.5320510.5653322
    www.sina.com.cn header > HTTP/1.1 302 Moved Temporarily
    www.sina.com.cn header > Server: nginx
    www.sina.com.cn header > Date: Sat, 25 May 2019 14:04:43 GMT
    www.sina.com.cn header > Content-Type: text/html
    www.sina.com.cn header > Content-Length: 154
    www.sina.com.cn header > Connection: close
    www.sina.com.cn header > Location: https://www.sina.com.cn/
    www.sina.com.cn header > X-Via-CDN: f=edge,s=ctc.wuhan.ha2ts4.39.nb.sinaedge.com,c=111.175.50.85;
    www.sina.com.cn header > X-Via-Edge: 15587930833255532af6f81e3313a53f89a17
    www.163.com header > HTTP/1.1 302 Moved Temporarily
    www.163.com header > Date: Sat, 25 May 2019 14:04:43 GMT
    www.163.com header > Content-Length: 0
    www.163.com header > Connection: close
    www.163.com header > Server: Cdn Cache Server V2.0
    www.163.com header > Location: http://www.163.com/special/0077jt/error_isp.html
    www.163.com header > X-Via: 1.0 PShbxgdx6lc87:14 (Cdn Cache Server V2.0)
    


```python
"""
使用协程 - 模拟快递中心派发快递
"""
from time import sleep
from random import random

def build_deliver_man(man_id):
    total = 0
    while True:
        total += 1
        print('%d号快递员准备接今天的第%d单.' % (man_id, total))
        pkg = yield
        print('%d号快递员收到编号为%s的包裹.' % (man_id, pkg))
        sleep(random() * 3)

def package_center(deliver_man, max_per_day):
    num = 1
    deliver_man.send(None)
    # next(deliver_man)
    while num <= max_per_day:
        package_id = 'PKG-%d' % num
        deliver_man.send(package_id)
        num += 1
        sleep(0.1)
    deliver_man.close()
    print('今天的包裹派送完毕!')

dm = build_deliver_man(1)
package_center(dm, 10)

```

    1号快递员准备接今天的第1单.
    1号快递员收到编号为PKG-1的包裹.
    1号快递员准备接今天的第2单.
    1号快递员收到编号为PKG-2的包裹.
    1号快递员准备接今天的第3单.
    1号快递员收到编号为PKG-3的包裹.
    1号快递员准备接今天的第4单.
    1号快递员收到编号为PKG-4的包裹.
    1号快递员准备接今天的第5单.
    1号快递员收到编号为PKG-5的包裹.
    1号快递员准备接今天的第6单.
    1号快递员收到编号为PKG-6的包裹.
    1号快递员准备接今天的第7单.
    1号快递员收到编号为PKG-7的包裹.
    1号快递员准备接今天的第8单.
    1号快递员收到编号为PKG-8的包裹.
    1号快递员准备接今天的第9单.
    1号快递员收到编号为PKG-9的包裹.
    1号快递员准备接今天的第10单.
    1号快递员收到编号为PKG-10的包裹.
    1号快递员准备接今天的第11单.
    今天的包裹派送完毕!
    


```python
"""
使用协程 - 查看协程的状态
"""
from time import sleep
from inspect import getgeneratorstate

def build_deliver_man(man_id):
    total = 0
    while True:
        total += 1
        print('%d号快递员准备接今天的第%d单.' % (man_id, total))
        pkg = yield
        print('%d号快递员收到编号为%s的包裹.' % (man_id, pkg))
        sleep(0.5)

def package_center(deliver_man, max_per_day):
    num = 1
    # 创建状态(GEN_CREATED) - 等待开始执行
    print(getgeneratorstate(deliver_man))
    deliver_man.send(None)
    # 挂起状态(GEN_SUSPENDED) - 在yield表达式处暂停
    print(getgeneratorstate(deliver_man))
    # next(deliver_man)
    while num <= max_per_day:
        package_id = 'PKG-%d' % num
        deliver_man.send(package_id)
        num += 1
    deliver_man.close()
    # 结束状态(GEN_CLOSED) - 执行完毕
    print(getgeneratorstate(deliver_man))
    print('包裹派送完毕!')

dm = build_deliver_man(1)
package_center(dm, 10)
```

    GEN_CREATED
    1号快递员准备接今天的第1单.
    GEN_SUSPENDED
    1号快递员收到编号为PKG-1的包裹.
    1号快递员准备接今天的第2单.
    1号快递员收到编号为PKG-2的包裹.
    1号快递员准备接今天的第3单.
    1号快递员收到编号为PKG-3的包裹.
    1号快递员准备接今天的第4单.
    1号快递员收到编号为PKG-4的包裹.
    1号快递员准备接今天的第5单.
    1号快递员收到编号为PKG-5的包裹.
    1号快递员准备接今天的第6单.
    1号快递员收到编号为PKG-6的包裹.
    1号快递员准备接今天的第7单.
    1号快递员收到编号为PKG-7的包裹.
    1号快递员准备接今天的第8单.
    1号快递员收到编号为PKG-8的包裹.
    1号快递员准备接今天的第9单.
    1号快递员收到编号为PKG-9的包裹.
    1号快递员准备接今天的第10单.
    1号快递员收到编号为PKG-10的包裹.
    1号快递员准备接今天的第11单.
    GEN_CLOSED
    包裹派送完毕!
    


```python
"""
生成器 - 生成器语法
"""
seq = [x * x for x in range(10)]
print(seq)

gen = (x * x for x in range(10))
print(gen)
for x in gen:
    print(x)

num = 10
gen = (x ** y for x, y in zip(range(1, num), range(num - 1, 0, -1)))
print(gen)
n = 1
while n < num:
    print(next(gen))
    n += 1
```

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    <generator object <genexpr> at 0x000001588486F570>
    0
    1
    4
    9
    16
    25
    36
    49
    64
    81
    <generator object <genexpr> at 0x000001588486F6D8>
    1
    256
    2187
    4096
    3125
    1296
    343
    64
    9
    


```python
"""
生成器 - 使用yield关键字
"""
def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n += 1

for x in fib(20):
    print(x)
```

    1
    1
    2
    3
    5
    8
    13
    21
    34
    55
    89
    144
    233
    377
    610
    987
    1597
    2584
    4181
    6765
    


```python
"""
使用Process类创建多个进程
"""
# 通过下面程序的执行结果可以证实 父进程在创建子进程时复制了进程及其数据结构
# 每个进程都有自己独立的内存空间 所以进程之间共享数据只能通过IPC的方式

from multiprocessing import Process, Queue
from time import sleep

def sub_task(string, q):
    number = q.get()
    while number:
        print('%d: %s' % (number, string))
        sleep(0.001)
        number = q.get()

def main():
    q = Queue(10)
    for number in range(1, 11):
        q.put(number)
    Process(target=sub_task, args=('Ping', q)).start()
    Process(target=sub_task, args=('Pong', q)).start()

if __name__ == '__main__':
    main()
```


```python
"""
实现进程间的通信
"""
import multiprocessing
import os

def sub_task(queue):
    print('子进程进程号:', os.getpid())
    counter = 0
    while counter < 1000:
        queue.put('Pong')
        counter += 1

if __name__ == '__main__':
    print('当前进程号:', os.getpid())
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=sub_task, args=(queue,))
    p.start()
    counter = 0
    while counter < 1000:
        queue.put('Ping')
        counter += 1
    p.join()
    print('子任务已经完成.')
    for _ in range(2000):
        print(queue.get(), end='')
```

    当前进程号: 9948
    子任务已经完成.
    PingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPingPing


```python
"""
创建进程调用其他程序
"""
import subprocess
import sys

def main():
    # 通过sys.argv获取命令行参数
    if len(sys.argv) > 1:
        # 第一个命令行参数是程序本身所以从第二个开始取
        for index in range(1, len(sys.argv)):
            try:
                # 通过subprocess模块的call函数启动子进程
                status = subprocess.call(sys.argv[index])
            except FileNotFoundError:
                print('不能执行%s命令' % sys.argv[index])
    else:
        print('请使用命令行参数指定要执行的进程')

if __name__ == '__main__':
    main()
```


```python
from time import time

def main():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('Execution time: %.3fs' % (end - start))

if __name__ == '__main__':
    main()
```


```python
"""
多个线程共享数据 - 没有锁的情况
"""
from time import sleep
from threading import Thread, Lock

class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 这段代码放在finally中保证释放锁的操作一定要执行
            self._lock.release()
    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕∫
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)

if __name__ == '__main__':
    main()
```


```python
"""
使用多线程的情况 - 模拟多个下载任务
"""
from random import randint
from time import time, sleep
import atexit
import _thread

def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    print('剩余时间%d秒.' % time_to_download)
    sleep(time_to_download)
    print('%s下载完成!' % filename)

def shutdown_hook(start):
    end = time()
    print('总共耗费了%.3f秒.' % (end - start))

def main():
    start = time()
    # 将多个下载任务放到多个线程中执行
    thread1 = _thread.start_new_thread(download_task, ('Python从入门到住院.pdf',))
    thread2 = _thread.start_new_thread(download_task, ('Peking Hot.avi',))
    # 注册关机钩子在程序执行结束前计算执行时间
    atexit.register(shutdown_hook, start)

if __name__ == '__main__':
    main()

```


```python
"""
使用多线程的情况 - 模拟多个下载任务
"""
from random import randint
from threading import Thread
from time import time, sleep

def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))

def main():
    start = time()
    thread1 = Thread(target=download_task, args=('Python从入门到住院.pdf',))
    thread1.start()
    thread2 = Thread(target=download_task, args=('Peking Hot.avi',))
    thread2.start()
    thread1.join()
    thread2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))

if __name__ == '__main__':
    main()
```


```python
"""
使用多线程的情况 - 模拟多个下载任务
"""
from random import randint
from time import time, sleep
import threading

class DownloadTask(threading.Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        print('剩余时间%d秒.' % time_to_download)
        sleep(time_to_download)
        print('%s下载完成!' % self._filename)

def main():
    start = time()
    # 将多个下载任务放到多个线程中执行
    # 通过自定义的线程类创建线程对象 线程启动后会回调执行run方法
    thread1 = DownloadTask('Python从入门到住院.pdf')
    thread1.start()
    thread2 = DownloadTask('Peking Hot.avi')
    thread2.start()
    thread1.join()
    thread2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))

if __name__ == '__main__':
    main()

# 请注意通过threading.Thread创建的线程默认是非守护线程
```


```python
"""
多个线程共享数据 - 有锁的情况
"""
import time
import threading

class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = threading.Lock()

    def deposit(self, money):
        # 获得锁后代码才能继续执行
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            time.sleep(0.01)
            self._balance = new_balance
        finally:
            # 操作完成后一定要记着释放锁
            self._lock.release()
    @property
    def balance(self):
        return self._balance

if __name__ == '__main__':
    account = Account()
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        threading.Thread(target=account.deposit, args=(1,)).start()
    # 等所有存款的线程都执行完毕
    time.sleep(2)
    print('账户余额为: ￥%d元' % account.balance)

# 结果不是我们期望的100元
```


```python
"""
不使用多线程的情况 - 模拟多个下载任务
"""
from random import randint
from time import time, sleep

def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('下载完成! 耗费了%d秒' % time_to_download)

def main():
    start = time()
    download_task('Python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))

if __name__ == '__main__':
    main()
```


```python
"""
不使用多线程的情况 - 耗时间的任务阻塞主事件循环
"""
import time
import tkinter
import tkinter.messagebox

def download():
    # 模拟下载任务需要花费10秒钟时间
    time.sleep(10)
    tkinter.messagebox.showinfo('提示', '下载完成!')

def show_about():
    tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')

def main():
    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()

if __name__ == '__main__':
    main()

# 在不使用多线程的情况下 一旦点击下载按钮 由于该操作需要花费10秒中的时间
# 整个主消息循环也会被阻塞10秒钟无法响应其他的事件
# 事实上 对于没有因果关系的子任务 这种顺序执行的方式并不合理
```


```python
import time
from threading import Thread, Lock

class Account(object):

    def __init__(self, balance=0):
        self._balance = balance
        self._lock = Lock()
    @property
    def balance(self):
        return self._balance

    def deposit(self, money):
        # 当多个线程同时访问一个资源的时候 就有可能因为竞争资源导致资源的状态错误
        # 被多个线程访问的资源我们通常称之为临界资源 对临界资源的访问需要加上保护
        if money > 0:
            self._lock.acquire()
            try:
                new_balance = self._balance + money
                time.sleep(0.01)
                self._balance = new_balance
            finally:
                self._lock.release()

class AddMoneyThread(Thread):

    def __init__(self, account):
        super().__init__()
        self._account = account

    def run(self):
        self._account.deposit(1)

def main():
    account = Account(1000)
    tlist = []
    for _ in range(100):
        t = AddMoneyThread(account)
        tlist.append(t)
        t.start()
    for t in tlist:
        t.join()
    print('账户余额: %d元' % account.balance)

if __name__ == '__main__':
    main()
```


```python
from random import randint
from threading import Thread
from time import sleep

import pygame

class Color(object):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return r, g, b

class Car(object):

    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    def move(self):
        if self._x + 80 < 950:
            self._x += randint(1, 10)

    def draw(self, screen):
        pygame.draw.rect(screen, self._color,
                         (self._x, self._y, 80, 40), 0)

def main():

    class BackgroundTask(Thread):

        def run(self):
            while True:
                screen.fill(Color.GRAY)
                pygame.draw.line(screen, Color.BLACK, (130, 0), (130, 600), 4)
                pygame.draw.line(screen, Color.BLACK, (950, 0), (950, 600), 4)
                for car in cars:
                    car.draw(screen)
                pygame.display.flip()
                sleep(0.05)
                for car in cars:
                    car.move()

    cars = []
    for index in range(5):
        temp = Car(50, 50 + 120 * index, Color.random_color())
        cars.append(temp)
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    BackgroundTask(daemon=True).start()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == '__main__':
    main()
```


```python

```
