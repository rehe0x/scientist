#!/usr/bin/env python3
# encoding: utf-8

import requests
import time
import base64
import json

baseHeaders = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'limit.yysports.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'X-Requested-With': 'XMLHttpRequest'
      }

class yy:

  def __init__(self,userAgent,activityId):
    self.reqUtil = requests.utils
    self.req = requests.Session()
    baseHeaders['User-Agent'] = userAgent
    self.baseHeaders = baseHeaders
    self.activityId = activityId


  def login(self, username, password, state, proxies):
    url = 'https://sso-prod.yysports.com/api/member/pousheng/account/login'
    data = {
      "username" : username,
      "password": str(base64.b64encode(password.encode("utf-8")),'utf-8'),
      "client_id": "matrix",
      "redirect_uri": f"https://wx.yysports.com/limitelotterybeijing/registresult.html?activityId={self.activityId}",
      "response_type": "code",
      "state": "fd87828dd5ce44fd9fa530e177fafb02"
    }
    headers = {
      'Host': 'sso-prod.yysports.com',
      'Origin': 'https://sso-prod.yysports.com',
      'Referer': f'https://sso-prod.yysports.com/login?redirect_uri=https://limit.yysports.com/limitelotterybeijing/form.html?activityId={self.activityId}&from=244000018&fromType=1&client_id=matrix&state={state}',
      'Content-Type': 'application/json;charset=UTF-8'
    }
    result = self.req.post(
      url = url,
      data=json.dumps(data),
      headers= {**self.baseHeaders, **headers},
      proxies=proxies)

    re = self.res_handler(result, self.login, username, password, state, proxies)
    return re

  def getAuthorize(self, state, proxies):
    url = 'https://sso-prod.yysports.com/oauth/authorize'
    data = {
      "client_id" : 'matrix',
      "redirect_uri": f'https://limit.yysports.com/limitelotterybeijing/form.html?activityId={self.activityId}',
      "response_type": "code",
      "state": state
    }
    
    headers = {
      'Host': 'sso-prod.yysports.com',
      'Origin': 'https://sso-prod.yysports.com',
      'Referer': f'https://sso-prod.yysports.com/login?redirect_uri=https://limit.yysports.com/limitelotterybeijing/form.html?activityId={self.activityId}&from=244000018&fromType=1&client_id=matrix&state={state}',
      'Content-Type': 'application/json;charset=utf-8'
    }
    result = self.req.get(
      url = url,
      params=data,
      headers= {**self.baseHeaders, **headers},
      proxies=proxies)
    re = self.res_handler(result, self.getAuthorize, state, proxies)
    return re

  def getToekn(self, code, state, proxies):
    url = 'https://limit.yysports.com/limitelotterybeijing/regist/checkssologin'
    data = {
      "code" : code,
      "redirecturl": f'form.html?activityId={self.activityId}'
    }
    headers = {
      'Host': 'limit.yysports.com',
      'Referer': f'https://limit.yysports.com/limitelotterybeijing/form.html?activityId={self.activityId}&code={code}&state={state}',
      'Content-Type': 'application/json;charset=UTF-8'
    }
    result = self.req.get(
      url = url,
      params=data,
      headers= {**self.baseHeaders, **headers},
      proxies=proxies)
    re = self.res_handler(result, self.getToekn, code, state, proxies)
    return re

  def getRegistItems(self, token, code, proxies):
    url = 'https://limit.yysports.com/limitelotterybeijing/activity/registitems'

    headers = {
      'Host': 'limit.yysports.com',
      'Referer': f'https://limit.yysports.com/limitelotterybeijing/registresult.html?activityId={self.activityId}&code={code}',
      'Content-Type': 'application/json;charset=UTF-8',
      'Authorization': 'Bearer '+token
    }
    result = self.req.get(
      url = url,
      headers= {**self.baseHeaders, **headers},
      proxies=proxies)
    re = self.res_handler(result, self.getRegistItems, token, code, proxies)
    return re

  def res_handler(self, body, func, *args):
    # func(*args)
    body.encoding="utf-8"
    if body.status_code == 200:
      return body
    elif body.status_code == 302:
      return body
    elif body.status_code == 500:
      if json.loads(body.text)['status'] == 500 and json.loads(body.text)['message'] == 'login.auth.forbidden':
        raise Exception('换ip')
    else:
      print(body.status_code)
      print(body.headers['Content-Type'])
      print(body.text)
      return body