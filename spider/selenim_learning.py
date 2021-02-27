




'''
from selenium import webdriver
登录淘宝

chrome = webdriver.Chrome()
chrome.get('https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fs.taobao.com%2Fsearch%3Fq%3Diphone%26imgfile%3D%26commend%3Dall%26ssid%3Ds5-e%26search_type%3Ditem%26sourceId%3Dtb.index%26spm%3Da21bo.2017.201856-taobao-item.1%26ie%3Dutf8%26initiative_id%3Dtbindexz_20170306&uuid=310611a6bfe1855eb92eb7b187e7c16e')
chrome.find_element_by_id('fm-login-id').send_keys('shaotao')
chrome.find_element_by_id('fm-login-password').send_keys('sdsada')
chrome.find_element_by_link_text('登录')

'''

from selenium import webdriver

'''
选取元素用xpath 和 id是最屌的

'''
chrome = webdriver.Chrome()
chrome.get('https://passport.bilibili.com/login')
chrome.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[1]/span[2]').click()
chrome.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[3]/div[1]/div/input').send_keys('19800303173')
chrome.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[3]/div[3]/button/span').click()

