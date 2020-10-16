#此页面写的是协同制造模块的用例
import os, sys
sys.path.append(os.getcwd())
# import pytest
from Commen import commen
from Commen import commen_console
from Commen import commen_admin
from selenium.webdriver.common.by import By

province = '海南省'
city = '海口市'
area = '龙华区'


countrywide_xpath= ".//button[contains(text(),'全国')]"
other_city = ".//button[contains(text(),'其他城市')]"

#控制台状态
draft_status= '草稿'
commit_status= '已提交'
release_status='已发布'

#控制台操作
move = '移除'
edit = "编辑"
check_reason = "查看驳回的原因"
undercarriage_console = "下架"
cancel = "撤销"



#sp操作
reject = ".//a[contains(text(),'驳回')]"         #驳回
agree =".//a[contains(text(),'同意')]"           #同意
undercarriage = ".//a[contains(text(),'下架')]"       #下架





#新增发布需求
def add_fictitious_needs(status, item_name):
    commen.init_driver().switch_to.default_content()
    commen.init_driver().switch_to.frame(1)
    commen.time.sleep(3)
    commen.find_one_ele(By.XPATH, ".//input", 0).send_keys(item_name)  # 输入项目名称
    commen.find_one_ele(By.XPATH, ".//input", 1).send_keys("需求概述001")  # 输入需求概述
    commen.find_ele(By.XPATH, ".//button[contains(text(),'一口价')]").click()  # 选择项目预算
    commen.find_one_ele(By.XPATH, ".//input", 2).send_keys("99")  # 输入项目预算
    commen.find_ele(By.XPATH, ".//button[contains(text(),'线上交易')]").click()  # 选择交易方式
    commen.click_ele(By.XPATH, ".//a[contains(text(),'从通讯录获取')]")  # 点击从通讯录获取
    commen.find_ele(By.XPATH, ".//strong[contains(text(),'通讯录')]")
    commen.click_ele(By.XPATH, ".//input[@type='checkbox']")  # 点击选择联系人
    commen.time.sleep(1)
    commen.find_one_ele(By.XPATH, ".//button[contains(text(),'确定')]",1).click()  # 点击确定
    commen.time.sleep(1)
    commen.click_ele(By.XPATH, ".//a[contains(text(),'全部')]")
    commen.click_ele(By.XPATH, ".//a[contains(text(),'{}')]".format(province))  # 选择省
    commen.time.sleep(1)
    # commen.click_ele(By.XPATH, ".//a[contains(text(),'全部')]")
    # commen.time.sleep(1)
    # commen.click_ele(By.XPATH, ".//a[contains(text(),'{}')]".format(city))  # 选择市
    # commen.time.sleep(1)
    # commen.click_ele(By.XPATH, ".//a[contains(text(),'全部')]")
    # commen.time.sleep(1)
    # commen.click_ele(By.XPATH, ".//a[contains(text(),'{}')]" .format(area))  # 选择区
    commen.send_text(By.XPATH, "//div[@class='notranslate public-DraftEditor-content']", "需求详情111")
    commen.time.sleep(1)
    commen.click_ele(By.XPATH, ".//button[contains(text(),'下一步')]")  # 点击下一步
    commen.time.sleep(1)
    commen.find_one_ele(By.XPATH, ".//a[@role='menuitem']", 1)  # 选择接包对象
    # 默认选择其他的选项
    commen.click_ele(By.XPATH, ".//button[contains(text(),'完成')]")  # 点击完成
    commen.time.sleep(5)
    commen.find_ele(By.XPATH, ".//h4[contains(text(),'需求提交成功')]")  # 验证需求提交成功
    commen.click_ele(By.XPATH, ".//button[contains(text(),'返回需求列表')]")  # 点击返回需求列表
    commen.init_driver().switch_to.default_content()
    commen.init_driver().switch_to.frame(1)
    commen.time.sleep(5)
    commen.find_ele(By.XPATH, ".//h2[contains(text(),'需求列表')]")
    commen.find_ele(By.XPATH, ".//td/div[contains(text(),'{}')]/../../td/div[@title='{}']".format(status, item_name))

