import requests
from lxml import html

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
url = 'https://movie.douban.com/top250'
r = requests.get(url, headers=headers)
tree = html.fromstring(r.text)
# copy的xpath
# quotes_a=[]
# quotes_a.append(tree.xpath('//*[@id="content"]/div/div[1]/ol//li/div/div[2]/div[2]/p[2]/span/text()'))
# print(quotes_a)
# 自己写的xpath
quotes_b = []
quotes_b.append(tree.xpath('//span[@class="inq"]/text()'))
print(quotes_b)
