import random
import requests
import time
import re

titles=[]
pics=[]
details=[]
prices=[]
stores=[]
urls=[f'https://s.taobao.com/search?q=iPhone&imgfile=&commend=all&ssid=s5-e&sea\
rch_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taoba\
o-item.1&ie=utf8&initiative_id=tbindexz_20170306&p4ppushleft=1%2C48&s={44*i}'for i in range(0,10) ]
cookie_dic = {}
def make_dic():
    cookies_raw='cookie: _m_h5_tk=bf6120654303ee1957c2b3df99c62139_1616057748480; _m_h5_tk_enc=624ba9e5a36673d46d53a8ccb7aebb66; t=40dca96e339cff2ff00c861e140e9c24; cna=bIrQGAGHxFICAd9ok9TZHiw+; xlly_s=1; sgcookie=E100gp2Ok409XMoIYJoTNct3lr8IpEGA1%2FNpw5XtRqdmYGf7jUYoWG5n7XtrHu3vgyyppO1HIVwtkPMc1TlZUSRwcQ%3D%3D; uc3=vt3=F8dCuAop38iUPa1IzYs%3D&nk2=EFY19vuvzQutNOPWvRbt&id2=UUGgqiOvqe2nVA%3D%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; lgc=shaojin49217468; uc4=nk4=0%40Eo9LPC4uMk7J3P86ERJ0bc5DXlKfDGU4Jdk%3D&id4=0%40U2OXkB8iSZQ92%2B6ZfHWNvWDU8kgP; tracknick=shaojin49217468; _cc_=V32FPkk%2Fhw%3D%3D; enc=9Ek96Ms1j5r6okkBVuqWry8VY5OIO%2BdoBvOaH9wKhyzoeA4JnU1EX6WVzrzC81cLmNgKozwC1ry4rMKXbTqbWg%3D%3D; mt=ci=27_1; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=Uoe1hMShVQv5eQ%3D%3D; _tb_token_=eed44e3165176; JSESSIONID=2C387A01E4973BADC6797BE4EE3C748B; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; isg=BDQ0YxC06DRY-3z5h_JRLsIHBfKmDVj3QIvows6VwL9COdSD9h0oh-r7vXHh2pBP; l=eBEstMWuji4Smwb2BOfanurza77OSIRYYuPzaNbMiOCP9w1B547dW6w0G8Y6C3GVh6DXR3SodYDwBeYBqQAonxv92j-la_kmn; tfstk=c9I1B7vOBfc1aNUqbOwE0SKmPeKAwsPBKPOOCaZJVfAyjQ1cn0RWLAbmtDLJd'
    pattern=re.compile(r':{0,1} ([_a-zA-Z].+?[_a-z\d])=(.+?);')
    cookies_res=pattern.findall(cookies_raw)
    for each in cookies_res:
        cookie_dic[each[0]]=each[1]
    cookie_dic['tfstk']='c9I1B7vOBfc1aNUqbOwE0SKmPeKAwsPBKPOOCaZJVfAyjQ1cn0RWLAbmtDLJd'
    print('done dic')
    print('----------------------------------------------------------------------------')


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeb\
    Kit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
'referer':'https://s.taobao.com/search?q=iPhone&imgfile=&c\
ommend=all&ssid=s5-e&search_type=item&sourceId=tb.index\
&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'
}


def run():
    for each_url in urls:
        r = requests.get(each_url, headers=headers, cookies=cookie_dic)
        print(r.text)
        pattern = re.compile(
            r'"raw_title":"(.+?)"[\s\S]+?"pic_url":"(.+?)"[\s\S]+?"detail_url":"(.+?)"[\s\S]+?"view_price":"(.+?)"[\s\S]+?"nick":"(.+?)"')
        data = pattern.findall(r.content.decode('UTF-8'))
        print('done one page-------------------------------')
        for each in data:
            titles.append(each[0])
            pics.append(each[1])
            details.append(each[2])
            prices.append(each[3])
            stores.append(each[4])
        time.sleep(random.randint(0,3))
def save():
    with open('taobao.txt','w')as f:
        for i in range(0,len(stores)):
            f.write(titles[i]+' '+pics[i]+'   '+details[i]+'  '+prices[i]+'  '+stores[i]+'\n')
make_dic()
run()
save()



# r = requests.get(urls[0], headers=headers, cookies=cookie_dic)
# print(r.text)
# pattern = re.compile( r'"raw_title":"(.+?)"[\s\S]+?"pic_url":"(.+?)"[\s\S]+?"detail_url":"(.+?)"[\s\S]+?"view_price":"(.+?)"[\s\S]+?"nick":"(.+?)"')
# data = pattern.findall(r.content.decode('UTF-8'))
# print(data)