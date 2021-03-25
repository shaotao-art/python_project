import requests
import json
import re
import subprocess
url='https://www.bilibili.com/video/BV1nE411w7tv?from=search&seid=6138967245019187791'
name='en'
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chr\
            ome/88.0.4324.182 Safari/537.36'}
def get_urls(url):
    session=requests.session()
    res = session.get(url=url,headers=headers)
    pattern=re.compile('playinfo__=(.+?)<\/script>')
    infos=pattern.findall(res.text)
    video_url=json.loads(infos[0])["data"]["dash"]["video"][0]["baseUrl"]
    audio_url = json.loads(infos[0])["data"]["dash"]["audio"][0]["baseUrl"]
    print(video_url)
    print(audio_url)
    return video_url,audio_url

def fileDownload(homeurl,url, name, session=requests.session()):
    # 添加请求头键值对,写上 refered:请求来源
    headers.update({'Referer': homeurl})
    # 发送option请求服务器分配资源
    session.options(url=url, headers=headers)
    # 指定每次下载1M的数据
    begin = 0
    end = 1024*512 - 1
    flag = 0
    while True:
        # 添加请求头键值对,写上 range:请求字节范围
        headers.update({'Range': 'bytes=' + str(begin) + '-' + str(end)})
        # 获取视频分片
        res = session.get(url=url, headers=headers)
        if res.status_code != 416:
            # 响应码不为为416时有数据
            begin = end + 1
            end = end + 1024*512
        else:
            headers.update({'Range': str(end + 1) + '-'})
            res = session.get(url=url, headers=headers)
            flag=1
        with open(name.encode("utf-8").decode("utf-8"), 'ab') as fp:
            fp.write(res.content)
            fp.flush()
        # data=data+res.content
        if flag==1:
            fp.close()
            break
def combineVideoAudio(videopath,audiopath,outpath):
    subprocess.call(("C:\\Users\starfish\Favorites\\ffmpeg-N-101694-g322be6107a-win64-gpl-shared-vulkan\\bin\\ffmpeg -i " + videopath + " -i " + audiopath + " -c copy "+ outpath))
if __name__ == '__main__':
    v_url,a_url=get_urls(url=url)
    fileDownload(homeurl=url,url=v_url,name=f'{name}.mp4')
    fileDownload(homeurl=url,url=a_url, name=f'{name}.wav')
