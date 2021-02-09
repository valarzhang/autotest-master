import numpy as np
import unittest
from selenium import webdriver
from time import sleep
import variable
from PO.role import Role
from BasePage import wait_element
from configparser import ConfigParser
from BasePage import skip_dependon

class MyTestCase(unittest.TestCase):
    #全局前置，最新运行，只运行一次
    @classmethod
    def setUpClass(cls):
        conf = ConfigParser()
        conf.read("../cfginfo.ini", encoding="utf-8")
        conf.sections()
        url = conf.get('URL', 'url')
        cls.homeUrl = conf.get('URL', 'homeUrl')
        username = conf.get('LOGIN', 'username')
        password = conf.get('LOGIN', 'password')
        checkKey = conf.get('LOGIN', 'checkKey')
        cls.rolename = conf.get('ROLE', 'rolename')
        cls.rolename2 = conf.get('ROLE', 'rolename2')
        cls.sort1 = conf.get('ROLE', 'sort1')
        cls.remarks = conf.get('ROLE','remarks')
        cls.sort4 = conf.get('ROLE', 'sort4')


        print("开始执行部门管理脚本")
        dr = webdriver.Chrome()            #启动chrom浏览器
        cls.dr = dr
        print("登陆统一开发平台")
        dr.get(url)              #打开统一平台地址
        dr.maximize_window()              #将浏览器最大化
        variable.login(dr,username,password,checkKey)                #输入用户名、密码、验证码后登陆
        for i in range(10):
            if dr.current_url == cls.homeUrl:
                break
            else:
                print("登陆等待中...")
                sleep(2)

    #全局后置，最后运行，只运行一次
    @classmethod
    def tearDownClass(cls):
        print("结束执行部门管理脚本")
        cls.dr.quit()                     #关闭chrom浏览器

    def setUp(self):
        dr = self.dr
        self.assertEqual(dr.current_url,self.homeUrl,msg="登陆平台异常")#检查登陆是否成功或页面刷新后是否返回首页
        print("当前处于首页状态")
        #点击系统管理按钮
        Role(dr).sys_manger_btn.click()
        print("点击左侧菜单’系统管理‘")
        sleep(1)
        #点击部门管理标签页
        wait_element(self.dr, 'By.LINK_TEXT', u"用户管理").click()
        print("点击左侧菜单’角色管理‘")


    def tearDown(self):
        print("刷新页面，返回首页")
        self.dr.refresh() #刷新页面，返回首页
        sleep(1)


    # def test_1_init(self):
    #     print("-------------------------开始执行第一条用例：数据检查----------------------------------")
    #     dr = self.dr
    #     #定位到树形结构所属的iframe
    #     dr.switch_to.frame(Role(dr).iframe_sw[1])
    #     sleep(1)
    #     print("检查初始页面，左侧的一级角色与列表中展示的一级角色是否一致")
    #     rx=Role(dr).tree_level1
    #     tree = []
    #     print("开始获取左侧一级角色")
    #     for i in range(len(rx)):
    #         tree.append(rx[i].get_attribute('textContent'))
    #     tx = variable.get_table(dr)
    #     table = []
    #     print("开始获取列表中一级角色")
    #     for i in range(len(tx)):
    #         table.append(tx[i][0])
    #
    #     self.assertEqual(tree,table,msg="左侧结构图中的角色与列表中的角色不一致")
    #     print("左侧结构图中的角色与列表中的角色一致")


    def test_2_add(self):
        print("-------------------------开始执行第二条用例：添加一级角色----------------------------------")
        dr = self.dr
        self.dr.switch_to.frame(Role(self.dr).iframe_sw[1])
        sleep(1)
        wait_element(self.dr,'By.CSS_SELECTOR',"button[lay-event='add']").click()
        sleep(1)
        wait_element(self.dr,'By.CSS_SELECTOR',"a[class='layui-layer-btn1']").click()
        sleep(15)









