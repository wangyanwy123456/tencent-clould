import os, sys
sys.path.append(os.getcwd())
import pytest
import logging
from Commen import commen
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TestCloudApp():

    # 登陆浏览器
    def setup_class(self):
        commen.init_driver().get("http://www.qcloud.com")

    #退出浏览器
    def teardown_class(self):
        commen.init_driver().quit()


    def test_cloud_app(self):
        time.sleep(5)
        # 验证首页云应用跳转的正确性
        commen.init_driver().find_element_by_link_text("云服务").click()
        time.sleep(5)
        commen.init_driver().switch_to.frame(0)
        time.sleep(5)
        input_ele = commen.init_driver().find_element(By.XPATH,".//input[@placeholder='搜索产品名称']")


        #验证应用搜索
        input_ele.send_keys("公网IP")
        time.sleep(2)
        commen.init_driver().find_element(By.XPATH, ".//input[@placeholder='搜索产品名称']").send_keys(Keys.ENTER)
        commen.get_ele_lenth(4,By.XPATH,".//p[@class='shade']")   #验证搜索出来的数据和预期一致


        #验证应用详情页跳转
        commen.init_driver().find_element(By.XPATH,".//p[@class='shade']").click()
        # commen.init_driver().switch_to.frame(0)
        WebDriverWait(commen.init_driver(), 10).until(EC.presence_of_element_located((By.XPATH, ".//*[contains(text(),'立即开通')]")))




4