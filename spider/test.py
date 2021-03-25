import requests
import json
import re
import subprocess
url='https://rb546n.jomodns.com/r/bdcdncmn3.inter.71edge.com/videos/vts/20210323/ad/6e/4082b4203732118fb9f2f5b62cbd9d2d.ts?key=02df0838288b54a60706118f237f12d7d&dis_k=c3fe6f03db9c73c5156ae0438e43fb6a&dis_t=1616674785&dis_dz=CMNET-BeiJing&dis_st=49&src=iqiyi.com&dis_hit=0&dis_tag=01000000&uuid=78f46d9f-605c7fe1-f4&sgti=14_16da677fb8f73287b62d8ba6d1bc5e0d_1616674794644&mss=1&pv=0.1&qd_tm=1616674785146&start=55613440&cross-domain=1&qd_ip=0&sd=0&dfp=&contentlength=13890560&qd_vip=1&qd_p=0&qd_k=de84235492797b6458fae8862f8bbf94&ve=&qd_tvid=5072596009294600&qd_src=01010031010000000000&stauto=1&end=69504000&qd_uid=1400635358&ori=pcw1&num=1616674802579'
name='fffffffffff.mp4'
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chr\
            ome/88.0.4324.182 Safari/537.36'}


# 获取视频分片
session=requests.session()
res = session.get(url=url, headers=headers)
with open(name.encode("utf-8").decode("utf-8"), 'ab') as fp:
    fp.write(res.content)
    fp.flush()
fp.close()