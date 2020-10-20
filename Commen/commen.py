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


"""
#浏览器
"""
driver = webdriver.Firefox()
Action=ActionChains(driver)

#初始化driver对象
def init_driver():
    driver.maximize_window()
    time.sleep(1)
    return driver


#判断获取的元素数量
def get_ele_lenth(count_ele,by_method,ele_xpath):
    eles = init_driver().find_elements(by_method,ele_xpath)
    count = len(eles)
    print(count)
    assert count_ele == count

#判断元素文本是否包含
def get_ele_text(by_method,ele_xpath,text):
    ele_text = init_driver().find_element(by_method,ele_xpath).text
    assert text in ele_text
    return ele_text

#元素跳转
def click_ele(by_method,ele_xpath):
    init_driver().find_element(by_method,ele_xpath).click()
    time.sleep(1)


#验证元素存在
# def find_ele(by_method,ele_xpath):
#     ele = init_driver().find_element(by_method,ele_xpath)
#     return ele


#在指定时间内查找元素
def find_ele(by_method,ele_xpath):
    # WebDriverWait(init_driver(), 10).until(EC.presence_of_element_located((by_method, ele_xpath)))
    init_driver().implicitly_wait(10)
    ele = init_driver().find_element(by_method, ele_xpath)
    return ele

#输入文本
def send_text(by_method,ele_xpath,text):
    ele=find_ele(by_method,ele_xpath)
    ele.send_keys(Keys.CONTROL, 'a')
    time.sleep(2)
    ele.send_keys(text)
    time.sleep(0.5)


#从一组元素中找到某一个元素
def find_one_ele(by_method,ele_xpath,num):
    ele_list = init_driver().find_elements(by_method,ele_xpath)
    ele = ele_list[num]
    return ele

#点击确认或取消
def click_act(name,act):
    find_ele(By.XPATH,".//*[contains(text(),'{}')]".format(name))
    click_ele(By.XPATH,".//button[contains(text(),'{}')]".format(act))





