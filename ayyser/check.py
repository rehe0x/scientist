#!/usr/bin/env python3
# encoding: utf-8
from dao.yy import yy
from common.util import getUserAgent,getUUID
from common.ip import getProxies
import json

import queue
import threading
import time 

#线程数
threadMax = 20
#队列最大数
workQueue = queue.Queue(1000)
queueLock = threading.Lock()
threads = []
exitFlag = 0


def start():
  # 创建新线程
  for tid in range(threadMax):
      thread = myThread('Thread-%s' % (tid), workQueue)
      thread.start()
      threads.append(thread)

  fu=open("./file/1k.txt")
  users = fu.read().splitlines()
  # print(users)
  # 填充队列
  queueLock.acquire()
  for user in users:
    u = user.split(' ')
    user = {
      'username' : u[0],
      'password' : u[1]
    }
    workQueue.put(user)
  print(workQueue.qsize())
  queueLock.release()

  # 等待队列清空
  while not workQueue.empty():
      pass
  # 通知线程是时候退出
  global exitFlag
  exitFlag = 1
  # 等待所有线程完成
  for t in threads:
      t.join()
  print ("退出主线程")

def checkRI(user):
  print(user)
  dao = yy(getUserAgent(),2)
  uuid4 = getUUID()
  try:
    jwt = getJwt(dao, user['username'], user['password'], uuid4)
    print(jwt)

    itme = dao.getRegistItems(jwt['jwt'] ,jwt['code'], getProxies())

    print(itme.status_code)
    print(itme.text)
  except Exception as er:
    print(er)
 


def getJwt(dao, username, password, uuid4):
  dao.login(username,password,uuid4,getProxies())

  authCode = dao.getAuthorize(uuid4,getProxies())
  code = authCode.url.split('&')[1].split('=')[1]

  jwt = dao.getToekn(code, uuid4, getProxies())
  jwtCookie = dao.reqUtil.dict_from_cookiejar(jwt.cookies)

  return {
    'jwt' : json.loads(jwt.text)['jwt'],
    'code': code,
    'uid' : jwtCookie['uid']
  }


class myThread (threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            checkRI(data)
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        # time.sleep(1)