from selenium.webdriver.common.by import By
import time,allure


class BaseAction:
    # 当类初始化的时候这个方法就执行?
    def __init__(self,driver):
        self.driver = driver

    #点击元素
    def click_element(self,loc):
        self.find_element(loc).click()

    # 向输入框输入内容
    def send_element_content(self,loc,content):
        self.find_element(loc).clear()
        self.find_element(loc).send_keys(content)


    """
    找到一个元素对象 返回
    """

    def find_element(self,loc):
        time.sleep(1)
        return self.driver.find_element(loc[0],loc[1])

    """
    找到一组元素对象  返回
    """
    def find_elements(self,loc):
        time.sleep(1)
        return self.driver.find_elements(loc[0],loc[1])

    @allure.step("获取弹窗内容")
    def get_toast_message(self,message):
        toast_xpath = "//*[contains(@text(),'{}')]".format(message)
        toast_message = self.find_element(By.XPATH,toast_xpath).text
        return toast_message

    #截图
    def get_screen(self):
        #截图名称
        png_name = "./screen/{}.png".format(int(time.time()))
        self.driver.get_screenshot_as_file(png_name)

        with open("abc.png","rb") as f:
            allure.attach("截图名字",f.read(),allure.attach_type.PNG)


