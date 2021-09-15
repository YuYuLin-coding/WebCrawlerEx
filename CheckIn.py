print("Check_In_Project is starting")
from bs4 import BeautifulSoup
import urllib.request as urllib
import random
import time
from datetime import datetime
a=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#'2018-07-17 22:54:25'


print()
waitingTime=random.randint(0, 60)
time.sleep(waitingTime)

url='''https://manage.iiiedu.org.tw/api/class/remoteAttendance?qrcode=eyJjbGFzc0lEIjoiSkpBSUVOVDIxMDEiLCJFbWFpbCI6Ims2ZThuMG42eUBnbWFpbC5jb20iLCJOYW1lIjoi5p6X56WQ576kIiwgImN1c3RvbWVyU04iOiIyMDA5MTMxNjAyMTUiLCJJc01lYXRMZXNzIjoiTiJ9'''

response =urllib.urlopen(url)
soup=BeautifulSoup(response,'html.parser')
innertext=soup.find_all('p', class_="text")

if innertext != None:
    with open('/Users/yq/desktop/lessonfile/ChecKIn/checkInRecord.txt','a+') as fin:
        fin.write('systemCall: '+str(a)+', sleepTime: '+str(waitingTime)+"\n")
        fin.write(innertext[0].text+' '+innertext[1].text+' '+innertext[2].text+"\n")
    print("CheckIn done")
else:
    print("CheckIn fail")

