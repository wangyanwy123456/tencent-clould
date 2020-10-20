#此页面写的是航空服务号模块的用例
import os, sys
sys.path.append(os.getcwd())
# import pytest
from Commen import commen
from Commen import commen_console
from Commen import commen_admin
from selenium.webdriver.common.by import By
import allure
import pytest

#控制台中的元素
upload_logo = [By.XPATH,".//input[@class='upload-img__input']"]     #上传logo
create_fig = [By.XPATH, ".// button[contains(text(), '生成图片')]"]     #生成图片
slogan_input = [By.XPATH,".//input[@placeholder='请填写slogan，不超过20个字']"]      #输入标语
brief_input = [By.XPATH,".//textarea[@placeholder='请填写介绍，不超过800个字']"]      #输入简介
website_input = [By.XPATH,".//input[@placeholder='请填写官方地址']"]       #输入官网
domain_input = [By.XPATH,".//input[@placeholder='例如输入：aviclouds']"]     #输入域名
email_input = [By.XPATH,".//input[@placeholder='请填写邮箱']"]            #输入邮箱
address_choose_1 = [By.XPATH,".//input/..//i"]           #选择地址
# address_choose_province = [By.XPATH,".//li/div[contains(text(),'{}')]".format(province)]
province_ele = [By.XPATH,".//a[contains(text(),'省份')]"]          #省份tab
city_ele = [By.XPATH,".//a[contains(text(),'城市')]"]              #城市tab
address_input = [By.XPATH,".//input[@placeholder='输入文本内容']"]      #输入详细地址
phone_input = [By.XPATH,".//input[@placeholder='请填写联系电话']"]         #输入电话
credit_code_input = [By.XPATH,".//div[contains(text(),'请填写18位统一社会信用代码或者组织机构代码')]/../input"]      #输入统一社会信用代码
commit_verify = [By.XPATH,".//button[contains(text(),'提交审核')]"]     #提交审核
commit_success = [By.XPATH,".//h3[contains(text(),'提交成功')]"]        #提交成功


edit = (By.XPATH,".//button[contains(text(),'编辑')]")                  #编辑
update = (By.XPATH,".//button[contains(text(),'更新')]")                #更新
basic_information_manage = [By.XPATH,".//h2[contains(text(),'基本信息管理')]"]         #基本信息管理
basic_information = [By.XPATH,".//a[contains(text(),'基本信息')]"]           #基本信息


#admin管理后台的元素
virify_title = [By.XPATH,".//h2[contains(text(),'企业与机构审核')]"]     #企业与机构审核
virifing = [By.XPATH,".//a[contains(text(),'审核中')]"]           #审核中
finish_virify = [By.XPATH,".//a[contains(text(),'已完成审核')]"]       #已完成审核
left_bussyniss_virify = [By.XPATH,".//span[contains(text(),'企业与机构审核')]"]    #左侧侧边栏标题_企业与机构审核
reject_reason = [By.XPATH,".//h3[contains(text(),'请输入驳回原因')]"]
reject_reason_input = [By.XPATH,".//textarea[@placeholder='请输入驳回原因']"]      #驳回原因输入框
confirm_button = [By.XPATH,".//button[contains(text(),'确定')]"]                   #确定按钮



