import smtplib
from email.mime.text import MIMEText

import requests
from bs4 import BeautifulSoup

# 抓取教务处新闻列表
def get_news_list():
    # 抓取网页内容
    url = "http://jwc.scu.edu.cn"
    html = requests.get(url)
    html.encoding = 'utf-8'
    # print(html.text)
    web_source = BeautifulSoup(html.text, 'html.parser')
    # 获取新闻列表
    news_list = web_source.select('.list-llb-list')

    # 遍历新闻内容，进一步分析title，url，date
    real_news_list = []
    for index, news in enumerate(news_list):
        a = news.find("a")
        # <a href="" target="" title=“”>
        #       <span...
        #       <em...
        # </a>
        href = url + "/" + a["href"]
        title = a["title"]
        date = a.select(".list-date-a")[0].get_text()

        real_news_list.append((href, title, date))

        # print("{}: 地址：{} 标题：{} 日期：{}"
        #       .format(index + 1, href, title, date))
    return real_news_list

# 邮件发送第一条新闻
def send_email(message_body, receiver):
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = config.get_key("receiver")  # 用户名
    mail_pass = config.get_key("mailToken")  # 口令
    sender = config.get_key("receiver")
    message = MIMEText(message_body, 'plain', 'utf-8')
    message['From'] = "43471492@qq.com"
    message['To'] = receiver
    message['Subject'] = "微服务自助打卡邮件通知"
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receiver, message.as_string())
        print("邮件发送成功")
        smtpObj.quit()
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

# 短信发送第一条新闻
# 微信发送第一条新闻