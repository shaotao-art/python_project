import requests
from lxml import html
import datetime
#发现的新思路
#可以先把图片的包抓到  再到网页源代码中找是否有相关信息
'''
爬取bing搜索每日图片
'''
class spider:
    #headers
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}


    def request_info(self, url):
        r = requests.get(url, headers=self.headers)
        return r.text

    def serch(self,r_text):
        tree=html.fromstring(r_text)
        url= 'https://www.bing.com' + str(tree.xpath('//@data-ultra-definition-src')[0])
        return url

    def download(self,url):
        name=str(datetime.date.today())+'.jpg'
        img= requests.get(url, headers=self.headers)
        with open(name,'wb')as f:
            f.write(img.content)
        print('done')


bing_spider=spider()
r_text=bing_spider.request_info('https://cn.bing.com/?')
url=bing_spider.serch(r_text)
bing_spider.download(url)