#该类写的是航空服务号模块的用例
class Test_Voyage_Service:
    # 登陆浏览器
    # def setup_class(self):
    #     commen_console.login_console()

    # 退出浏览器
    def teardown_class(self):
        commen.init_driver().quit()

    #控制台编辑航空服务号
    def open_voyage_service(self,file,slogan,brief,website,domain,email,province,city,address,phone,code):
        commen.find_ele(By.XPATH,".//h2[contains(text(),'开通航空服务号')]")
        commen.click_ele(By.XPATH,".// button[contains(text(), '立即开通')]")
        commen.find_ele(upload_logo[0],upload_logo[1]).send_keys("D:\\tencent-clould\\Resource\\fig\\{}" .format(file))    #上传logo
        commen.click_ele(create_fig[0], create_fig[1])                #生成图片
        commen.send_text(slogan_input[0],slogan_input[1],slogan)         #输入标语
        commen.send_text(brief_input[0], brief_input[1], brief)          #输入简介
        commen.send_text(website_input[0], website_input[1], website)       #输入官网
        commen.send_text(domain_input[0],domain_input[1],domain)         #输入域名
        commen.send_text(email_input[0], email_input[1], email)          #输入邮箱
        commen.click_ele(address_choose_1[0], address_choose_1[1])       #点击地址选择框
        commen.click_ele(province_ele[0], province_ele[1])  # 点击省份tab
        commen.click_ele(By.XPATH,".//li/div[contains(text(),'{}')]".format(province))     #选择省
        commen.click_ele(city_ele[0], city_ele[1])  # 点击城市tab
        commen.click_ele(By.XPATH, ".//li/div[contains(text(),'{}')]".format(city))  # 选择市
        commen.send_text(address_input[0], address_input[1], address)          #输入详细地址
        commen.send_text(phone_input[0], phone_input[1], phone)  # 输入电话
        commen.send_text(credit_code_input[0],credit_code_input[1],code)       #输入统一社会信用代码
        commen.click_ele(commit_verify[0],commit_verify[1])            #点击提交审核
        commen.click_act("确定提交审核么","确定")             #确认提交审核
        commen.find_ele(commit_success[0],commit_success[1])        #提交审核成功后出现的提示
        commen.find_ele(commit_success[0], commit_success[1])  # 提交审核成功后出现的提示


    #编辑航空服务号
    def edit_voyage_service(self, file, slogan, brief, website, domain, email, province, city, address, phone, code):
        commen.find_ele(basic_information_manage[0],basic_information_manage[1])          #基本信息管理
        commen.click_ele(basic_information[0],basic_information[1])          #点击基本信息tab
        commen.click_ele(edit[0],edit[1])        #点击编辑
        commen.find_ele(upload_logo[0], upload_logo[1]).send_keys("D:\\tencent-clould\\Resource\\fig\\{}".format(file))  # 上传logo
        commen.click_ele(create_fig[0], create_fig[1])  # 生成图片
        commen.send_text(slogan_input[0], slogan_input[1], slogan)  # 输入标语
        commen.send_text(brief_input[0], brief_input[1], brief)  # 输入简介
        commen.send_text(website_input[0], website_input[1], website)  # 输入官网
        commen.send_text(domain_input[0], domain_input[1], domain)  # 输入域名
        commen.send_text(email_input[0], email_input[1], email)  # 输入邮箱
        commen.click_ele(address_choose_1[0], address_choose_1[1])  # 点击地址选择框
        commen.click_ele(province_ele[0], province_ele[1])  # 点击省份tab
        commen.click_ele(By.XPATH, ".//li/div[contains(text(),'{}')]".format(province))  # 选择省
        commen.click_ele(city_ele[0], city_ele[1])  # 点击城市tab
        commen.click_ele(By.XPATH, ".//li/div[contains(text(),'{}')]".format(city))  # 选择市
        commen.send_text(address_input[0], address_input[1], address)  # 输入详细地址
        commen.send_text(phone_input[0], phone_input[1], phone)  # 输入电话
        commen.send_text(credit_code_input[0], credit_code_input[1], code)  # 输入统一社会信用代码
        commen.click_ele(update[0],update[1])


    #admin审核航空服务号:驳回
    def admin_reject_voyage_service(self,status,name,act,reject_reason_text,status_1):
        commen.click_ele(By.LINK_TEXT, "航空服务号")
        commen.click_ele(left_bussyniss_virify[0],left_bussyniss_virify[1])
        commen.find_ele(virify_title[0],virify_title[1])
        commen.click_ele(virifing[0],virifing[1])      #点击审核中
        commen.find_ele(By.XPATH,".//td/div/span[@title='{}']/../../../td/div/span[contains(text(),'{}')]".format(status,name))      #判断列表中的状态
        #执行操作:同意/驳回/查看详情
        commen.click_ele(By.XPATH,".//td/div/span[@title='{}']/../../../td/div/button[contains(text(),'{}')]".format(name,act))
        commen.find_ele(reject_reason[0],reject_reason[1])
        commen.send_text(reject_reason_input[0],reject_reason_input[1],reject_reason_text)
        commen.click_ele(confirm_button[0],confirm_button[1])         #点击确定按钮
        commen.click_ele(finish_virify[0],finish_virify[1])       #点击已完成审核,进入已完成审核列表
        commen.find_ele(By.XPATH,".//td/div/span[@title='{}']/../../../td/div/span[contains(text(),'{}')]".format(status_1,name))    #判断列表中的状态

    # admin审核航空服务号:同意
    def admin_agree_voyage_service(self, status, name, act, status_1,):
        commen.click_ele(By.LINK_TEXT, "航空服务号")
        commen.click_ele(left_bussyniss_virify[0], left_bussyniss_virify[1])
        commen.find_ele(virify_title[0], virify_title[1])
        commen.click_ele(virifing[0], virifing[1])  # 点击审核中
        commen.find_ele(By.XPATH,".//td/div/span[@title='{}']/../../../td/div/span[contains(text(),'{}')]".format(status,name))
        # 执行操作:同意//查看详情
        commen.click_ele(By.XPATH,".//td/div/span[@title='{}']/../../../td/div/button[contains(text(),'{}')]".format(name, act))
        commen.click_act("确定同意该申请吗","确认" )
        commen.click_ele(finish_virify[0], finish_virify[1])  # 点击已完成审核,进入已完成审核列表
        commen.find_ele(By.XPATH,".//td/div/span[@title='{}']/../../../td/div/span[contains(text(),'{}')]".format(status_1,name))  # 判断列表中的状态


    def delete_voyage_service(self,status,name,act):
        commen.click_ele(By.LINK_TEXT, "航空服务号")
        commen.click_ele(left_bussyniss_virify[0], left_bussyniss_virify[1])
        commen.find_ele(virify_title[0], virify_title[1])
        commen.click_ele(finish_virify[0],finish_virify[1])       #点击已完成审核
        commen.find_ele(By.XPATH,".//td/div/span[@title='{}']/../../../td/div/span[contains(text(),'{}')]".format(status,name))    # 判断列表中的状态
        commen.click_ele(By.XPATH,".//td/div/span[@title='{}']/../../../td/div/div/button[contains(text(),'{}')]".format(name,act))      #点击删除
        commen.click_act("确定删除该航空服务号吗", "确定删除")
        commen.find_ele(By.XPATH,".//*[contains(text(),'删除成功')]")       #出现删除成功的提示


    def test_voyage_service(self):
        commen.click_ele(By.LINK_TEXT,"航空服务号")
        test_voyage_service.open_voyage_service("机构logo_1.jpg","越努力,越幸运","这是一条简介","https://www.muchenit.com","123456abc","1111@163.com","广东","广州","天河区","13976691459","460004198546595236")
        commen_admin.login_admin()
        test_voyage_service.admin_reject_voyage_service("审核中", "企业人工认证", "驳回", "填写不规范;请重新填写", "审核驳回")
        test_voyage_service.edit_voyage_service("机构logo_2.png", "编辑越努力,越幸运", "编辑这是一条简介", "https://www.muchenit111.com",
                                                "bianji123456abc",
                                                "bianji1111@163.com", "海南", "海口", "龙华区", "18459190322",
                                                "200004198546595236")
        commen_admin.login_admin()
        test_voyage_service.admin_agree_voyage_service("审核中", "和大家更好的结构化", "同意", "已开通")
        test_voyage_service.delete_voyage_service("已开通", "和大家更好的结构化", "删除")



test_voyage_service=Test_Voyage_Service()







