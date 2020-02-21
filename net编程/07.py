#导入相关的包
import smtplib
from email.mime.text import MIMEText
mail_content="""
       <!DOCTYPE html>
       <html lang="en">
       <head>
           <meta  charset="UTF-8">
           <title>Title</title>
       </head>
       <body>
       <h1>这是一封python邮件</h1>
       
       </body>
       </html>
"""
#MIMEText三个主要参数
#1.邮件内容
#2.MIME子类型，在此案例中我们使用plain表示text类型
#3.邮件编码格式
msg = MIMEText(mail_content,"html","utf-8")
#发送email地址，此处地址为qq邮箱
from_aadr = "1789353033@qq.com"
#授权码
from_pwd = "pfppgamsqjqabehf"

#收件人信息
to_addr = "1789353033@qq.com"


#输入SMTP服务器地址
#此处根据不同的邮件服务商有不同的值
#现在基本任何一家邮件服务商，如果采用第三方收发邮件，需要开启授权选项
#腾讯qq邮箱的SMTP地址是 smtp.qq.com

smtp_srv = "smtp.qq.com"


#此处使用异常是害怕代码出现异常

try:
    #两个参数
    #第一个是服务器地址，但一定是bytes格式，所以要编码
    #第二个参数是服务器接收访问端口
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)
    #登录邮箱发送
    srv.login(from_aadr,from_pwd)
    #发送邮箱
    #三个参数
    #1.发送地址
    #2.接受地址，必须是list形式
    #3.发送内容，作为字符串发送
    srv.sendmail(from_aadr,[to_addr],msg.as_string())
    srv.quit()
except Exception as e:
    print(e)
