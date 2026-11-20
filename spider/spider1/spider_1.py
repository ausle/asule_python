
#
from urllib.request import urlopen

url = 'https://www.baidu.com/'
# 访问百度，获取服务器响应的内容，即是：网页的源代码。
html = urlopen(url)

# 将服务器响应的内容保存到某个文件
with open('baidu.html', 'w',encoding='utf-8') as f:
    f.write(html.read().decode('utf-8'))

print('exit')












