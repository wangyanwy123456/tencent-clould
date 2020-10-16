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



admin_url = "http://admin.qcloud.com"
username_admin = "lxq520064@126.com"
password_admin = "123qweQWE!@#"
admin_acount_name = "SP"


#登录amidn管理后台
def login_admin():
    commen.init_driver().get(admin_url)
    commen.send_text(By.XPATH,".//input[@placeholder='邮箱地址']",username_admin)
    commen.send_text(By.XPATH,".//input[@placeholder='密码']",password_admin)
    commen.click_ele(By.XPATH,".//button[@type='submit']")
    time.sleep(15)
    commen.get_ele_text(By.XPATH, ".//div[@class='overview-panel-inner']", admin_acount_name)

if __name__ == "__main__":
    login_admin()