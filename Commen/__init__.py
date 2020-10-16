from selenium.webdriver.common.by import By
from selenium import webdriver

"""
首页
"""
#登录按钮
homepage_login = By.XPATH,".//a[@data-report='homepage_login']"
#注册按钮
homepage_register= By.XPATH,".//a[data-report='homepage_register']"


"""
登录页
"""
#请使用微信扫一扫
wechat_scan = By.XPATH,".//div[contains(text(),'请使用微信扫一扫登录')]"
#邮箱登陆
email_login = By.XPATH,".//button[1]"
#子用户登陆
child_user_login = By.XPATH,"./*[contains(text(),'子用户登录')]"
#用户名输入框
username_input = By.XPATH,".//input[@placeholder='邮箱地址']"
#密码输入框
password_input = By.XPATH,".//input[@placeholder='密码']"


"""
注册页
"""
new_user_register = By.XPATH,".//a[contains(text(),'新用户注册')]"


#用户名
username_busyness = "wy1185095441@163.com"
#密码
pwd_busyness = "506019wy"