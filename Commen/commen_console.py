from selenium import webdriver
import Commen
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Commen import commen



console_url = "http://console.qcloud.com"
username_busyniss = "2781532837@qq.com"
password_busyniss = "506019wy!"


#登录console
def login_console():
    commen.init_driver().get(console_url)
    commen.click_ele(By.XPATH,".//button[@class='seal-button seal-button--link'][1]")
    commen.send_text(By.XPATH,".//input[@placeholder='邮箱地址']",username_busyniss)
    commen.send_text(By.XPATH,".//input[@placeholder='密码']",password_busyniss)
    commen.click_ele(By.XPATH,".//button[@type='submit']")
    time.sleep(15)
    commen.get_ele_text(By.XPATH,".//ul[@class='account-content']",username_busyniss)


#点击确认或取消
def click_act(name,act):
    commen.find_ele(By.XPATH,".//*[contains(text(),'{}')]".format(name))
    commen.click_ele(By.XPATH,".//*[contains(text(),'{}')]".format(act))
# if __name__ == "__main__":
#     login_console()