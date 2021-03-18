# 主要是两个参数的加密算法   有兴趣可以分析一下
import requests
import json
paras={'params': 'F//DijLFIs3ixwW9UpiI4XWH6+bQ9Ax+/DvZmj9tepPDp7EYKol6syNPJLSJhsryV5Z8XcmY4RDsmSYHar8GjtlYKpZajN8pUqbob6towOkU8Ojp/Cc7WM8VmG3DomJvqJWVHOvK/JwVuG/GqLd8sIQeoYceACNhqWlWkNifuHsFfqFb8DfdsCCrGt5uPUVhVkRZBqNt0XJeoewCrS2k2JGWkTjnHN5Ku0BSRenvxjDZvFsV+kuO8bQFSVA/b110EDXMLAQtMTjUQaF0veFLAUPhieqPYR7n10OrLOqrd0U=',
'encSecKey': '2a139e62de050c56fa49fe375bb3f2d9226811599b98bf895b3a6cf9277685f17e9b8e068ec5ca6400318b8aaaee0b12e23defa2555d85334626c69d4e92997d86716ecbd8ac9fa80abbdd3a0500ccf2c27b494ddbb956e04413f3822bc7a24e9d1ab7d112d72cd081c1358760bc9cc4c78dae8003147eb042b0a68348d20c66'
}

a=requests.post('https://music.163.com/weapi/comment/resource/comments/get?csrf_token=',data=paras)
data=json.loads(a.text)
for each in data['data']['comments']:
    print(each['content']+'     '+each['user']['nickname'])
