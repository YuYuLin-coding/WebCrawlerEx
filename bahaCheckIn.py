print("bahaCheckIn is starting")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

driver = webdriver.Chrome(
    executable_path="/Users/yq/desktop/lessonfile/ChecKIn/chromedriver"
)
driver.get("https://user.gamer.com.tw/login.php")

with open("/Users/yq/desktop/lessonfile/ChecKIn/bahainfo.txt", "r") as fin:
    postusr = fin.readline().splitlines()
    postpasswd = fin.readline()

usrname = driver.find_element(By.NAME, "userid")
usrname.send_keys(postusr)
usrpass = driver.find_element(By.NAME, "password")
usrpass.send_keys(postpasswd + Keys.ENTER)

time.sleep(2)
try:
    a = driver.find_element(By.PARTIAL_LINK_TEXT, "進 入 巴 哈 姆 特")
    a.click()
except:
    print("no show 進入巴哈姆特")

time.sleep(2)
a = driver.find_element(By.ID, "signin-btn")
a.click()

time.sleep(2)
a = driver.find_element(By.ID, "signin-btn")
text = a.text.split("\n")
print(text[0])
Todaytime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
if "每日簽到已達成" in text[0]:
    with open("/Users/yq/desktop/lessonfile/ChecKIn/bahaCheckList.txt", "a+") as fin:
        fin.write("簽到時間: " + str(Todaytime) + " " + text[0] + "\n")
    print("bahaCheckIn 簽到成功")
    driver.quit()
else:
    with open("/Users/yq/desktop/lessonfile/ChecKIn/bahaCheckList.txt", "a+") as fin:
        fin.write("systemCall: " + str(Todaytime) + " 巴哈姆特本日尚未簽到!! " + "\n")
    print("bahaCheckIn 簽到失敗")
