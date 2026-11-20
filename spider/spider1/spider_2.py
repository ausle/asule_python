

import requests

url = 'https://www.baidu.com/s?wd=asule'
headers = {
    # 客户端的设备信息
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/158.0.0.0 Safari/537.36'
}
# GET请求
response = requests.get(url, headers=headers)
print(response)
print(response.text)


# POST请求
url1 = "https://fanyi.baidu.com/sug"
# s = input("请输入你要翻译的英文单词")
dat = {
    "kw": '啤酒'
}

# 发送 POST 请求，请求体
response1 = requests.post(url1, data=dat)
print(response1.json())


url2='https://m.douban.com/rexxar/api/v2/tv/recommend'

param = {
    "refresh": "0",
    "start": "0",
    "count": "20",
    "selected_categories": "xxx",
    "uncollect": "false",
    "score_range": "0,10",
    "tags": "",
    "ck": "jSIc",
}
headers1 = {
    # 客户端的设备信息
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/158.0.0.0 Safari/537.36'
}

response2 = requests.get(url2, params=param,headers=headers1)
# 响应码为418，表示可能触发了网站的反爬机制。需要排查请求的请求头信息
print(response2.request.headers)

print("状态码：", response2.status_code)
print("Content-Type：", response2.headers.get("Content-Type"))
print("响应内容：", repr(response2.text[:500]))
print(response2.json())

# 保持的连接需关闭掉
response2.close()









