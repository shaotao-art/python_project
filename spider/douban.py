from lxml import html
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
url = 'https://movie.douban.com/top250?start=225&filter='
while True:
    r = requests.get(url, headers=headers)
    tree = html.fromstring(r.text)
    names = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
    infos = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[1]/text()')
    detail_urls = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/@href')
    for each in detail_urls:
        time.sleep(1)
        intro_r = requests.get(each, headers=headers)
        intro_tree = html.fromstring(intro_r.text)
        intros = intro_tree.xpath('//span[@property="v:summary"]/text()')
    next_page = 'https://movie.douban.com/top250' + str(
        tree.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href')[0])
    try:
        if next_page:
            url = next_page
    except IndexError as e:
        print(e)
        print('done')
