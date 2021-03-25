from lxml import html
import requests

import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
url = 'https://www.toutiao.com/api/pc/feed/?min_behot_time=0&category=news_game&utm_source=toutiao&widen=1&tadrequire=true&_signature=_02B4Z6wo00d01ObzUoQAAIDDVgK-T9ojvNjm11YAAFm1RXSLq7PrXd-.gAJw3gW9eF2PuQxdwRrKCQ07-FIEI3b6hydnVK1UaQ-jDd1OR0Ec2DCyH3mhP8ivum2NI0-W69U4rd.uXpUl5aAjd0'


r = requests.get(url, headers=headers)
print(json.load(r.content))
# a=re.findall('<video class="" autoplay="" tabindex="2" mediatype="video" crossorigin="anonymous" src="//v9-xg-web-s.ixigua.com/d2e14b09c2ec50e53f30ea6f3b4f51d3/6012dcaf/video/tos/cn/tos-cn-ve-0026/5c0e52b6580b4a59baaae04bb045abe0/\?a=1768&amp;br=6123&amp;bt=2041&amp;cd=0%7C0%7C0&amp;ch=0&amp;cr=0&amp;cs=0&amp;cv=1&amp;dr=0&amp;ds=3&amp;er=0&amp;l=202101282247180100220281621A08287B&amp;lr=default&amp;mime_type=video_mp4&amp;pl=0&amp;qs=0&amp;rc=M3M3bzVoNTRkMzMzO2QzM0ApOTxmN2VlO2VmNzRpZDxoPGcwYTBxZDEvZTJgLS0tLjBzczYyYDQxYjZfLTBjYjAyNmI6Yw%3D%3D&amp;vl=&amp;vr=" style="position: absolute; top: 0px; left: 0px;"></video>',r.text)
# print(a)