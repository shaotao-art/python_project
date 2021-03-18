import requests
import re
from lxml import html
from selenium import webdriver
import time
from random import randint

class job_51:
    def __init__(self):
        self.urls=[]
        self.ids=[]
        self.jobs = []
        self.salary = []
        self.companys = []
        self.detail_urls=[]
        self.detail=[]
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chr\
            ome/88.0.4324.182 Safari/537.36'}

    def get_max_page(self,url):
        #利用selenium获取最大页面数
        chrome=webdriver.Chrome('C:\\Users\starfish\Documents\chromedriver')
        chrome.implicitly_wait(10)
        chrome.get(url=url)
        page_nums=chrome.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[2]/div/div/div/span[1]').text
        max_page=int(re.findall(r'\d+',page_nums)[0])
        chrome.close()
        self.urls = [f'https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,{i}.html?la\
        ng=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&or\
        d_field=0&dibiaoid=0&line=&welfare=' for i in range(1, 3)]




    def list_append(self):
        for each_url in self.urls:
            r=requests.get(headers=self.headers,url=each_url)

            data=re.compile(r'"jobid":"(.*?)".+?"job_name":"(.*?)".+?"providesalary_text":"(.*?)".+?"company_name":"(.*?)"')
            datas=data.findall(r.text)

            for each in datas:
                self.detail_urls.append(f'https://jobs.51job.com/beijing/{each[0]}.html?s=sou_sou_soulb&t=0')
                self.jobs.append(each[1])
                self.salary.append(each[2])
                self.companys.append(each[3])

            time.sleep(randint(1,3))

    def get_detail(self)->str:
        for each_url in self.detail_urls:
            r=requests.get(headers=self.headers,url=each_url)
            r_text=r.content.decode('gbk')
            a=html.fromstring(r_text).xpath('//div[@class="bmsg job_msg inbox"]')[0].xpath('string(.)').strip() #获取一个标签下的所有文本
            info=''
            for each_str in a:
                info=info+each_str.strip()
            print(each_url)
            self.detail.append(info)
            print('------------------------------------------------------------------------------------')
            time.sleep(randint(1, 3))



    def svae(self):
        with open('51job.txt','w')as f:
            for i in range(0,len(self.jobs)):
                f.write(self.jobs[i]+'|||'+self.salary[i]+'|||'+self.companys[i]+'|||'+self.detail[i]+'\n')


a=job_51()
a.get_max_page('https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=')
a.list_append()
a.get_detail()
a.svae()

