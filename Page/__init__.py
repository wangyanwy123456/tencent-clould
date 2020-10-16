from selenium.webdriver.common.by import By


#该页面保存常用元素的定位方式
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


"""
注册页
"""
new_user_register = By.XPATH,".//a[contains(text(),'新用户注册')]"
