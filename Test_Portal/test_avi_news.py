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




class TestLogin():

    # 登陆浏览器
    def setup_class(self):
        commen.init_driver().get("http://www.qcloud.com")

    #退出浏览器
    def teardown_class(self):
        commen.init_driver().quit()


    def test_more_news_click(self):
        time.sleep(5)
        # 验证首页更多资讯跳转的正确性
        commen.init_driver().find_element_by_link_text("更多资讯").click()


        #验证航空头条页面内容显示的正确性
        new_window=commen.init_driver().window_handles[1]
        commen.init_driver().switch_to.window(new_window)
        commen.init_driver().find_element(By.XPATH,".//*[contains(text(),'热点资讯排行榜')]")


        #验证测试航空头条内容搜索
        commen.init_driver().find_element(By.XPATH,".//input").send_keys("机上互联网推动民航新基建数字化进程发展")
        #按下回车键
        commen.init_driver().find_element(By.XPATH,".//input").send_keys(Keys.ENTER)
        time.sleep(5)
        #页面出现了搜索内容
        search_article=commen.init_driver().find_element(By.XPATH, ".//*[contains(text(),'机上互联网推动民航新基建数字化进程发展')]")

        #验证航空头条内容详情页面的跳转
        search_article.click()
        WebDriverWait(commen.init_driver(), 10).until(EC.presence_of_element_located((By.XPATH, ".//*[contains(text(),'资讯详情')]")))



