def console_act_need(status, item_name,act):
    commen.click_ele(By.XPATH,".//a/span[contains(text(),'需求列表')]")
    commen.init_driver().switch_to.frame(1)
    commen.find_ele(By.XPATH, ".//td/div[contains(text(),'{}')]/../../td/div[@title='{}']".format(status, item_name))
    # 点击编辑/移除/下架/撤销
    commen.click_ele(By.XPATH, ".//td/div[@title='{}']/../../td/div/a[contains(text(),'{}')]".format(item_name, act))




#验证点击新建跳转到发布需求页面
def new_need():
    commen.click_ele(By.XPATH,".//button[contains(text(),'新建')]")           #点击新建
    commen.init_driver().switch_to.default_content()
    commen.init_driver().switch_to.frame(1)
    commen.find_ele(By.XPATH,".//h2[contains(text(),'发布')]")


#admin审核需求
def audit_need(status, item_name,act):
    commen.click_ele(By.LINK_TEXT,"协同制造")
    commen.init_driver().switch_to.frame(1)
    commen.find_ele(By.XPATH,".//h2[contains(text(),'需求审核')]")
    commen.find_ele(By.XPATH,".//td/div[contains(text(),'{}')]/../../td/div[@title='{}']".format(status,item_name))
    commen.click_ele(By.XPATH,".//td/div[@title='{}']/../../td/div/a[contains(text(),'{}')]".format(item_name,act))
    commen.time.sleep(1)



    # if commen.find_ele(By.XPATH,".//strong[contains(text(),'请输入驳回此需求的原因')]")==True:
    #     commen.send_text(By.XPATH,".//textarea","填写内容不规范;请严格按照规范内容进行填写")
    #     commen.click_ele(By.XPATH,".//button[@class='tc-15-btn']")       #点击提交
    # else:
    #     commen.click_ele(By.XPATH,".//button[@class='tc-15-btn']")       #点击同意




#该类写的是协同制造供需服务管理模块的用例
class Test_Supply_Demand_Service:
    # 登陆浏览器
    def setup_class(self):
        commen_console.login_console()

    # 退出浏览器
    def teardown_class(self):
        commen.init_driver().quit()


    # 1）发布虚拟需求——返回需求列表——需求列表中展示已发布的需求、查询需求、新建需求页面跳转
    # sp平台——需求评审——驳回需求——控制台——编辑需求——同意需求——需求详情页跳转——下架需求
    def test_fictitious_needs(self):
        #点击协同制造
        commen.click_ele(By.LINK_TEXT,"协同制造")
        commen.get_ele_text(By.XPATH,".//h2[@class='qc-aside-headline']/span","协同制造")
        add_fictitious_needs(commit_status,"小牛测试公司的需求")           #发布需求
        new_need()                                                  #点击新建
        commen_admin.login_admin()
        audit_need("审核中","小牛测试公司的需求","同意")


