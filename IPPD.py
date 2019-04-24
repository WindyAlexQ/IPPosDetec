#! python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-24 08:03:52
# @Author  : windy
# @Version : v2.0
import requests
import time
import json
url='http://freeapi.ipip.net/'
filename='result-{}.log'.format(time.strftime('%Y%m%d%H%M',time.localtime(time.time())))
with open(filename,'a') as f2:
	with open('ip.txt','r') as f:
		ip=f.readline().replace('\n','')
		while ip:
			url_g=url+ip
			s=requests.get(url_g)
			print(ip)
			f2.write(ip+'\n')
			a=('-'.join(json.loads(s.text)))
			print(a)
			f2.write(a+'\n')
			ip=f.readline().replace('\n','')
			time.sleep(1)
input("Finish! Please view the log file:{}!".format(filename))
