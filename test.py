import requests
# 导入 webdriver
from selenium import webdriver
import time
import json

# # 创建chrome启动选项
# chrome_options = webdriver.ChromeOptions()

# # 指定chrome启动类型为headless 并且禁用gpu
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')

# #设置图片不加载
# prefs = {
#     'profile.default_content_setting_values': {
#         'images': 2
#     }
# }
# chrome_options.add_experimental_option('prefs', prefs)
# chrome_options.add_argument('blink-settings=imagesEnabled=false')

# #设置代理
# PROXY = "127.0.0.1:1087"
# chrome_options.add_argument('--proxy-server={0}'.format(PROXY))

# 调用环境变量指定的chrome浏览器创建浏览器对象
# driver = webdriver.Chrome(options=chrome_options)

# # 查看本机ip，查看代理是否起作用
# driver.get("http://httpbin.org/ip")
# print(driver.page_source)


# while(True):
#   print(1)
#   # 如果没有在环境变量指定Chrome位置
#   driver = webdriver.Chrome(options=chrome_options, executable_path='/Users/Horng/git/scientist/chromedriver')
#   # # get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
#   driver.get("https://limit.yysports.com/limitelotterybeijing/activity/registitems")
#   driver
  
#   # print(driver.page_source)
#   print(driver.title)
#   driver.quit()
#   # print(driver.get_cookies())



# while(True):
#   print(1)
#   # 如果没有在环境变量指定Chrome位置
#   driver = webdriver.Chrome(options=chrome_options, executable_path='/Users/Horng/git/scientist/chromedriver')
#   # # get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
#   driver.get("https://wx.yysports.com/limitelottery/activity/registitems")
#   print(driver.page_source)
#   print(driver.title)
#   driver.quit()
  # print(driver.get_cookies())
 

# s = requests.Session()
# proxies={
#     # 'http':'113.194.29.40:9999',
#     # 'https':'113.194.29.40:9999'
#     }
# headers = {
#       'Accept': '*/*',
#       'Accept-Encoding': 'gzip, deflate, br',
#       'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
#       'Connection': 'keep-alive',
#       'Host': 'limit.yysports.com',
#       'Referer': 'https://limit.yysports.com/limitelotterybeijing/registresult.html?activityId=0',
#       'Sec-Fetch-Dest': 'empty',
#       'Sec-Fetch-Mode': 'cors',
#       'Sec-Fetch-Site': 'same-origin',
#       'X-Requested-With': 'XMLHttpRequest',
#       'Cookie':'acw_sc__v3=5fbf7738cbccb07728183923170c5df85d89516b11',
#       # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
#       'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJsaW1pdGVkX2VkaXRpb25fbG90dGVyeSIsImlhdCI6MTYwNjM3MjQxMCwianRpIjoiMzg1MjI5MDgiLCJzdWIiOiIxODU4MzE1ODAwNyIsImxpbWl0ZWRVc2VyIjp0cnVlfQ.bVUHSBMpkGKmjjh4iYPCPNlUK3ccOm6UNsqCh00ff4E'
#     }
# r = s.get('https://limit.yysports.com/limitelotterybeijing/activity/registitems',headers=headers,proxies=proxies)
# print(r)
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)



s = requests.Session()
# proxies={
#     'http':'127.0.0.1:1087',
#     'https':'127.0.0.1:1087'
#     }
headers = {
     'Connection': 'keep-alive',
  'Sec-Fetch-Dest': 'empty',
  'x-requested-with': 'XMLHttpRequest',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15',
  'Mobile': 'Safari/537.36',
  'Content-Type': 'application/json',
  'Accept': '*/*',
  'Origin': 'https://sso-prod.yysports.com',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'
}
# username,
#   password: new Buffer(password).toString('base64'),
#   client_id: 'matrix',
#   redirect_uri: `https://wx.yysports.com/limitelotterybeijing/registresult.html?activityId=${activityId}`,
#   response_type: 'code',
#   state

data = {"username":"18583158002","password":"MTIzMTIzMTIz1","client_id":"matrix","redirect_uri":"https://wx.yysports.com/limitelotterybeijing/registresult.html?activityId=0","response_type":"code","state":"fd87828dd5ce44fd9fa530e177fafb02"}
r = s.post('https://sso-prod.yysports.com/api/member/pousheng/account/login',
data=json.dumps(data),
headers=headers)  
print(r)
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)