#该页面是写协同制造模块的用例
import os, sys
sys.path.append(os.getcwd())
# import pytest
from Commen import commen
from selenium.webdriver.common.by import By




class TestCloudApp():


    # 登陆浏览器
    def setup_class(self):
        commen.init_driver().get("http://www.qcloud.com")

    #退出浏览器
    def teardown_class(self):
        commen.init_driver().quit()


    #供需服务大厅——企业找服务服务首页展示——更多服务跳转——服务列表展示——服务详情页展示
    def test_collaborative(self):
        #验证协同制造模块——供需服务大厅跳转
        commen.time.sleep(1)
        collaborative = commen.init_driver().find_element_by_link_text("协同制造")
        commen.Action.move_to_element(collaborative).perform()
        commen.time.sleep(1)
        commen.init_driver().find_element_by_link_text("供需服务大厅").click()
        commen.time.sleep(1)
        commen.get_ele_text(By.XPATH,".//li[contains(text(),'企业找服务')]","企业找服务")


        #验证更多服务跳转
        commen.click_ele(By.XPATH, ".//*[contains(text(),'更多服务')]")
        commen.time.sleep(1)
        commen.find_ele(By.XPATH,".//*[contains(text(),'服务列表')]")

        #验证服务详情页展示
        commen.click_ele(By.XPATH,".//li/div[@class='seal-flex']")
        commen.find_ele(By.XPATH, ".//*[contains(text(),'服务商客服')]")


        #产能设备共享平台——设备首页展示——更多设备跳转——设备列表展示——设备详情页展示
    def test_more_device(self):
        commen.time.sleep(1)
        #验证协同制造模块产能设备共享平台跳转
        commen.init_driver().find_element(By.XPATH,".//*[contains(text(),'协同制造')]").click()
        commen.time.sleep(1)
        commen.init_driver().find_element_by_link_text("产能设备共享平台").click()
        commen.time.sleep(1)

        #验证协同制造模块产能设备跳转正确
        commen.find_ele(By.XPATH,".//*[contains(text(),'产能设备共享服务')]")

        #验证更多设备跳转正确
        commen.click_ele(By.XPATH,".//*[contains(text(),'更多设备')]")
        commen.find_ele(By.XPATH,".//a[contains(text(),'设备列表')]")

        #验证设备详情页跳转正确
        commen.click_ele(By.XPATH, ".//li/div[@class='seal-flex']")
        commen.find_ele(By.XPATH, ".//*[contains(text(),'设备详情')]")


    # 产能设备共享平台——更多共享首页展示——更多共享跳转——共享设备列表展示——共享设备详情页展示
    def test_more_share_device(self):
        commen.time.sleep(1)
        # 验证协同制造模块产能设备共享平台跳转
        commen.init_driver().find_element(By.XPATH, ".//*[contains(text(),'协同制造')]").click()
        commen.time.sleep(1)
        commen.time.sleep(1)
        commen.init_driver().find_element_by_link_text("产能设备共享平台").click()
        commen.time.sleep(1)

        #验证协同制造更多共享页展示正确
        commen.find_ele(By.XPATH, ".//*[contains(text(),'推荐产能设备共享服务')]")

        #验证更多共享跳转正确
        commen.click_ele(By.XPATH,".//*[contains(text(),'更多共享')]")
        commen.time.sleep(1)
        commen.find_ele(By.XPATH,".//*[contains(text(),'设备详情')]")


        #验证更多共享设备详情页跳转正确
        commen.click_ele(By.XPATH, ".//li/div[@class='seal-flex']")
        commen.time.sleep(1)
        commen.find_ele(By.XPATH,".//a[contains(text(),'设备基础信息')]")


    #高端人才共享平台——高端人才首页展示——更多人才跳转——人才列表展示——人才详情页展示
    def test_talent_pensonl(self):
        commen.time.sleep(1)
        # 验证协同制造高端人才共享平台跳转
        commen.find_ele(By.XPATH, ".//*[contains(text(),'协同制造')]").click()
        commen.time.sleep(1)
        commen.init_driver().find_element_by_link_text("高端人才共享平台").click()
        commen.time.sleep(1)


        #验证高端人才页面展示
        commen.find_ele(By.XPATH, ".//*[contains(text(),'推荐高端人才')]")


        #验证更多人才跳转
        commen.click_ele(By.XPATH,".//*[contains(text(),'更多人才')]")
        commen.time.sleep(1)
        commen.find_ele(By.XPATH,".//*[contains(text(),'人才列表')]")

        #验证人才列表详情页跳转
        commen.click_ele(By.XPATH,".//li/div[@class='seal-flex']")
        commen.time.sleep(1)
        commen.find_ele(By.XPATH,".//div[contains(text(),'个人详情')]")

    # 科技成果共享平台——科技成果首页展示——更多成果跳转——科技成果列表展示——科技成果详情页展示
    def test_scientific_achievements(self):
        commen.time.sleep(1)
        # 验证协同制造科技成果共享平台跳转
        commen.find_ele(By.XPATH, ".//*[contains(text(),'协同制造')]").click()
        commen.time.sleep(1)
        commen.init_driver().find_element_by_link_text("科技成果共享平台").click()
        commen.time.sleep(1)


        #验证协同制造科技成果共享平台显示正确
        commen.find_ele(By.XPATH, ".//*[contains(text(),'推荐科技成果')]")
        commen.time.sleep(1)


        #验证更多科技成果跳转正确
        commen.click_ele(By.XPATH,".//span[contains(text(),'更多科技成果')]")
        commen.time.sleep(1)
        commen.find_ele(By.XPATH,".//a[contains(text(),'科技成果列表')]")

        #验证科技成果详情页跳转正确
        commen.click_ele(By.XPATH,".//li/div[@class='seal-flex']")
        commen.find_ele(By.XPATH,".//li/a[contains(text(),'科技成果详情')]")

    # 科技成果共享平台——转让成果首页展示——更多转让成果跳转——转让成果列表展示——转让成果详情页展示
    def test_cession_achievements(self):
        commen.time.sleep(1)
        # 验证协同制造科技成果共享平台跳转
        commen.find_ele(By.XPATH, ".//*[contains(text(),'协同制造')]").click()
        commen.time.sleep(1)
        commen.init_driver().find_element_by_link_text("科技成果共享平台").click()
        commen.time.sleep(1)

        # 验证协同制造科技成果共享平台显示正确
        commen.find_ele(By.XPATH, ".//*[contains(text(),'推荐科技成果共享')]")
        commen.time.sleep(1)

        #验证更多转让成果跳转
        commen.click_ele(By.XPATH,".//span[contains(text(),'更多转让成果')]")
        commen.time.sleep(1)
        commen.find_ele(By.XPATH,".//a[contains(text(),'科技成果列表')]")

        #验证科技成果详情页面跳转
        commen.click_ele(By.XPATH,".//li/div[@class='seal-flex']")
        commen.time.sleep(1)
        commen.find_ele(By.XPATH,".//div[contains(text(),'服务商客服')]")

    # 公共服务共享平台——公共服务首页展示——更多融资项目跳转——融资项目列表展示——融资项目详情页展示
    def test_public_service(self):
        commen.time.sleep(1)
        # 验证协同制造公共服务共享平台跳转
        commen.find_ele(By.XPATH, ".//*[contains(text(),'协同制造')]").click()
        commen.time.sleep(1)
        commen.init_driver().find_element_by_link_text("公共服务共享平台").click()
        commen.time.sleep(1)
        commen.find_ele(By.XPATH,".//*[contains(text(),'公共服务-融资项目库')]")


        #验证更多融资项目跳转
        commen.click_ele(By.XPATH,".//span[contains(text(),'更多融资项目')]")
        commen.time.sleep(1)
        commen.find_ele(By.XPATH,".//a[contains(text(),'项目列表')]")

        #验证更多融资项目详情页跳转
        commen.click_ele(By.XPATH,".//li/div[@class='seal-flex']")
        commen.time.sleep(1)
        commen.find_ele(By.XPATH,".//a[contains(text(),'项目详情')]")



