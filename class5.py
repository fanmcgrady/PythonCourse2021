import requests

def send_wechat(message):
    """推送信息到微信"""
    url = 'http://sc.ftqq.com/{}.send'.format("SCT68294TUpr7ItuTn2jNCvEUrnuFSzhq")
    payload = {
        "text":'抢购结果',
        "desp": message
    }
    requests.get(url, params=payload)

if __name__ == '__main__':
    send_wechat("你好")
