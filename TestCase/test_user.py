#coding = utf -8
import unittest,variable,time
from selenium import webdriver
from configparser import ConfigParser
from db_fixture import test_data
from variable import login
from time import sleep
from PO.user import User
import warnings,os
from selenium.webdriver.common.action_chains import *
from BeautifulReport import BeautifulReport


class UserTestCase(unittest.TestCase):
    #全局前置，最新运行，运行一次
    @classmethod
    def setUpClass(cls):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        conf = ConfigParser()
        conf.read(os.path.join(BASE_DIR,'cfginfo.ini'),encoding = 'utf-8')
        conf.sections()
        cls.url = conf.get('URL','url')
        cls.homeUrl = conf.get('URL','homeurl')
        username = conf.get('LOGIN','username')
        cls.password = conf.get('LOGIN','password')
        cls.checkKey = conf.get('LOGIN', 'checkKey')
        cls.username = conf.get('USER', 'username')
        cls.deptname = conf.get('USER', "deptname")
        cls.userId = conf.get('USER','userId')
        cls.mobile = conf.get('USER','mobile')
        cls.email = conf.get('USER','email')
        cls.sort = conf.get('USER', 'sort')
        cls.relate_deptname = conf.get('USER',"relate_deptname")
        cls.relate_role = conf.get('USER','relate_role')
        cls.username_new = conf.get('USER', "username_new")
        cls.deptname_new = conf.get('USER', "deptname_new")
        cls.mobile_new = conf.get('USER', 'mobile_new')
        cls.email_new = conf.get('USER', 'email_new')
        cls.sort_new = conf.get('USER', 'sort_new')
        cls.userId_new = conf.get('USER','userId_new')
        cls.relate_deptname_new = conf.get('USER',"relate_deptname_new")
        cls.relate_role_new = conf.get('USER','relate_role_new')
        cls.user1 = conf.get('USER','user1')
        cls.user2 = conf.get('USER','user2')
        cls.sort98 = conf.get('USER','sort98')
        cls.sort99 = conf.get('USER','sort99')
        cls.username_e = conf.get('USER','username_e')
        cls.userId_e = conf.get('USER','userId_e')
        cls.username_s = conf.get('USER','username_s')
        cls.userId_s = conf.get('USER','userId_s')
        cls.username_d = conf.get('USER','username_d')
        cls.userId_d = conf.get('USER', 'userId_d')
        cls.userId1 = conf.get('USER','userId1')
        cls.userId2 = conf.get('USER', 'userId2')

        cls.parentdept1 = conf.get('USER','parentdept1')
        cls.parentdept2 = conf.get('USER', 'parentdept2')
        cls.parentdept3 = conf.get('USER', 'parentdept3')
        # 清空自己创建的历史数据并创建上级部门
        test_data.init_data()
        print("通过数据库新增上级部门1:" + cls.parentdept1 + "，部门2:" + cls.parentdept2 + "，部门3：" + cls.parentdept3)

        print('开始执行用户管理脚本')
        dr =webdriver.Chrome()  #打开Chrome浏览器
        cls.dr = dr
        print('登录统一开发平台')
        dr.get(cls.url)    #打开统一平台地址
        dr.maximize_window()    #将浏览器最大化
        login(dr,username,cls.password,cls.checkKey)    #输入用户名、密码、验证码后登陆
        for i in range(10):
            if dr.current_url == cls.homeUrl:
                break
            else:
                print('登录等待中...')
                sleep(2)

    # 全局后置，最后运行，只运行一次
    @classmethod
    def tearDownClass(cls):
        print("结束执行用户管理脚本")
        cls.dr.quit()  # 关闭chrome浏览器
        test_data.delete_data()

    def setUp(self):
        print(time.strftime("%Y_%m_%d_%H_%M_%S"))
        dr =self.dr
        self.assertEqual(dr.current_url,self.homeUrl,msg="登录平台异常")#检查登陆是否成功或页面刷新后是否返回首页
        print('当前处于首页状态')
        sleep(2)
        #点击系统管理按钮
        User(dr).sys_manger_btn.click()
        print("点击左侧菜单’系统管理‘")
        sleep(1)
        #点击用户管理标签页
        User(dr).user_btn.click()
        print("点击左侧菜单’用户管理‘")
        sleep(1)
        #检查是否打开用户管理标签页
        self.assertNotEqual(User(dr).curr_lable,False,msg="未打开用户管理标签页")
        self.assertEqual(User(dr).curr_lable.text,'用户管理',msg="打开的不是用户管理标签页")

    def tearDown(self):
        print("刷新页面，返回首页")
        print(time.strftime("%Y_%m_%d_%H_%M_%S"))
        self.dr.refresh()  # 刷新页面，返回首页
        sleep(1)

    def save_img(self, img_name):
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"./img"), img_name))

    @BeautifulReport.add_test_img("test_1_add_user")
    def test_1_add_user(self):
        '''新增用户'''
        print("--------------------新增用户-----------------------")
        dr = self.dr
        #新增用户
        print("新增用户："+self.username)
        User(dr).add_user_model(parentdept=self.parentdept1,username=self.username,userId=self.userId,mobile=self.mobile,email=self.email,sort=self.sort,relate_deptname=self.relate_deptname,relate_role=self.relate_role)
        sleep(1)
        try:
            text = User(dr).toast_info.get_attribute('textContent')  #info消息偶尔会定位失败
            self.assertEqual(text, "提交成功")
            print("提示：提交成功")
        except:
            print("根据页面列表数据判断是否提交成功")
        dr.switch_to.frame(User(dr).iframe_sw[1])
        sleep(2)
        #点击组织结构中上级部门
        User(dr).tree_name(departName=self.parentdept1).click()
        sleep(1)
        print("获取列表中的字段进行校验")
        table = variable.get_table(dr)
        for i in range(len(table)):
            if (self.username and self.userId )in table[i]:
                print("表格内字段成功验证")
                break
            elif i == len(table) -1:
                raise ("test_1_add_user：新增表格内字段未查询到")
            else:
                continue
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        User(dr).button_refresh.click()
        sleep(1)
        dr.switch_to.frame(User(dr).iframe_sw[1])
        sleep(1)
        #点击查看用户按钮
        element = User(dr).operation(username=self.username, ope="查看")
        sleep(1)
        dr.execute_script("arguments[0].click();", element)
        sleep(1)
        print("点击查看按钮")
        sleep(2)
        self.assertEqual(User(dr).user_title.text,"查看用户",msg="查看用户弹框未正常打开")
        sleep(2)
        dr.switch_to.frame(User(dr).iframe_dep)
        sleep(1)
        #验证查看的内容和添加内容一致
        print("验证添加的用户字段是否正确")
        self.assertEqual(User(dr).view_deptname.get_attribute("value"), self.deptname, msg="查看中字段部门和添加不一致")
        self.assertEqual(User(dr).view_username.get_attribute("value"), self.username, msg="查看中字段姓名和添加不一致")
        self.assertEqual(User(dr).view_userId.get_attribute("value"), self.userId, msg="查看中字段用户名和添加不一致")
        self.assertEqual(User(dr).view_email.get_attribute("value"), self.email, msg="查看中字段邮箱和添加不一致")
        self.assertEqual(User(dr).view_mobile.get_attribute("value"), self.mobile, msg="查看中字段手机号和添加不一致")
        self.relate_deptname =  self.relate_deptname + ","
        self.assertEqual(User(dr).view_deptNames.get_attribute("value"),self.relate_deptname, msg="查看中字段关联部门和添加不一致")
        self.relate_role = self.relate_role + ","
        self.assertEqual(User(dr).view_roleNames.get_attribute("value"), self.relate_role, msg="查看中字段关联角色和添加不一致")
        print('验证验证查看的内容和添加内容一致')
        sleep(2)
        #点击返回按钮
        User(dr).backToList.click()
        print('点击返回按钮')

    @BeautifulReport.add_test_img("test_2_edit_user")
    def test_2_edit_user(self):
        '''编辑用户'''
        print("--------------------编辑用户-----------------------")
        dr = self.dr
        #新增用户
        print("新增用户："+self.username_e)
        User(dr).add_user_model(parentdept=self.parentdept1,username=self.username_e,userId=self.userId_e,mobile=self.mobile,email=self.email,sort=self.sort,relate_deptname=self.relate_deptname,relate_role=self.relate_role)
        sleep(1)
        try:
            text = User(dr).toast_info.get_attribute('textContent')  #info消息偶尔会定位失败
            self.assertEqual(text, "提交成功")
            print("提示：提交成功")
        except:
            print("根据页面列表数据判断是否提交成功")
        dr.switch_to.frame(User(dr).iframe_sw[1])
        #点击组织结构中上级部门
        User(dr).tree_name(departName=self.parentdept1).click()
        sleep(1)
        print("获取列表中的字段进行校验")
        table = variable.get_table(dr)
        for i in range(len(table)):
            if (self.username_e and self.userId_e )in table[i]:
                print("表格内字段成功验证")
                break
            elif i == len(table) -1:
                raise ("test_1_add_user：新增表格内字段未查询到")
            else:
                continue
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        User(dr).button_refresh.click()
        sleep(1)
        #修改用户
        User(dr).edit_user(parentdept=self.parentdept3,username=self.username_e,username_new=self.username_new,mobile_new=self.mobile_new,email_new=self.email_new,sort_new=self.sort_new,relate_deptname_new=self.deptname,relate_role_new=self.relate_role_new)
        sleep(1)
        try:
            text = User(dr).toast_info.get_attribute('textContent')  # info消息偶尔会定位失败
            self.assertEqual(text, "提交成功")
            print("提示：提交成功")
        except:
            print("根据页面列表数据判断是否提交成功")
        dr.switch_to.frame(User(dr).iframe_sw[1])
        # 点击组织结构中上级部门
        User(dr).tree_name(departName=self.parentdept3).click()
        sleep(1)
        table = variable.get_table(dr)
        for i in range(len(table)):
            if self.username_new  in table[i]:
                print("表格内字段成功验证")
                break
            elif i == len(table)-1:
                raise ("test_3_edit_user:编辑表格内字段未查询到")
            else:
                continue

    @BeautifulReport.add_test_img("test_3_search_user")
    def test_3_search_user(self):
        '''搜索'''
        print("--------------------搜索-----------------------")
        dr =self.dr
        # 新增用户
        print("新增用户：" + self.username_s)
        User(dr).add_user_model(parentdept=self.parentdept1, username=self.username_s, userId=self.userId_s,
                                mobile=self.mobile, email=self.email, sort=self.sort)
        sleep(1)
        try:
            text = User(dr).toast_info.get_attribute('textContent')  # info消息偶尔会定位失败
            self.assertEqual(text, "提交成功")
            print("提示：提交成功")
        except:
            print("根据页面列表数据判断是否提交成功")
        dr.switch_to.frame(User(dr).iframe_sw[1])
        sleep(1)
        #输入查询条件
        User(dr).search_name.send_keys(self.username_s)
        print("输入查询姓名字段：",str(self.username_s))
        sleep(1)
        User(dr).disable_user.click()
        sleep(1)
        User(dr).button_disable_user.click()
        sleep(1)
        User(dr).btn_search.click()
        print("点击查询按钮")
        sleep(1)
        tx = variable.get_table(dr)
        self.assertEqual(tx[0][0], self.username_s)
        self.assertEqual(len(tx), 1)
        print("查询结果正确，列表只显示" + self.username_s)

    @BeautifulReport.add_test_img("test_4_reset_user")
    def test_4_reset_user(self):
        '''重置'''
        print("--------------------重置-----------------------")
        dr = self.dr
        # 新增用户
        dr.switch_to.frame(User(dr).iframe_sw[1])
        sleep(1)
        # 输入查询条件
        User(dr).search_name.send_keys(self.username_s)
        print("输入查询姓名字段：", str(self.username_s))
        text_input_username = User(dr).search_name.get_attribute('value')
        self.assertEqual(text_input_username,self.username_s)
        sleep(1)
        User(dr).disable_user.click()
        sleep(1)
        User(dr).reset.click()
        sleep(1)
        text_input = User(dr).search_name.get_attribute('value')
        self.assertEqual(text_input,'',msg="查询的字段未重置成功")

    @BeautifulReport.add_test_img("test_5_del_user")
    def test_5_del_user(self):
        '''删除用户'''
        print("--------------------删除用户-----------------------")
        dr = self.dr
        self.dr.switch_to.frame(User(self.dr).iframe_sw[1])
        sleep(1)
        User(dr).tree_name(departName=self.parentdept1).click()
        sleep(2)
        print("找到" + self.username_s + "用户后，点击删除按钮")
        sleep(1)
        element = User(dr).operation(self.username_s, ope="删除")
        sleep(1)
        dr.execute_script("arguments[0].click();",element)
        sleep(1)
        print("点击确定")
        User(dr).submit.click()
        sleep(1)
        try:
            text = User(dr).toast_info.get_attribute('textContent')  # info消息偶尔会定位失败
            self.assertEqual(text, "删除成功")
            print("提示：删除成功")
        except:
            print("根据页面列表数据判断是否提交成功")
        # 点击组织结构中上级部门
        User(dr).tree_name(departName=self.parentdept1).click()
        sleep(1)
        tx = variable.get_table(dr)
        print("开始检查列表中用户是否被删除")
        for i in range(len(tx)):
            self.assertNotEqual(tx[i][0], self.username_s)
        sleep(1)
        print("列表中的" + self.username_s + "用户已经被删除")

    @BeautifulReport.add_test_img("test_6_sort_user")
    def test_6_sort_user(self):
        '''排序'''
        print("--------------------排序-----------------------")
        dr = self.dr
        # 新增用户1
        User(dr).add_user_model(parentdept=self.parentdept1, username=self.user1, userId=self.userId1, mobile=self.mobile,
                                email=self.email, sort=self.sort98)
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        User(dr).button_refresh.click()
        sleep(1)
        # 新增用户2
        User(dr).add_user_model(parentdept=self.parentdept1, username=self.user2, userId=self.userId2, mobile=self.mobile,
                                email=self.email, sort=self.sort99)
        sleep(2)
        print("页面添加两个用户:" + self.user1 + '、' + self.user2 + "，排序分别为：" + self.sort98 + "、" + self.sort99)
        sleep(1)
        dr.switch_to.frame(User(dr).iframe_sw[1])
        sleep(1)
        tx = variable.get_table(dr)
        index = None
        index1 = None
        for i in range(len(tx)):
            if tx[i][0] == self.user1:
                index = i
            elif tx[i][0] == self.user2:
                index1 = i
            if index != None and index1 != None:
                break
        if index < index1:
            print("初始排序正确，用户" + self.user1 + "排在前面")
        else:
            raise ("排序错误")
        dr.switch_to.parent_frame()
        sleep(1)
        User(dr).button_refresh.click()
        sleep(1)
        dr.switch_to.frame(User(dr).iframe_sw[1])
        sleep(1)
        print("修改" + self.user2 + "的排序")
        sleep(2)
        element = User(dr).operation(username=self.user2, ope="编辑")
        sleep(3)
        dr.execute_script("arguments[0].click();", element)
        sleep(1)
        dr.switch_to.frame(User(dr).iframe_dep)
        sleep(1)
        User(dr).input_sort.clear()
        sleep(1)
        User(dr).input_sort.send_keys(str(int(self.sort99) - 2))
        print("修改用户排序为：" + str(int(self.sort99) - 2))
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        User(dr).submit.click()
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        User(dr).button_refresh.click()
        sleep(1)
        dr.switch_to.frame(User(dr).iframe_sw[1])
        sleep(1)
        tx = variable.get_table(dr)
        index = None
        index1 = None
        for i in range(len(tx)):
            if tx[i][0] == self.user1:
                index = i
            elif tx[i][0] == self.user2:
                index1 = i
            if index != None and index1 != None:
                break
        if index > index1:
            print("初始排序正确，用户" + self.user2 + "排在前面")
        else:
            raise ("排序错误")

    @BeautifulReport.add_test_img("test_7_del_batches_user")
    def test_7_del_batches_user(self):
        '''批量删除用户'''
        print("--------------------批量删除用户-----------------------")
        dr = self.dr
        dr.switch_to.frame(User(dr).iframe_sw[1])
        sleep(1)
        User(dr).tree_name(departName=self.parentdept1).click()
        sleep(1)
        tx = variable.get_table(dr)
        for i in range(len(tx)):
            if tx[i][0] == self.user1:
                print("当前批量删除用户在列表行数：", str(i + 1))
                sleep(1)
                User(dr).checkbox_del(i=str(i + 1)).click()
                sleep(1)
                print("选择要删除用户前的复选框按钮")
                break
            elif i == len(tx)-1:
                raise ("test_8_del_batches:没有找到要删除的用户"+self.user1)
            else:
                continue
        for j in range(len(tx)):
            if tx[j][0] == self.user2:
                print("当前批量删除用户在列表行数：", str(j + 1))
                sleep(1)
                User(dr).checkbox_del(i=str(j + 1)).click()
                print("选择要删除用户前的复选框按钮")
                break
            elif j == len(tx) - 1:
                raise ("test_8_del_batches:没有找到要删除的用户"+self.user2)
            else:
                continue
        sleep(1)
        User(dr).del_all_button.click()
        print("点击批量删除按钮")
        sleep(1)
        ts = User(dr).toast_info.get_attribute('textContent')
        self.assertEqual(ts, "确定删除吗？")
        print("提示：" + ts)
        sleep(1)
        User(dr).submit.click()
        sleep(1)
        print("点击确定")
        sleep(1)
        tx = variable.get_table(dr)
        for j in range(len(tx)):
            self.assertNotEqual(tx[j][0], self.user1)
            self.assertNotEqual(tx[j][0], self.user2)
        sleep(1)
        print("验证列表中数据被成功删除")


