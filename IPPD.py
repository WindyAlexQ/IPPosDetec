import requests
import time
url='http://freeapi.ipip.net/'
with open('ip.txt','r') as f:
	ip=f.readline().replace('\n','')
	while ip:
		url_g=url+ip
		s=requests.get(url_g)
		print ip
		print s.content
		ip=f.readline().replace('\n','')
		time.sleep(1)
print "That's all"