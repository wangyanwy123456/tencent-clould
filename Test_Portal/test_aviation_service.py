#该页面是写协同制造模块的用例
import os, sys
sys.path.append(os.getcwd())
# import pytest
from Commen import commen
from selenium.webdriver.common.by import By




class Test_Aviation_Service():


    # 登陆浏览器
    def setup_class(self):
        commen.init_driver().get("http://www.qcloud.com")

    #退出浏览器
    def teardown_class(self):
        commen.init_driver().quit()


    def test_aviation_service(self):
        # 验证航空服务号跳转
        commen.init_driver().find_element_by_link_text("航空服务号").click()
        commen.time.sleep(1)
        commen.find_ele(By.XPATH,".//div[contains(text(),'机构类型')]")


        #验证航空服务号搜索
        commen.send_text(By.XPATH,".//input[@class='seal-input']","上海沐冬电子科技有限公司")
        commen.find_ele(By.XPATH,".//input[@class='seal-input']").send_keys(commen.Keys.ENTER)
        commen.time.sleep(1)
        commen.get_ele_text(By.XPATH,".//span[@class='list-head-number']","2")

        #验证航空服务号详情页跳转
        commen.click_ele(By.XPATH,".//li/div[@class='seal-flex']")
        commen.time.sleep(1)
        commen.get_ele_text(By.XPATH, ".//div[@class='tabs-item']","关于我们" )


