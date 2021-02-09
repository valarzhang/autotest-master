import unittest,time
from selenium import webdriver
from time import sleep
import variable
from PO.role import Role
from BeautifulReport import BeautifulReport
from PO.user import User
from BasePage import wait_element
from configparser import ConfigParser
from BasePage import skip_dependon
import numpy as np
from db_fixture import test_dataForRole
import os
from BeautifulReport import BeautifulReport

class RoleTestCase(unittest.TestCase):

    #全局前置，最新运行，只运行一次
    @classmethod
    def setUpClass(cls):
        test_dataForRole.clear_data()
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        conf = ConfigParser()
        conf.read(os.path.join(BASE_DIR, 'cfginfo.ini'), encoding='utf-8')
        conf.sections()
        cls.url = conf.get('URL', 'url')
        cls.homeUrl = conf.get('URL', 'homeUrl')
        username = conf.get('LOGIN', 'username')
        cls.password = conf.get('LOGIN', 'password')
        cls.checkKey = conf.get('LOGIN', 'checkKey')
        cls.rolename = conf.get('ROLE', 'rolename')
        cls.rolename2 = conf.get('ROLE', 'rolename2')
        cls.rolename3 = conf.get('ROLE', 'rolename3')
        cls.rolename4 = conf.get('ROLE', 'rolename4')
        cls.rolename5 = conf.get('ROLE', 'rolename5')
        cls.sort1 = conf.get('ROLE', 'sort1')
        cls.remarks = conf.get('ROLE','remarks')
        cls.sort4 = conf.get('ROLE', 'sort4')
        cls.user1 = conf.get('ROLE', 'user1')
        cls.departname = conf.get('ROLE', 'departnamesql')

        print("通过数据库新增角色"+cls.rolename3+"，部门："+cls.departname+"，用户："+cls.user1)
        test_dataForRole.init_data()

        print("开始执行角色管理脚本")
        dr =webdriver.Chrome()            #启动chrom浏览器
        cls.dr = dr
        print("登陆统一开发平台")
        dr.get(cls.url)              #打开统一平台地址
        dr.maximize_window()              #将浏览器最大化
        variable.login(dr,username,cls.password,cls.checkKey)                #输入用户名、密码、验证码后登陆
        for i in range(10):
            if dr.current_url == cls.homeUrl:
                break
            else:
                print("登陆等待中...")
        sleep(2)

    #全局后置，最后运行，只运行一次
    @classmethod
    def tearDownClass(cls):
        print("结束执行角色管理脚本")
        cls.dr.quit()                     #关闭chrom浏览器
        test_dataForRole.clear_data()

    def save_img(self, img_name):
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"./img"), img_name))

    def setUp(self):
        print(time.strftime("%Y_%m_%d_%H_%M_%S"))
        dr = self.dr
        self.assertEqual(dr.current_url,self.homeUrl,msg="登陆平台异常")#检查登陆是否成功或页面刷新后是否返回首页
        print("当前处于首页状态")
        #点击系统管理按钮
        Role(dr).sys_manger_btn.click()
        print("点击左侧菜单’系统管理‘")
        sleep(2)
        #点击部门管理标签页
        Role(dr).role_btn.click()
        print("点击左侧菜单’角色管理‘")
        sleep(1)
        #检查是否打开部门管理标签页
        self.assertNotEqual(Role(dr).curr_lable,False,msg="未打开角色管理标签页")
        self.assertEqual(Role(dr).curr_lable.get_attribute('textContent'),'角色管理',msg="打开的不是角色管理标签页")

    def tearDown(self):
        print("刷新页面，返回首页")
        print(time.strftime("%Y_%m_%d_%H_%M_%S"))
        self.dr.refresh() #刷新页面，返回首页
        sleep(1)

    @BeautifulReport.add_test_img("test_1_roleinit")
    def test_1_roleinit(self):
        """初始数据验证"""
        dr = self.dr
        #定位到树形结构所属的iframe
        dr.switch_to.frame(Role(dr).iframe_sw[1])
        sleep(1)
        print("检查初始页面，左侧的一级角色与列表中展示的一级角色是否一致")
        rx=Role(dr).tree_level1
        tree = []
        print("开始获取左侧一级角色")
        for i in range(len(rx)):
            tree.append(rx[i].get_attribute('title'))
        tx = variable.get_table(dr)
        table = []
        print("开始获取列表中一级角色")
        for i in range(len(tx)):
            table.append(tx[i][0])

        self.assertEqual(tree,table,msg="左侧结构图中的角色与列表中的角色不一致")
        print("左侧结构图中的角色与列表中的角色一致")

    @BeautifulReport.add_test_img("test_2_addrole")
    def test_2_addrole(self):
        """添加一级角色"""
        dr = self.dr
        self.dr.switch_to.frame(Role(self.dr).iframe_sw[1])
        sleep(1)
        Role(dr).role_add(rolename=self.rolename,sort=self.sort1,remarks=self.remarks)
        try:
            text = Role(dr).toast_info.get_attribute('textContent')  #info消息偶尔会定位失败
            self.assertEqual(text, "提交成功")
            print("提示：提交成功")
        except:
            print("根据页面列表数据判断是否提交成功")
        sleep(2)
        rx = Role(dr).tree_level1
        tree = []
        print("开始获取左侧一级角色")
        for i in range(len(rx)):
            tree.append(rx[i].get_attribute('textContent'))
        arr = np.array(tree)
        self.assertTrue((arr == self.rolename).any())
        print("左侧菜单新增角色成功")
        tx = variable.get_table(dr)
        table = []
        print("开始获取列表中一级角色")
        for i in range(len(tx)):
            table.append(tx[i][0])
        i = table.index(self.rolename)  #查询指定角色的下标
        self.assertEqual(tx[i][1],self.remarks) #根据下标找到指定角色的备注后进行比较
        # arr = np.array(table)
        # self.assertTrue((arr == self.rolename).any())
        print("列表中新增角色成功,备注内容正确")

    @BeautifulReport.add_test_img("test_3_editrole")
    def test_3_editrole(self):
        """开始执行第二条用例：编辑一级角色"""
        dr = self.dr
        self.dr.switch_to.frame(Role(self.dr).iframe_sw[1])
        sleep(1)
        Role(dr).operation(depName=self.rolename,ope='编辑').click()
        sleep(1)
        self.dr.switch_to.frame('layui-layer-iframe2')
        sleep(1)
        print("修改角色名称为："+self.rolename2)
        Role(self.dr).input_rolename.clear()
        sleep(1)
        Role(self.dr).input_rolename.send_keys(self.rolename2)
        print("修改排序为:"+self.sort4)
        Role(dr).input_sort.clear()
        sleep(1)
        Role(dr).input_sort.send_keys(self.sort4)
        sleep(1)
        print("修改上级角色为admin")
        Role(self.dr).list_parentrole.click()
        sleep(1)
        self.dr.switch_to.frame('layui-layer-iframe1')
        sleep(1)
        Role(dr).tree_admin.click()
        sleep(1)
        self.dr.switch_to.parent_frame()  # 确定按钮和弹框不在一个iframe里，需要跳到上级ifranme中
        sleep(1)
        self.dr.switch_to.parent_frame()
        sleep(1)
        Role(self.dr).submit.click()
        sleep(5)
        print("点击查看")
        Role(dr).tree_admin.click()
        sleep(1)
        Role(dr).operation(depName=self.rolename2, ope='编辑').click()
        sleep(1)
        self.dr.switch_to.frame(Role(dr).iframe_auto)
        sleep(1)
        self.assertEqual(Role(dr).input_rolename.get_attribute("value"), self.rolename2)
        self.assertEqual(Role(dr).list_parentrole.get_attribute("value"), "admin")
        self.assertEqual(Role(dr).input_sort.get_attribute("value"), self.sort4)
        print("页面数据正确")

    @BeautifulReport.add_test_img("test_4_reUser")
    def test_4_reUser(self):
        """角色关联用户"""
        dr = self.dr
        self.dr.switch_to.frame(Role(self.dr).iframe_sw[1])
        sleep(1)
        print("进入角色"+self.rolename3+"的配置用户页面")
        Role(dr).operation(depName=self.rolename3, ope='配置用户').click()
        sleep(1)
        self.dr.switch_to.frame(dr.find_element_by_xpath("//iframe[contains(@src,'/udp/role/selectUserForRole?')]"))
        sleep(1)
        print("点击添加用户")
        Role(dr).role_add_user_btn.click()
        sleep(2)
        Role(dr).input_user.send_keys(self.user1)
        sleep(5)
        ch = Role(dr).choose_list
        self.assertEqual(ch.get_attribute("textContent"),self.user1)
        ch.click()
        print("选择用户"+self.user1)
        sleep(1)
        Role(dr).add_user_submit.click()
        sleep(1)
        print("点击确定添加用户")
        dr.switch_to.parent_frame()
        sleep(1)
        Role(dr).submit.click()
        sleep(1)
        dr.refresh()
        sleep(1)
        User(dr).sys_manger_btn.click()
        sleep(1)
        print("进入用户管理页面，查看用户"+self.user1+"的绑定关系")
        User(dr).user_btn.click()
        sleep(1)
        self.assertEqual(User(dr).curr_lable.text, '用户管理', msg="打开的不是用户管理标签页")
        dr.switch_to.frame(User(dr).iframe_sw[1])
        sleep(2)
        element=User(dr).operation(username=self.user1, ope="查看")
        sleep(1)
        dr.execute_script("arguments[0].click();", element)
        sleep(1)
        print("打开用户"+self.user1+"的查看页面")
        dr.switch_to.frame('layui-layer-iframe1')
        sleep(1)
        self.assertEqual(User(dr).view_roleNames.get_attribute("value").strip(","),self.rolename3)
        print("用户绑定正确，当前绑定角色"+self.rolename3)

    @BeautifulReport.add_test_img("test_5_reMou")
    def test_5_reMou(self):
        """角色关联模块"""
        print("继承上一个用例角色"+self.rolename3+"已经关联用户"+self.user1)
        dr = self.dr
        dr.switch_to.frame(Role(self.dr).iframe_sw[1])
        sleep(1)
        print("进入角色"+self.rolename3+"的配置模块页面")
        Role(dr).operation(depName=self.rolename3, ope='配置模块').click()
        sleep(1)
        dr.switch_to.frame(dr.find_element_by_xpath("//iframe[contains(@src,'/udp/role/selectModuleForRole?')]"))
        print("选择部门管理模块")
        element = Role(dr).Module_checkBox(module="部门管理")
        element.click()
        sleep(3)
        self.assertIn(Role(dr).Module_checkBox(module="部门管理").get_attribute("class"),"button chk checkbox_true_full_focus")
        Role(dr).add_Mod_submit.click()
        sleep(1)
        print("使用"+self.user1+"账号登陆平台")
        dr1 = webdriver.Chrome()
        dr1.get(self.url)
        dr1.maximize_window()  # 将浏览器最大化
        sleep(1)
        variable.login(dr1, self.user1, self.password, self.checkKey)
        for i in range(10):
            if dr1.current_url == self.homeUrl:
                print("登陆成功")
                break
            else:
                print("登陆等待中...")
                sleep(2)

        try:
            elenium = variable.check_modules(dr1, parent="系统管理", child="部门管理")
            self.assertNotEqual(elenium, False)
            print(self.user1+"账号下含有部门管理模块")
            print("admin账号删除账号" + self.user1 + "下的部门管理")
            Role(dr).Module_checkBox(module="部门管理").click()
            sleep(1)
            self.assertIn(Role(dr).Module_checkBox(module="部门管理").get_attribute("class"),
                          "button chk checkbox_false_full_focus")
            Role(dr).add_Mod_submit.click()
            sleep(1)
            dr1.refresh()
            sleep(1)
            print("检查"+self.user1+"用户下是否含有部门管理模块")
            elenium = variable.check_modules(dr1, parent="系统管理")
            self.assertEqual(elenium, False)
            print("账号" + self.user1 + "下没有系统管理菜单")
            dr1.quit()
        except:
            dr1.quit()
            raise ("角色权限验证失败")

    @BeautifulReport.add_test_img("test_6_del_role")
    def test_6_del_role(self):
        """删除角色"""
        dr = self.dr
        self.dr.switch_to.frame(Role(self.dr).iframe_sw[1])
        sleep(1)
        Role(dr).operation(depName=self.rolename3, ope='删除').click()
        sleep(1)
        print("点击角色"+self.user1+"的删除按钮，确定删除")
        Role(dr).submit.click()
        sleep(1)
        tx = variable.get_table(dr)
        for i in range(len(tx)):
            if self.rolename3 in tx[i]:
                print("该角色下存在用户，无法删除，先删除用户")
                Role(dr).operation(depName=self.rolename3, ope='配置用户').click()
                sleep(1)
                dr.switch_to.frame(dr.find_element_by_xpath("//iframe[contains(@src,'/udp/role/selectUserForRole?')]"))
                sleep(3)
                element = Role(dr).del_user
                dr.execute_script("arguments[0].click();", element)
                dr.switch_to.parent_frame()
                sleep(1)
                Role(dr).submit.click()
                sleep(1)
                print("删除角色下的用户成功")
                print("重新删除角色")
                Role(dr).operation(depName=self.rolename3, ope='删除').click()
                sleep(1)
                print("点击角色" + self.user1 + "的删除按钮，确定删除")
                Role(dr).submit.click()
                sleep(1)
                break
            elif i == len(tx)-1:
                raise ("删除角色失败")
        print("检查页面角色列表")

        tx = variable.get_table(dr)
        for i in range(len(tx)):
            if self.rolename3 in tx[i]:
                raise ("删除角色失败")
        print("删除角色成功，列表数据正确")

    @BeautifulReport.add_test_img("test_7_batdelrole")
    def test_7_batdelrole(self):
        """批量删除"""
        dr = self.dr
        print("添加两条角色数据"+self.rolename4+","+self.rolename5)
        test_dataForRole.insert_data2()
        sleep(1)
        print("刷新页面数据")
        self.dr.switch_to.frame(Role(self.dr).iframe_sw[1])
        sleep(1)
        Role(dr).btn_search.click()
        sleep(1)
        tx = variable.get_table(dr)
        for i in range(len(tx)):
            if tx[i][0] == self.rolename4:
                print("当前批量删除用户在列表行数：", str(i+1))
                sleep(1)
                User(dr).checkbox_del(i=str(i+1)).click()
                print("选择要删除用户前的复选框按钮")
            elif tx[i][0] == self.rolename5:
                print("当前批量删除用户在列表行数：", str(i+1))
                sleep(1)
                User(dr).checkbox_del(i=str(i+1)).click()
                print("选择要删除用户前的复选框按钮")
            else:
                print("未找到对应要删除的数据")
        sleep(2)
        Role(dr).btn_batdel.click()
        sleep(1)
        ts = User(dr).toast_info.get_attribute('textContent')
        self.assertEqual(ts, "确定删除吗？")
        print("提示：" + ts)
        Role(dr).submit.click()
        print("点击确定")
        sleep(1)
        tx = variable.get_table(dr)
        for j in range(len(tx)):
            self.assertNotEqual(tx[j][0], self.rolename4)
            self.assertNotEqual(tx[j][0], self.rolename5)
        sleep(1)
        print("验证列表中数据被成功删除")

    @BeautifulReport.add_test_img("test_8_searchrole")
    def test_8_searchrole(self):
        """查询功能验证"""
        dr = self.dr
        self.dr.switch_to.frame(Role(self.dr).iframe_sw[1])
        tb = variable.get_table(dr)
        self.assertNotEqual(len(tb),1) #角色列表执行完前面的用例后应该不止一个，如果只有一个此用例执行无意义
        print("搜索admin角色")
        print("查询输入框输入admin")
        Role(dr).text_search.send_keys("admin")
        sleep(1)
        print("点击搜索按钮")
        Role(dr).btn_search.click()
        sleep(1)
        tb = variable.get_table(dr)
        self.assertEqual(tb[0][0],"admin")
        self.assertEqual(len(tb),1)
        print("查询结果正确，列表只显示admin角色")
        print("点击重置按钮")
        text1 = Role(dr).text_search.get_attribute('value')
        sleep(1)
        Role(dr).btn_reset.click()
        sleep(1)
        text2 = Role(dr).text_search.get_attribute('value')
        self.assertNotEqual(text1,text2)
        self.assertEqual(text2,'')


if __name__ == '__main__':
    testsuite = unittest.TestSuite()

    runner = unittest.TextTestRunner()
    runner.run(testsuite)
























































