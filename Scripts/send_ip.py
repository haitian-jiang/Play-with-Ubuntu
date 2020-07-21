#!/usr/bin/env python3

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

import os
import time


def get_ip():
    process = os.popen('curl http://members.3322.org/dyndns/getip')
    output = process.read()
    process.close()
    return output


def send_mail(ip):
    #qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    #sender_qq为发件人的qq号码
    sender_qq = '111111111@qq.com'
    #pwd为qq邮箱的授权码
    pwd = 'hm************ed'
    #发件人的邮箱
    sender_qq_mail = '1111111111@qq.com'
    #收件人邮箱
    receiver = 'example@exam.com'
    
    #邮件的正文内容
    str_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    mail_content = ip + str_time
    #邮件标题
    mail_title = 'ip地址'
    
    #ssl登录
    smtp = SMTP_SSL(host_server)
    #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)
    
    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()


def main():
    ip = ''
    while True:
        new_ip = get_ip()
        with open("ip.log","a") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            f.write('--'+new_ip)
        if new_ip != ip:
            send_mail(new_ip)
            ip = new_ip
        time.sleep(1200) # 20分钟查一次


if __name__ == '__main__':
    main()

