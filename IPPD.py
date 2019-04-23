# -*- coding:utf-8 -*-
import requests
import time
import json
url='http://freeapi.ipip.net/'
with open('ip.txt','r') as f:
	ip=f.readline().replace('\n','')
	while ip:
		url_g=url+ip
		s=requests.get(url_g)
		with open('result.log','a') as f2:
				print(ip)
				f2.write(ip+'\n')
				a=('-'.join(json.loads(s.text)))
				print(a)
				f2.write(a.encode('utf-8')+'\n')
		ip=f.readline().replace('\n','')
		time.sleep(1)
print("Finish! Please view the log file!")
