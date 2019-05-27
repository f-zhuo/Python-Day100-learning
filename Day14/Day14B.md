
# 网络应用开发



```python
'''发送邮件'''
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = '123456@126.com'
    receivers = ['ffffff@qq.com', 'hhhhh@163.com']
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = Header('王大锤', 'utf-8')
    message['To'] = Header('骆昊', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.126.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, '2333333')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')

if __name__ == '__main__':
    main()
```


    ---------------------------------------------------------------------------

    SMTPAuthenticationError                   Traceback (most recent call last)

    <ipython-input-2-6ffc2b79af54> in <module>
         18 
         19 if __name__ == '__main__':
    ---> 20     main()
    

    <ipython-input-2-6ffc2b79af54> in main()
         13     smtper = SMTP('smtp.126.com')
         14     # 请自行修改下面的登录口令
    ---> 15     smtper.login(sender, 'zf960504')
         16     smtper.sendmail(sender, receivers, message.as_string())
         17     print('邮件发送完成!')
    

    D:\Anaconda\lib\smtplib.py in login(self, user, password, initial_response_ok)
        728 
        729         # We could not login successfully.  Return result of last attempt.
    --> 730         raise last_exception
        731 
        732     def starttls(self, keyfile=None, certfile=None, context=None):
    

    D:\Anaconda\lib\smtplib.py in login(self, user, password, initial_response_ok)
        719                 (code, resp) = self.auth(
        720                     authmethod, getattr(self, method_name),
    --> 721                     initial_response_ok=initial_response_ok)
        722                 # 235 == 'Authentication successful'
        723                 # 503 == 'Error: already authenticated'
    

    D:\Anaconda\lib\smtplib.py in auth(self, mechanism, authobject, initial_response_ok)
        640         if code in (235, 503):
        641             return (code, resp)
    --> 642         raise SMTPAuthenticationError(code, resp)
        643 
        644     def auth_cram_md5(self, challenge=None):
    

    SMTPAuthenticationError: (550, b'\xd3\xc3\xbb\xa7\xce\xde\xc8\xa8\xb5\xc7\xc2\xbd')



```python
'''发送带有附件的邮件'''
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import urllib

def main():
    # 创建一个带附件的邮件消息对象
    message = MIMEMultipart()
    
    # 创建文本内容
    text_content = MIMEText('附件中有本月数据请查收', 'plain', 'utf-8')
    message['Subject'] = Header('本月数据', 'utf-8')
    # 将文本内容添加到邮件消息对象中
    message.attach(text_content)

    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('/Users/Hao/Desktop/hello.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=hello.txt'
        message.attach(txt)
    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('/Users/Hao/Desktop/汇总数据.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        xls['Content-Type'] = 'application/vnd.ms-excel'
        xls['Content-Disposition'] = 'attachment; filename=month-data.xlsx'
        message.attach(xls)
    
    # 创建SMTP对象
    smtper = SMTP('smtp.126.com')
    # 开启安全连接
    # smtper.starttls()
    sender = 'abcdefg@126.com'
    receivers = ['uvwxyz@qq.com']
    # 登录到SMTP服务器
    # 请注意此处不是使用密码而是邮件客户端授权码进行登录
    # 对此有疑问的读者可以联系自己使用的邮件服务器客服
    smtper.login(sender, 'secretpass')
    # 发送邮件
    smtper.sendmail(sender, receivers, message.as_string())
    # 与邮件服务器断开连接
    smtper.quit()
    print('发送完成!')

if __name__ == '__main__':
    main()
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-3-518f7b8f3a8e> in <module>
         47 
         48 if __name__ == '__main__':
    ---> 49     main()
    

    <ipython-input-3-518f7b8f3a8e> in main()
         18 
         19     # 读取文件并将文件作为附件添加到邮件消息对象中
    ---> 20     with open('/Users/Hao/Desktop/hello.txt', 'rb') as f:
         21         txt = MIMEText(f.read(), 'base64', 'utf-8')
         22         txt['Content-Type'] = 'text/plain'
    

    FileNotFoundError: [Errno 2] No such file or directory: '/Users/Hao/Desktop/hello.txt'



```python
'''发送短信'''
import urllib.parse
import http.client
import json

def main():
    host  = "106.ihuyi.com"
    sms_send_uri = "/webservice/sms.php?method=Submit"
    # 下面的参数需要填入自己注册的账号和对应的密码
    params = urllib.parse.urlencode({'account': '你自己的账号', 'password' : '你自己的密码', \
                                     'content': '您的验证码是：147258。请不要把验证码泄露给其他人。',\
                                     'mobile': '接收者的手机号', 'format':'json' })
    print(params)
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    conn.close()

if __name__ == '__main__':
    main()
```

    account=%E4%BD%A0%E8%87%AA%E5%B7%B1%E7%9A%84%E8%B4%A6%E5%8F%B7&password=%E4%BD%A0%E8%87%AA%E5%B7%B1%E7%9A%84%E5%AF%86%E7%A0%81&content=%E6%82%A8%E7%9A%84%E9%AA%8C%E8%AF%81%E7%A0%81%E6%98%AF%EF%BC%9A147258%E3%80%82%E8%AF%B7%E4%B8%8D%E8%A6%81%E6%8A%8A%E9%AA%8C%E8%AF%81%E7%A0%81%E6%B3%84%E9%9C%B2%E7%BB%99%E5%85%B6%E4%BB%96%E4%BA%BA%E3%80%82&mobile=%E6%8E%A5%E6%94%B6%E8%80%85%E7%9A%84%E6%89%8B%E6%9C%BA%E5%8F%B7&format=json
    {'code': 405, 'msg': '用户名或密码不正确', 'smsid': '0'}
    


```python

```
