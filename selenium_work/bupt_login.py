from selenium import webdriver
from selenium_work.username_pw import *

chrome=webdriver.Chrome()
chrome.implicitly_wait(5)#wait chrome finish load


chrome.get('https://webvpn.bupt.edu.cn/login')
chrome.find_element_by_id('user_name').send_keys(username)
chrome.find_element_by_name('password').send_keys(pws[0])

chrome.find_element_by_xpath('//*[@id="group-1"]/div[2]/div/div[2]/p[1]').click()
#切换标签页
for handle in chrome.window_handles:
    chrome.switch_to.window(handle)
    if '统一身份验证' in chrome.title:
        break

chrome.find_element_by_id('username').send_keys(username)
chrome.find_element_by_id('password').send_keys(pws[1])
a=chrome.find_element_by_xpath('//*[@id="xtztc"]/div[1]').click()
for handle in chrome.window_handles:
    chrome.switch_to.window(handle)
    if '登录' in chrome.title:
        break
chrome.find_element_by_id('userAccount').send_keys(username)
chrome.find_element_by_id('userPassword').send_keys(pws[2])