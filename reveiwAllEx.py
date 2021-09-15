from typing import Pattern
import urllib.request as urllib
response=urllib.urlopen('你的網址')
text=response.read().decode('utf-8') #以utf-8解析為為文字字串
lines=text.split('\n') #這字串以空行符號分為陣列

#如果想用命令提示字元使用程式＋特地網頁:
#Ex: python3 ooxx.py '引述字'
import sys
url=sys.argv[1] #在命令提示字元的引述位置加入網頁
filename=url[url.rindex('/')+1:] #取名為網址最後一個/後面

#如果你的爬蟲 網頁/資料 格式為 json
#json 的不同物件key值必須要有一致性
import urllib.request as urllib
import json 
import sys
response=urllib.urlopen('你的網址')
jsonObj=json.load(response) #可以貼到postman看你的資料格式要取哪個陣列

#import re 才可以使用哪些功能
import re
pattern,string='你的條件','你的字串' #條件可以用正規表示法
re.compile(pattern)
re.search(pattern, string, flags=0)
re.match(pattern, string, flags=0)
re.fullmatch(pattern, string, flags=0)
re.split(pattern, string, maxsplit=0, flags=0)
re.findall(pattern, string, flags=0)

#如果你的資料來源是xml檔案
# 必須開頭有 <?xml version="1.0"?>
import urllib.request as urllib
import sys
import xml.etree.ElementTree as ET
tree =ET.parse('all.xml') #從xml檔案解析
root=tree.getroot() #先取得根目錄 且必須為唯一性
#或從字串解析
xml_string ="....."
root = ET.fromstring(xml_string) #root第一個都必須要有唯一性
#-取得子標籤--------------
for child in root:
    print(child.tag, child.attrib)
#-運用陣列----------------
print(root[1][1].text)
#-直接取得特定標籤----------
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

#正規表示法常用寫法:
import re
'<.*>'    #有多遠就找多遠
'<.*?>'   #有多近就找多近
'>(.*)<'  #match.group( )='>(.*)<'
          #match.group(1)='(.*)' 括號內數字表示要求第幾個括號內
result = re.findall('<div>.*?</div>', str)
#==>    ['<div>hello</div>', '<div>hi</div>']
result = re.findall('<div>(.*?)</div>', str)
#==>    ['hello', 'hi']

#如果你的網頁為一般網頁則使用BeautifulSoup
from bs4 import BeautifulSoup
import urllib.request as urllib
response = urllib.urlopen(url)
soup = BeautifulSoup(response, 'html.parser') #解析對象:HTML #Python 內建 html.parser
soup = BeautifulSoup(response, "lxml")        #解析對象:HTML #解析器:lxml
soup = BeautifulSoup(response, "lxml-xml")    #解析對象:XML #解析器:lxml
soup = BeautifulSoup(response, "xml")         #解析對象:XML #解析器:lxml
#上述任意四種求得後，可用以下操作
soup.tag #標籤 #<pid="a01">hello</pid=>
soup.tag.name #標籤的名字 #p
soup.tag['屬性名稱'] 
soup.tag.contents                 #Tag陣列: ['hello']
soup.tag.string #若包含兩個子標籤時，傳回None: hello
#子標籤 .children
#父標籤 .parent
#旁系標籤 .next_sibling /.previous_sibling
#有換行/空格符號時也會被視為標籤 善用repr('目標')
#下一個標籤 .next_element / .previous_element
#find() 與 find_all()
'''find_all('div')
find_all(class_='class_name')
find_all(id='a01')
find_all(id=True)
find_all(attrs={'id': 'a01'})
find_all(attrs={'x': '20', 'y': '30'}) 
find_all(href=re.compile('ad'))''' #運用正規表示