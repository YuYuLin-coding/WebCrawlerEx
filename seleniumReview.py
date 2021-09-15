# selenium Review 使用時機:需要與網頁互動時
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#需等待特定時間做動作時
import time # 較笨
from selenium.webdriver.support.ui import WebDriverWait #較佳

#定義等待項目
# 或使用: time.sleep(2)
def checkNumber(driver):
    number=driver.find_element(By.ID,'number')
    if number.text =='hello':
        return False
    else:
        return True

#啟動chromedriver,路徑為同層資料夾執行檔./
driver = webdriver.Chrome(executable_path='./chromedriver')
    #也可以用headless選項不直接開啟瀏覽器
    #options=webdriver.chrome.options.Options()
    #options.add_argument('--headless')
    #driver = webdriver.Chrome(executable_path='./chromedriver',options=options)
#瀏覽器呼叫網址
driver.get('https://google.com.tw')
#import By來索取標籤名字，如google.com.tw的收尋欄
q=driver.find_element(By.NAME,'q')
#import Keys 來表示模擬按鍵，並輸入字串後按下Enter鍵。
q.send_keys('疫情'+Keys.BACKSPACE+Keys.BACKSPACE+'指揮中心'+ Keys.ENTER)
#呼叫WebDriverWait 等待什麼事情發生 當然也要宣告最多等多久
WebDriverWait(driver,timeout=30).until(checkNumber)
#搜尋超連結且其中名字有指定字串的第一個符合連結
a=driver.find_element(By.PARTIAL_LINK_TEXT("指揮"))
#全部都符合的字串連結: driver.find_element_by_link_text
a.click()
#同理按鈕: driver.find_element(By.ID, 'bn').click()

#同時多重鍵操作，例如全選
# 需要導入模塊: from selenium import webdriver [as 別名]
# 或者: from selenium.webdriver import ActionChains [as 別名]
action = webdriver.ActionChains(driver)
action.key_down(Keys.COMMAND).send_keys_to_element(q,'a').perform()
#參考更多指令: https://codertw.com/程式語言/367991/

#有表單，輸入完後送表單
form = driver.find_element(By.ID, 'myform')
form.submit()

#--------------------------------------------------
#---------------題外話:簡單建立後台連線----------------
#--------------------------------------------------
'''
必須要先建如下
/WWW
    /bin-cgi
        /後台位置內容.py
'''
#後台位置內容.py 開頭必須要有以下字串
'''
#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
'''
#上述字元來源，可以在命令提示字元輸入: which python3
#/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

#建好後，想確認連線正常可以在 bin-cgi 資料夾下的命令提示字元輸入
'''
chmod 755 '你的檔案名稱.副檔名'
'''
'''
./test.py
'''


#開啟後台資料庫連線，在www資料夾下 命令提示字元輸入
'''
python3 -m http.server --cgi
'''