
# 网络编程


```python
from socket import socket
from threading import Thread

def main():

    class RefreshScreenThread(Thread):

        def __init__(self, client):
            super().__init__()
            self._client = client

        def run(self):
            while running:
                data = self._client.recv(1024)
                print(data.decode('utf-8'))

    nickname = input('请输入你的昵称: ')
    myclient = socket()
    myclient.connect(('10.7.189.118', 12345))
    running = True
    RefreshScreenThread(myclient).start()
    while running:
        content = input('请发言: ')
        if content == 'byebye':
            myclient.send(content.encode('utf-8'))
            running = False
        else:
            msg = nickname + ': ' + content
            myclient.send(msg.encode('utf-8'))

if __name__ == '__main__':
    main()
    
```

    请输入你的昵称: 陈独秀
    


    ---------------------------------------------------------------------------

    TimeoutError                              Traceback (most recent call last)

    <ipython-input-2-391cef779631> in <module>
         30 
         31 if __name__ == '__main__':
    ---> 32     main()
         33 
         34 
    

    <ipython-input-2-391cef779631> in main()
         17     nickname = input('请输入你的昵称: ')
         18     myclient = socket()
    ---> 19     myclient.connect(('10.7.189.118', 12345))
         20     running = True
         21     RefreshScreenThread(myclient).start()
    

    TimeoutError: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。



```python
from socket import socket
from threading import Thread

def main():

    class ClientHandler(Thread):

        def __init__(self, client):
            super().__init__()
            self._client = client

        def run(self):
            try:
                while True:
                    try:
                        data = self._client.recv(1024)
                        if data.decode('utf-8') == 'byebye':
                            clients.remove(self._client)
                            self._client.close()
                            break
                        else:
                            for client in clients:
                                client.send(data)
                    except Exception as e:
                        print(e)
                        clients.remove(self._client)
                        break
            except Exception as e:
                print(e)

    server = socket()
    server.bind(('10.7.189.118', 12345))
    server.listen(512)
    clients = []
    while True:
        curr_client, addr = server.accept()
        print(addr[0], '连接到服务器.')
        clients.append(curr_client)
        ClientHandler(curr_client).start()

if __name__ == '__main__':
    main()
```


    ---------------------------------------------------------------------------

    OSError                                   Traceback (most recent call last)

    <ipython-input-3-597b793a0719> in <module>
         40 
         41 if __name__ == '__main__':
    ---> 42     main()
    

    <ipython-input-3-597b793a0719> in main()
         30 
         31     server = socket()
    ---> 32     server.bind(('10.7.189.118', 12345))
         33     server.listen(512)
         34     clients = []
    

    OSError: [WinError 10049] 在其上下文中，该请求的地址无效。



```python
from socket import socket
from json import loads
from base64 import b64decode

def main():
    client = socket()
    client.connect(('192.168.1.2', 5566))
    # 定义一个保存二进制数据的对象
    in_data = bytes()
    # 由于不知道服务器发送的数据有多大每次接收1024字节
    data = client.recv(1024)
    while data:
        # 将收到的数据拼接起来
        in_data += data
        data = client.recv(1024)
    # 将收到的二进制数据解码成JSON字符串并转换成字典
    # loads函数的作用就是将JSON字符串转成字典对象
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('/Users/Hao/' + filename, 'wb') as f:
        # 将base64格式的数据解码成二进制数据并写入文件
        f.write(b64decode(filedata))
    print('图片已保存.')

if __name__ == '__main__':
    main()
```


    ---------------------------------------------------------------------------

    TimeoutError                              Traceback (most recent call last)

    <ipython-input-4-7ff7e93ad3f7> in <module>
         25 
         26 if __name__ == '__main__':
    ---> 27     main()
    

    <ipython-input-4-7ff7e93ad3f7> in main()
          5 def main():
          6     client = socket()
    ----> 7     client.connect(('192.168.1.2', 5566))
          8     # 定义一个保存二进制数据的对象
          9     in_data = bytes()
    

    TimeoutError: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。



