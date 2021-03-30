from lxml import html
import requests
from bs4 import BeautifulSoup as bs
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
url = 'http://mobile.zol.com.cn/detail_13432/'
while True:
    time.sleep(1)
    r = requests.get(url, headers=headers)
    soup = bs(r.text)
    infos = soup.find_all('div', class_='info-head')
    titles = []
    urls = []
    for each in infos:
        titles.append(each.get_text(strip=True))
        urls.append('http:' + str(each.a['href']))
    print([titles, urls])
    for each_passage in urls:
        passage_r = requests.get(each_passage, headers=headers)
        tree = html.fromstring(passage_r.text)
        pragras = tree.xpath('//*[@id="article-content"]/div/p/text()')
        print(pragras)
    if soup.find_all('a', class_='next'):
        next_page = 'http://mobile.zol.com.cn' + str((soup.find_all('a', class_='next'))[0]['href'])
        url = next_page
    else:
        print('done')
        break
