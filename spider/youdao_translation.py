# from lxml import html
# import requests
#
# import json
# cookie={'OUTFOX_SEARCH_USER_ID':'345055189@10.108.160.102',
#         'JSESSIONID':'aaatXRJr01jZe9bMXxfHx',
#         'OUTFOX_SEARCH_USER_ID_NCOO':'1578783882.3104763',
#         '___rl__test__cookies':'1616071888838'}
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeb\
#     Kit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
# }
# url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
# data_dic={
# 'i': '喜欢',
# 'client': 'fanyideskweb',
# 'keyfrom': 'fanyi.web',
#
#
# }
#
# r = requests.post(url,data=data_dic, headers=headers,cookies=cookie)
# print(r.text)
import hashlib
import random
import time
import requests

"""
向有道翻译发送data，得到翻译结果
"""
class Youdao:
    def __init__(self, msg):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.msg = msg
        self.ts=self.get_ts()
        self.salt=self.get_salt()

    def get_ts(self):
        # 根据当前时间戳获取ts参数
        s = int(time.time() * 1000)
        return str(s)

    def get_salt(self):
        # 根据当前时间戳获取salt参数
        s = int(time.time() * 1000) + random.randint(0, 10)
        return str(s)

    def get_sign(self):
        # 使用md5函数和其他参数，得到sign参数
        words = "fanyideskweb" + self.msg + self.salt + "n%A-rKaT5fb[Gy?;N5@Tj"

        # 对words进行md5加密
        hashlib.md5()
        m = hashlib.md5()
        m.update(words.encode('utf-8'))
        return m.hexdigest()

    def get_result(self):
        Form_Data = {
            'i': self.msg,
            'from': 'zh-CHS',
            'to': 'en',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.get_sign(),
            'ts': self.ts,
            'bv': 'a4f4c82afd8bdba188e568d101be3f53',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION'
        }

        headers = {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=1389460813@123.125.1.12',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OSX10_14_2) AppleWebKit/537.36(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        response = requests.post(self.url, data=Form_Data, headers=headers)
        translate_results = response.json()
        # 找到翻译结果
        if 'translateResult' in translate_results:
            translate_results = translate_results['translateResult'][0][0]['tgt']
            print(f'\t【{self.msg}】 >>> 【{translate_results}】成功!')
            return translate_results
        else:
            print(translate_results)

def change_cn2en(keywords):
    return Youdao(keywords).get_result()


if __name__ == "__main__":
    keywords='找到翻译结果'
    change_cn2en(keywords)