class UserTestCaseOpe(unittest.TestCase):
    #全局前置，最新运行，运行一次
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        conf = ConfigParser()
        conf.read(os.path.join(BASE_DIR,'cfginfo.ini'),encoding = 'utf-8')
        conf.sections()
        cls.url = conf.get('URL', 'url')
        cls.homeUrl = conf.get('URL', 'homeurl')
        cls.username_admin = conf.get('LOGIN', 'username')
        cls.password = conf.get('LOGIN', 'password')
        cls.checkKey = conf.get('LOGIN', 'checkKey')
        cls.deptname = conf.get('USER', "deptname")
        cls.username = conf.get('USER', "username")
        cls.relate_deptname = conf.get('USER',"relate_deptname")
        cls.relate_role = conf.get('USER','relate_role')
        cls.userId = conf.get('USER', 'userId')
        cls.mobile = conf.get('USER', 'mobile')
        cls.email = conf.get('USER', 'email')
        cls.sort = conf.get('USER', 'sort')
        cls.new_password = conf.get('USER','new_password')
        cls.username_ope = conf.get('USER','username_ope')
        cls.userId_ope = conf.get('USER','userId_ope')

        cls.parentdept1 = conf.get('USER','parentdept1')
        cls.parentdept2 = conf.get('USER', 'parentdept2')
        cls.parentdept3 = conf.get('USER', 'parentdept3')

        # 清空自己创建的历史数据并创建上级部门
        sleep(5)
        test_data.insert_data1()
        print("通过数据库新增上级部门1:" + cls.parentdept1 + "，部门2:" + cls.parentdept2 + "，部门3：" + cls.parentdept3)


    # 全局后置，最后运行，只运行一次
    @classmethod
    def tearDownClass(cls):
        print("清空数据库添加的前置数据")
        test_data.delete_data()
    def save_img(self, img_name):
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"./img"), img_name))
    def setUp(self):
        print(time.strftime("%Y_%m_%d_%H_%M_%S"))
        dr = webdriver.Chrome()  # 打开Chrome浏览器
        self.dr =dr
        print('登录统一开发平台')
        dr.get(self.url)  # 打开统一平台地址
        dr.maximize_window()  # 将浏览器最大化
        login(dr, self.username_admin, self.password,self.checkKey)  # 输入用户名、密码、验证码后登陆
        for i in range(10):
            if dr.current_url == self.homeUrl:
                break
            else:
                print('登录等待中...')
                sleep(2)
        self.assertEqual(dr.current_url,self.homeUrl,msg="登录平台异常")#检查登陆是否成功或页面刷新后是否返回首页
        print('当前处于首页状态')
        sleep(2)
        #点击系统管理按钮
        User(dr).sys_manger_btn.click()
        print("点击左侧菜单’系统管理‘")
        sleep(1)
        #点击用户管理标签页
        User(dr).user_btn.click()
        print("点击左侧菜单’用户管理‘")
        sleep(1)
        #检查是否打开用户管理标签页
        self.assertNotEqual(User(dr).curr_lable,False,msg="未打开用户管理标签页")
        self.assertEqual(User(dr).curr_lable.text,'用户管理',msg="打开的不是用户管理标签页")

    def tearDown(self):
        print(time.strftime("%Y_%m_%d_%H_%M_%S"))
        print("关闭浏览器")
        self.dr.quit()  # 关闭chrome浏览器
        sleep(1)

    @BeautifulReport.add_test_img("test_1_modify_password")
    def test_1_modify_password(self):
        '''创建用户修改密码'''
        print("--------------------创建用户修改密码-----------------------")
        dr =self.dr
        sleep(2)
        #新增用户
        print("创建用户修改密码")
        User(dr).add_user_model(parentdept=self.parentdept1,username=self.username_ope,userId=self.userId_ope,mobile=self.mobile,email=self.email,sort=self.sort)
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        ActionChains(dr).move_to_element(User(dr).name).perform()
        sleep(5)
        #点击退出按钮
        User(dr).logout.click()
        print("退出系统管理员账号")
        sleep(1)
        #新增的用户登录修改密码
        print("普通用户登录修改密码")
        login(dr,self.userId_ope,self.password,self.checkKey)  # 输入用户名、密码、验证码后登陆
        sleep(2)
        #修改密码
        User(dr).oldPassword.send_keys(self.password)
        sleep(2)
        User(dr).newPassword.send_keys(self.new_password)
        sleep(2)
        User(dr).confirmPassword.send_keys(self.new_password)
        sleep(2)
        User(dr).login_submit.click()
        sleep(1)
        try:
            text = User(dr).toast_info.get_attribute('textContent')  #info消息偶尔会定位失败
            self.assertEqual(text, "密码修改成功")
        except:
            raise ("密码修改失败")

    @BeautifulReport.add_test_img("test_2_init_password")
    def test_2_init_password(self):
        '''初始化用户'''
        print("--------------------初始化用户-----------------------")
        dr =self.dr
        dr.switch_to.frame(User(dr).iframe_sw[1])
        sleep(2)
        # 点击查看用户按钮
        print("点击查看用户:"+self.username_ope)
        element = User(dr).operation(username=self.username_ope, ope="查看")
        sleep(1)
        dr.execute_script("arguments[0].click();", element)
        sleep(1)
        print("点击查看按钮")
        sleep(2)
        dr.switch_to.frame(User(dr).iframe_dep)
        sleep(1)
        User(dr).view_init_password.click()
        print("点击初始化密码按钮")
        sleep(1)
        ts = User(dr).toast_info.get_attribute('textContent')
        self.assertEqual(ts, "初始化密码成功",msg="初始化密码失败")
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(2)
        ActionChains(dr).move_to_element(User(dr).name).perform()
        sleep(5)
        # 点击退出按钮
        User(dr).logout.click()
        sleep(1)
        print("退出系统管理员账号")
        # 新增的用户登录修改密码
        login(dr,self.userId_ope,self.password,self.checkKey)  # 输入用户名、密码、验证码后登陆
        #验证登录之后修改密码页
        sleep(2)
        self.assertEqual(User(dr).login_submit.text,"提交",msg="测试用户"+self.userId_ope+"未成功登录")

    @BeautifulReport.add_test_img("test_3_disable_user")
    def test_3_disable_user(self):
        '''禁用用户'''
        print("--------------------禁用用户-----------------------")
        dr = self.dr
        sleep(1)
        dr.switch_to.frame(User(dr).iframe_sw[1])
        sleep(2)
        # 点击查看用户按钮
        element = User(dr).operation(username=self.username_ope, ope="查看")
        sleep(1)
        dr.execute_script("arguments[0].click();", element)
        sleep(1)
        print("点击查看按钮")
        sleep(2)
        dr.switch_to.frame(User(dr).iframe_dep)
        sleep(1)
        User(dr).view_disable_user.click()
        print("点击禁用按钮")
        sleep(1)
        ts = User(dr).toast_info.get_attribute('textContent')
        sleep(1)
        self.assertEqual(ts, "禁用成功")
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(2)
        ActionChains(dr).move_to_element(User(dr).name).perform()
        sleep(5)
        # 点击退出按钮
        User(dr).logout.click()
        sleep(1)
        login(dr, self.userId_ope, self.password, self.checkKey)  # 输入用户名、密码、验证码后登陆
        sleep(2)
        self.assertEqual(User(dr).login_msg.text,"用户被禁用")

    @BeautifulReport.add_test_img("test_4_activate_user")
    def test_4_activate_user(self):
        '''激活用户'''
        print("--------------------激活用户-----------------------")
        dr = self.dr
        sleep(1)
        dr.switch_to.frame(User(dr).iframe_sw[1])
        sleep(1)
        # 搜索禁用用户
        User(dr).disable_user.click()
        sleep(1)
        User(dr).button_able_user.click()
        sleep(1)
        User(dr).btn_search.click()
        print("点击查询按钮")
        sleep(2)
        # 点击查看用户按钮
        element = User(dr).operation(username=self.username_ope, ope="查看")
        sleep(1)
        dr.execute_script("arguments[0].click();", element)
        sleep(2)
        print("点击查看按钮")
        sleep(2)
        dr.switch_to.frame(User(dr).iframe_dep)
        sleep(1)
        User(dr).view_able_user.click()
        print("点击激活按钮")
        sleep(1)
        ts = User(dr).toast_info.get_attribute('textContent')
        self.assertEqual(ts, "激活成功")
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(2)
        ActionChains(dr).move_to_element(User(dr).name).perform()
        sleep(5)
        # 点击退出按钮
        User(dr).logout.click()
        sleep(1)
        login(dr,self.userId_ope,self.password,self.checkKey)  # 输入用户名、密码、验证码后登陆
        sleep(2)
        # 验证登录之后修改密码页
        self.assertEqual(User(dr).login_submit.text, "提交", msg="测试用户" + self.userId_ope + "未成功登录")

    @BeautifulReport.add_test_img("test_5_clearUserLock")
    def test_5_clearUserLock(self):
        '''解除锁定'''
        print("--------------------解除锁定-----------------------")
        dr = self.dr
        sleep(2)
        ActionChains(dr).move_to_element(User(dr).name).perform()
        sleep(5)
        # 点击退出按钮
        User(dr).logout.click()
        sleep(1)
        # 新增的用户登录锁定账号
        login(dr, self.userId_ope, self.new_password, self.checkKey)  # 输入用户名、密码、验证码后登陆
        sleep(1)
        self.assertEqual(User(dr).login_msg.get_attribute('textContent'), "用户名或密码错误")
        sleep(1)
        User(dr).msg_close.click()
        sleep(1)
        User(dr).button_login_submit.click()
        sleep(1)
        self.assertEqual(User(dr).login_msg.get_attribute('textContent'), "用户名或密码错误")
        sleep(1)
        User(dr).msg_close.click()
        sleep(1)
        User(dr).button_login_submit.click()
        sleep(1)
        self.assertEqual(User(dr).login_msg.get_attribute('textContent'), "用户名或密码错误")
        sleep(1)
        User(dr).msg_close.click()
        sleep(1)
        User(dr).button_login_submit.click()
        sleep(1)
        self.assertEqual(User(dr).login_msg.text,"对不起，因为您输入的密码已经多次错误，该账号将被锁定10分钟。")
        print("用户登录账号或密码错误3次，提示账号锁定")
        User(dr).msg_close.click()
        sleep(1)
        print("点击提示信息关闭按钮")
        login(dr,self.username_admin, self.password, self.checkKey)
        sleep(1)
        # 点击系统管理按钮
        User(dr).sys_manger_btn.click()
        print("点击左侧菜单’系统管理‘")
        sleep(1)
        # 点击用户管理标签页
        User(dr).user_btn.click()
        print("点击左侧菜单’用户管理‘")
        sleep(1)
        dr.switch_to.frame(User(dr).iframe_sw[1])
        sleep(2)
        # 点击查看用户按钮
        element = User(dr).operation(username=self.username_ope, ope="查看")
        sleep(1)
        dr.execute_script("arguments[0].click();", element)
        print("点击查看按钮")
        sleep(2)
        dr.switch_to.frame(User(dr).iframe_dep)
        sleep(1)
        User(dr).view_clearUserLock.click()
        print("点击解除锁定按钮")
        sleep(1)
        ts = User(dr).toast_info.get_attribute('textContent')
        self.assertEqual(ts, "解除锁定成功")
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(2)
        ActionChains(dr).move_to_element(User(dr).name).perform()
        sleep(5)
        # 点击退出按钮
        User(dr).logout.click()
        sleep(1)
        login(dr, self.userId_ope, self.password, self.checkKey)  # 输入用户名、密码、验证码后登陆
        sleep(2)
        # 验证登录之后修改密码页
        self.assertEqual(User(dr).login_submit.text, "提交", msg="测试用户" + self.userId_ope + "未成功登录")


if __name__=='__main__':
    unittest.main()







