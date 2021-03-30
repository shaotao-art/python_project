import requests
import re
'''
下载网易云歌单的所有歌曲
测试url：'https://music.163.com/#/playlist?id=6677994458'
'''

#抓包所得
'''
pagelist;https://music.163.com/playlist?id=6677994458    #由此也可见真实的请求是没有井号的
comment接口：https://music.163.com/weapi/comment/resource/comments/get?csrf_token=
音频链接：https://m701.music.126.net/20210326181726/04eb0c0362b1c5a97f2436c4a6209ce0/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/7694712557/5f34/d7c7/2a4c/31a9eb3383562342a1f46e086dc39b89.m4a
可以下载播放  但是看起来自己构造链接会很麻烦
'''

'''
应该在request结果下搜索
比如你请求这'https://music.163.com/#/playlist?id=6677994458'
浏览器中敲入该链接的源代码
也与request的不同 因为浏览器会多加载
'''

class spider:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}

    # url是从外部传来的  所以代码中不要写self.url  url不是其内部的变量
    def request_info(self, url):
        r = requests.get(url, headers=self.headers)
        return r.text

    #获取歌曲的名称和id  并拼接成下载链接
    def select_info(self, pattern, r_text):
        songs_info = re.findall(pattern, r_text)
        urls = []
        names = []
        # http://music.163.com/song/media/outer/url?id=566442496.mp3
        for song in songs_info:
            urls.append('http://music.163.com/song/media/outer/url?id=' + str(song[0]) + '.mp3')
            names.append(song[1] + '.mp3')
        return urls, names

    #根据url下载歌曲
    def download_songs(self, urls, names):
        for each in urls:
            song_r = requests.get(each, headers=self.headers)
            with open(f'./../midea/{names[urls.index(each)]}', 'wb')as f:
                f.write(song_r.content)


    #主函数
    def crawl_main(self, url, pattern):
        r_text = self.request_info(url)
        urls, names = self.select_info(pattern, r_text)
        self.download_songs(urls, names)

test=spider()

#请注意 请求url要将链接中的#号去掉 才能拿到信息
#print(test.request_info('https://music.163.com/#/playlist?id=6677994458'))
r_text=test.request_info('https://music.163.com/playlist?id=6677994458')
pattern='<li><a href="\/song\?id=(.*?)">(.*?)<\/a>'
urls,names=test.select_info(pattern=pattern,r_text=r_text)
test.download_songs(urls,names)




# 这里会长出一朵花