```python
from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread

def main():

    # 自定义线程类
    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'guido.jpg'
            # JSON是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成base64编码
            my_dict['filedata'] = data
            # 通过dumps函数将字典处理成JSON字符串
            json_str = dumps(my_dict)
            # 发送JSON字符串
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    # 1.创建套接字对象并指定使用哪种传输服务
    server = socket()
    # 2.绑定IP地址和端口(区分不同的服务)
    server.bind(('192.168.1.2', 5566))
    # 3.开启监听 - 监听客户端连接到服务器
    server.listen(512)
    
    print('服务器启动开始监听...')
    with open('guido.jpg', 'rb') as f:
        # 将二进制数据处理成base64再解码成字符串
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        # 用一个字典(键值对)来保存要发送的各种数据
        # 待会可以将字典处理成JSON格式在网络上传递
        FileTransferHandler(client).start()

if __name__ == '__main__':
    main()
```


    ---------------------------------------------------------------------------

    OSError                                   Traceback (most recent call last)

    <ipython-input-5-c6b2ccd808a6> in <module>
         43 
         44 if __name__ == '__main__':
    ---> 45     main()
    

    <ipython-input-5-c6b2ccd808a6> in main()
         28     server = socket()
         29     # 2.绑定IP地址和端口(区分不同的服务)
    ---> 30     server.bind(('192.168.1.2', 5566))
         31     # 3.开启监听 - 监听客户端连接到服务器
         32     server.listen(512)
    

    OSError: [WinError 10049] 在其上下文中，该请求的地址无效。



```python
from time import time
from threading import Thread

import requests
class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/Users/Hao/Downloads/' + filename, 'wb') as f:
            f.write(resp.content)

def main():
    # 通过requests模块的get函数获取网络资源
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=772a81a51ae5c780251b1f98ea431b84&num=10')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # 通过多线程的方式实现图片下载
        DownloadHanlder(url).start()

if __name__ == '__main__':
    main()
```

    Exception in thread Thread-9:
    Traceback (most recent call last):
      File "D:\Anaconda\lib\threading.py", line 917, in _bootstrap_inner
        self.run()
      File "<ipython-input-6-faebad183678>", line 14, in run
        with open('/Users/Hao/Downloads/' + filename, 'wb') as f:
    FileNotFoundError: [Errno 2] No such file or directory: '/Users/Hao/Downloads/fd17485260.jpg'
    
    Exception in thread Thread-14:
    Traceback (most recent call last):
      File "D:\Anaconda\lib\threading.py", line 917, in _bootstrap_inner
        self.run()
      File "<ipython-input-6-faebad183678>", line 14, in run
        with open('/Users/Hao/Downloads/' + filename, 'wb') as f:
    FileNotFoundError: [Errno 2] No such file or directory: '/Users/Hao/Downloads/1.jpg'
    
    Exception in thread Thread-13:
    Traceback (most recent call last):
      File "D:\Anaconda\lib\threading.py", line 917, in _bootstrap_inner
        self.run()
      File "<ipython-input-6-faebad183678>", line 14, in run
        with open('/Users/Hao/Downloads/' + filename, 'wb') as f:
    FileNotFoundError: [Errno 2] No such file or directory: '/Users/Hao/Downloads/1-1Z4261A924.jpg'
    
    Exception in thread Thread-8:
    Traceback (most recent call last):
      File "D:\Anaconda\lib\threading.py", line 917, in _bootstrap_inner
        self.run()
      File "<ipython-input-6-faebad183678>", line 14, in run
        with open('/Users/Hao/Downloads/' + filename, 'wb') as f:
    FileNotFoundError: [Errno 2] No such file or directory: '/Users/Hao/Downloads/e37839255d.jpg'
    
    Exception in thread Thread-11:
    Traceback (most recent call last):
      File "D:\Anaconda\lib\threading.py", line 917, in _bootstrap_inner
        self.run()
      File "<ipython-input-6-faebad183678>", line 14, in run
        with open('/Users/Hao/Downloads/' + filename, 'wb') as f:
    FileNotFoundError: [Errno 2] No such file or directory: '/Users/Hao/Downloads/fda4c055b8.jpg'
    
    Exception in thread Thread-10:
    Traceback (most recent call last):
      File "D:\Anaconda\lib\threading.py", line 917, in _bootstrap_inner
        self.run()
      File "<ipython-input-6-faebad183678>", line 14, in run
        with open('/Users/Hao/Downloads/' + filename, 'wb') as f:
    FileNotFoundError: [Errno 2] No such file or directory: '/Users/Hao/Downloads/3d136b6c34.jpg'
    
    Exception in thread Thread-6:
    Traceback (most recent call last):
      File "D:\Anaconda\lib\threading.py", line 917, in _bootstrap_inner
        self.run()
      File "<ipython-input-6-faebad183678>", line 14, in run
        with open('/Users/Hao/Downloads/' + filename, 'wb') as f:
    FileNotFoundError: [Errno 2] No such file or directory: '/Users/Hao/Downloads/57143cb224.jpg'
    
    Exception in thread Thread-12:
    Traceback (most recent call last):
      File "D:\Anaconda\lib\threading.py", line 917, in _bootstrap_inner
        self.run()
      File "<ipython-input-6-faebad183678>", line 14, in run
        with open('/Users/Hao/Downloads/' + filename, 'wb') as f:
    FileNotFoundError: [Errno 2] No such file or directory: '/Users/Hao/Downloads/04d7b0ffbe.jpg'
    
    Exception in thread Thread-15:
    Traceback (most recent call last):
      File "D:\Anaconda\lib\threading.py", line 917, in _bootstrap_inner
        self.run()
      File "<ipython-input-6-faebad183678>", line 14, in run
        with open('/Users/Hao/Downloads/' + filename, 'wb') as f:
    FileNotFoundError: [Errno 2] No such file or directory: '/Users/Hao/Downloads/1-1Z514014I7.jpg'
    
    Exception in thread Thread-7:
    Traceback (most recent call last):
      File "D:\Anaconda\lib\threading.py", line 917, in _bootstrap_inner
        self.run()
      File "<ipython-input-6-faebad183678>", line 14, in run
        with open('/Users/Hao/Downloads/' + filename, 'wb') as f:
    FileNotFoundError: [Errno 2] No such file or directory: '/Users/Hao/Downloads/df2f8973d5.jpg'
    
    


