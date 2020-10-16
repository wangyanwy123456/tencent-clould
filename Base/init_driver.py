from selenium import webdriver

"""
初始化driver对象
"""
def get_driver():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    return driver



