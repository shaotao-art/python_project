import requests
import re


class spider:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}

    # url是从外部传来的  所以代码中不要写self.url  url不是其内部的变量
    def request_info(self, url):
        r = requests.get(url, headers=self.headers)
        return r.text

    def select_info(self, pattern, r_text):
        songs_info = re.findall(pattern, r.text)
        urls = []
        names = []
        # http://music.163.com/song/media/outer/url?id=566442496.mp3
        for song in songs_info:
            urls.append('http://music.163.com/song/media/outer/url?id=' + str(song[0]) + '.mp3')
            names.append(song[1] + '.mp3')
        return urls, names

    def download_songs(self, urls, names):
        for each in urls:
            song_r = requests.get(each, headers=self.headers)
            with open(names[urls.index(each)], 'wb')as f:
                f.write(song_r.content)

    def crawl_main(self, url, pattern):
        r_text = self.request_info(url)
        urls, names = self.select_info(pattern, r_text)
        self.download_songs(urls, names)