```python
"""
套接字 - 基于TCP协议创建时间服务器
"""
from socket import *
from time import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 6789))
server.listen()
print('服务器已经启动正在监听客户端连接.')
while True:
    client, addr = server.accept()
    print('客户端%s:%d连接成功.' % (addr[0], addr[1]))
    currtime = localtime(time())
    timestr = strftime('%Y-%m-%d %H:%M:%S', currtime)
    client.send(timestr.encode('utf-8'))
    client.close()
server.close()
```

    服务器已经启动正在监听客户端连接.
    


```python
"""
套接字 - 基于TCP协议创建时间客户端
"""
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 6789))
while True:
    data = client.recv(1024)
    if not data:
        break
    print(data.decode('utf-8'))
client.close()
```


```python
"""
套接字 - 基于UDP协议Echo服务器
"""
from socket import *
from time import *

server = socket(AF_INET, SOCK_DGRAM)
server.bind(('localhost', 6789))
while True:
    data, addr = server.recvfrom(1024)
    server.sendto(data, addr)
server.close()
```


```python
"""
套接字 - 基于UDP协议创建Echo客户端
"""
from socket import *

client = socket(AF_INET, SOCK_DGRAM)
while True:
    data_str = input('请输入: ')
    client.sendto(data_str.encode('utf-8'), ('localhost', 6789))
    data, addr = client.recvfrom(1024)
    data_str = data.decode('utf-8')
    print('服务器回应:', data_str)
    if data_str == 'bye':
        break
client.close()
```


```python
"""
使用socketserver模块创建时间服务器
"""
from socketserver import TCPServer, StreamRequestHandler
from time import *

class EchoRequestHandler(StreamRequestHandler):

    def handle(self):
        currtime = localtime(time())
        timestr = strftime('%Y-%m-%d %H:%M:%S', currtime)
        self.wfile.write(timestr.encode('utf-8'))

server = TCPServer(('localhost', 6789), EchoRequestHandler)
server.serve_forever()
```


```python
from socket import socket

def main():
    client = socket()
    client.connect(('10.7.152.69', 6789))
    print(client.recv(1024).decode('utf-8'))
    client.close()

if __name__ == '__main__':
    main()
```


```python
from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def main():
    # 1.创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2.绑定IP地址和端口(区分不同的服务)
    server.bind(('192.168.1.2', 6789))
    # 3.开启监听 - 监听客户端连接到服务器
    server.listen(512)
    print('服务器启动开始监听...')
    # 4.通过循环接收客户端的连接并作出相应的处理(提供服务)
    while True:
        # accept方法是一个阻塞方法如果没有客户端连接到服务器
        # 这个方法就会阻塞代码不会向下执行
        # accept方法返回元组其中的第一个元素是客户端对象
        # 第二个元素是客户端的地址(由IP和端口两部分构成)
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器.')
        # 5.发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        # 6.断开连接
        client.close()

if __name__ == '__main__':
    main()
```


```python

```
