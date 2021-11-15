import smtplib
from email.mime.text import MIMEText

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

import requests
from bs4 import BeautifulSoup

from spider.readconfig import ReadConfig

config = ReadConfig()


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
def send_email(message, receiver):
    # 设置发件信息
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = config.get_value('email')  # 用户名
    mail_pass = config.get_value('passwd')  # 口令
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    smtpObj.login(mail_user, mail_pass)

    # 设置邮件内容
    sender = config.get_value('email')
    mimeText = MIMEText(message, 'plain', 'utf-8')
    mimeText['From'] = sender
    mimeText['To'] = receiver
    mimeText['Subject'] = "Python课程测试邮件"

    # 发送
    smtpObj.sendmail(sender, receiver, mimeText.as_string())
    print("邮件发送成功")
    smtpObj.quit()


# 短信发送第一条新闻
# 阿里云，腾讯云
def send_msg(title, url):
    """推送信息到短信"""
    # 模版内容:
    # ${name}您好，教务处网站${content}发布了新通知公告，标题为："${newsName}"。（地址：http://jwc.scu.edu.cn/${url}）
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', 15882307807)
    request.add_query_param('SignName', "四川大学网络空间安全学院")
    request.add_query_param('TemplateCode', "SMS_183760754")
    payload = {
        'name': '朱同学',
        'newsName': title,
        'url': url
    }
    request.add_query_param('TemplateParam', payload)

    client = AcsClient(config.get_value("key"),
                       config.get_value("secret"), 'cn-hangzhou')
    response = client.do_action(request)
    print(str(response, encoding='utf-8'))


# 微信发送第一条新闻
# http://sct.ftqq.com
def send_wechat(message):
    """推送信息到微信"""
    url = "http://sc.ftqq.com/{}.send"\
        .format(config.get_value('sckey'))

    payload = {
        'text': 'Python课程测试',
        'desp': message
    }

    requests.get(url, params=payload)


if __name__ == '__main__':
    # newslist = get_news_list()
    # send_email(str(newslist[0]), "43471492@qq.com")
    # send_wechat(str(newslist[0]))
    # url, title, date = newslist[0]
    # send_msg(title[:5], url[:5])
    send_email("hello", "43471492@qq.com")