import requests,lxml
from urllib import request
import base64
from http import cookiejar
from bs4 import *
import re
from fake_useragent import UserAgent
import time
import os
import sys
sys.setrecursionlimit(600)#递归深度，防止栈溢出

os.makedirs('./成绩/', exist_ok=True)

def get(id,pw):
    global tmp,flag#向解释器解释全局变量
    try:
        for i in range(len(id)-flag):

            headers = {
    
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Length': '25',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'jwxt.qlu.edu.cn',
                'Origin': 'http://jwxt.qlu.edu.cn',
                'Referer': 'http://jwxt.qlu.edu.cn/jsxsd/xk/LoginToXk',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': str(UserAgent(verify_ssl=False).random),
                #自动获取User-Agent
            }
            
            data = 'encoded={}%25%25%25{}'.format(base64.b64encode(bytes(id[i+flag],encoding="utf8")[0:12]).decode("utf-8"),base64.b64encode(bytes(pw[i+flag],encoding="utf8")[0:8]).decode("utf-8"))
            #post数据用base64编码，学号与密码间三个%25
            #i+flag用于报错后从当前位置开始，[0:12]、[0:8]为bytes编码后学号、密码，去除最后的\n符
            print("第{}个开始，学号{},密码{}  \033[0m".format(i+flag+1,bytes(id[i+flag],encoding="utf8")[0:12],bytes(pw[i+flag],encoding="utf8")[0:8]))
            session = requests.session()#session保持会话
            response = session.request("POST",url,data=data, headers=headers)
            cookies = requests.utils.dict_from_cookiejar(session.cookies)#没用了
            #print(cookies)
            cook=cookies['JSESSIONID']
            print("cookie:{}".format(cook))
            #print(len(response.text))
            if(len(response.text)==5039):
                #5039是登录页面长度，忽略密码错误的学号，继续向下执行，可自行修改
                print("\033[1;31m第{}个学号{},密码{}错误\033[0m".format(i+flag+1,bytes(id[i+flag],encoding="utf8")[0:12],bytes(pw[i+flag],encoding="utf8")[0:8]))
                fe=open("error.log",'ab')
                fe.write("\n[INFO] 第{}个学号{},密码{}错误".format(i+flag+1,bytes(id[i+flag],encoding="utf8")[0:12],bytes(pw[i+flag],encoding="utf8")[0:8]).encode('utf-8'))
                fe.close()
                time.sleep(1)
                continue
            response_grade = session.post(url=grade, data='kksj=&kcxz=&kcmc=&xsfs=all', headers=headers)
            #data是到成绩页的post数据，页面上的选项，这里是所有成绩，而非某学期
            text=response_grade.text
            #print(text)
            t=BeautifulSoup(text,"lxml")
            a=t.find_all("div",class_="Nsb_top_menu_nc")
            #获取姓名学号
            #print(str(a))
            name=re.search(r'<div.*>(.*)<\/div>', str(a)).group(1)
            #正则
    
            fg=open("./成绩/{}.html".format(name),'wb')
            fg.write(text.encode('utf-8'))
            fg.close()
            tmp+=1#记录总共的个数
            #session.invalidate()
            time.sleep(0.5)

    
    except:
        #远程服务拒绝后重发
        time.sleep(1)
        print("\033[1;35m重试......",end="")
        flag=tmp#中转flag
        get(ids,passwd)
    



url = 'http://.........'
grade='http://.........'
#自行修改url和grade

os.system('')#高亮显示
#ua = UserAgent(verify_ssl=False)
start = time.time()
fd=open("id.txt",'r')
fp=open('passwd.txt','r')
ids=fd.readlines()
passwd=fp.readlines()
flag=0#用于记录读取到的学号密码位置，seek过于繁琐
tmp=0#记录总共的个数，中转flag
get(ids,passwd)

fd.close()
fp.close()
end = time.time()
print("++++++共爬取{}个数据，耗时{:.3f}min!+++++++".format(tmp,(end-start)/60))
print("\n*************结束*************")