# 7.供应商认证
# 1)企业用户供应商申请——admin审核驳回供应商——控制台重新编辑供应商并提交——供应商审核成功
class Test_Supplier_Attestation():           #该类写的是供应商认证的用例


    def setup_class(self):
        commen_console.login_console()

    # 退出浏览器
    def teardown_class(self):
        commen.init_driver().quit()

    #申请成为供应商
    def supplier_apply(self,file,file_1,file_2):
        commen.init_driver().switch_to.default_content()
        commen.init_driver().switch_to.frame(1)
        commen.find_ele(By.XPATH,".//h2[contains(text(), '成为供应商')]")
        commen.find_ele(By.XPATH,".//input[@class='upload-img__input']").send_keys("D:\\tencent-clould\\Resource\\fig\\{}" .format(file))        #上传机构Logo
        commen.click_ele(By.XPATH,".// button[contains(text(), '生成图片')]")
        commen.find_ele(By.XPATH,".// span[contains(text(), '添加文件')] /../ input[@type = 'file']").send_keys("D:\\tencent-clould\\Resource\\fig\\{}".format(file_1))     #上传审核资质文件
        commen.find_one_ele(By.XPATH,".//input[@class='upload-img__input']",1).send_keys('D:\\tencent-clould\\Resource\\fig\{}'.format(file_2))     #上传介绍页展示图
        commen.click_ele(By.XPATH, ".// button[contains(text(), '生成图片')]")
        commen.send_text(By.XPATH,".//textarea[@class='tc-15-input-textarea']","能力描述6666")     #输入能力描述
        commen.click_ele(By.XPATH,".//button[contains(text(),'下一步')]")
        commen.find_one_ele(By.XPATH,".//input",0).send_keys("18419371389")       #输入手机号
        commen.find_one_ele(By.XPATH, ".//input", 1).send_keys("3695098641@qq.com")      #输入邮箱
        commen.click_ele(By.XPATH,".//button[contains(text(),'提交')]")           #点击提交
        commen.find_ele(By.XPATH,".//h4[@class='media-heading']")                 #显示提交成功提示语

    #编辑供应商
    def edit_supplier_apply(self,file,file_1,file_2,tel,email):
        commen.click_ele(By.LINK_TEXT, "协同制造")
        commen.click_ele(By.XPATH, ".//span[contains(text(),'供应商认证')]")
        commen.init_driver().switch_to.default_content()
        commen.init_driver().switch_to.frame(1)
        commen.find_ele(By.XPATH, ".//h2[contains(text(), '供应商信息')]")
        commen.click_ele(By.XPATH, ".//a[contains(text(), '编辑')]")
        commen.find_ele(By.XPATH, ".//input[@class='upload-img__input']").send_keys("D:\\tencent-clould\\Resource\\fig\\{}".format(file))  # 上传机构Logo
        commen.click_ele(By.XPATH, ".// button[contains(text(), '生成图片')]")
        commen.find_ele(By.XPATH, ".// span[contains(text(), '添加文件')] /../ input[@type = 'file']").send_keys("D:\\tencent-clould\\Resource\\fig\\{}".format(file_1))  # 上传审核资质文件
        commen.find_one_ele(By.XPATH, ".//input[@class='upload-img__input']", 1).send_keys( 'D:\\tencent-clould\\Resource\\fig\{}'.format(file_2))  # 上传介绍页展示图
        commen.click_ele(By.XPATH, ".// button[contains(text(), '生成图片')]")
        commen.send_text(By.XPATH, ".//textarea[@class='tc-15-input-textarea']", "能力描述6666")  # 输入能力描述
        commen.click_ele(By.XPATH, ".//button[contains(text(),'下一步')]")
        commen.find_one_ele(By.XPATH, ".//input", 0).clear()
        commen.find_one_ele(By.XPATH, ".//input", 0).send_keys(tel)  # 输入手机号
        commen.find_one_ele(By.XPATH, ".//input", 1).clear()
        commen.find_one_ele(By.XPATH, ".//input", 1).send_keys(email)  # 输入邮箱
        commen.click_ele(By.XPATH, ".//button[contains(text(),'提交')]")  # 点击提交
        commen.find_ele(By.XPATH, ".//h4[@class='media-heading']")  # 显示提交成功提示语


    #sp审核供应商
    def sp_verify_supplier(self,status, item_name,act):
        commen.click_ele(By.LINK_TEXT, "协同制造")
        # commen.click_ele(By.XPATH,".//span[contains(text(),'供需服务管理')]")
        commen.click_ele(By.XPATH,".//span[contains(text(),'供应商审核')]")
        commen.init_driver().switch_to.default_content()
        commen.init_driver().switch_to.frame(1)
        commen.find_ele(By.XPATH, ".//h2[contains(text(),'供应商审核')]")
        commen.find_ele(By.XPATH, ".//td/div[@title='{}']/../../td/div[@title='{}']".format(status, item_name))
        commen.click_ele(By.XPATH,".//td/div[@title='{}']/../../td/div/a[contains(text(),'{}')]".format(item_name, act))
        commen.time.sleep(1)
        commen_console.click_act("和大家更好的结构化","确认")


    def test_supplier_apply(self):
        #点击协同制造
        commen.click_ele(By.LINK_TEXT,"协同制造")
        commen.click_ele(By.XPATH,".//span[contains(text(),'供应商认证')]")
        supplier_attestation.supplier_apply("机构logo_1.jpg","机构logo_2.png","机构logo_1.jpg")

    # 1)企业用户供应商申请——admin审核驳回供应商——控制台重新编辑供应商并提交——供应商审核成功
    def test_sp_verify_supplier(self):
        supplier_attestation.edit_supplier_apply("机构logo_1.jpg","机构logo_2.png","机构logo_1.jpg","15610998854","565656@qq.com")
        commen_admin.login_admin()
        supplier_attestation.sp_verify_supplier("审核中","和大家更好的结构化","同意")


supplier_attestation = Test_Supplier_Attestation()







