#coding = utf -8
import unittest,variable,time
from selenium import webdriver
from configparser import ConfigParser
from db_fixture import test_dataForModule
from variable import login
from time import sleep
from PO.module import Module
from PO.user import User
import unittest, random, os, traceback
from BeautifulReport import BeautifulReport

SCREENSHOT_DIR = './test_result'

class MoudleTestCase(unittest.TestCase):
    #全局前置，最新运行，运行一次
    @classmethod
    def setUpClass(cls):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        conf = ConfigParser()
        conf.read(os.path.join(BASE_DIR, 'cfginfo.ini'), encoding='utf-8')
        conf.sections()
        cls.url = conf.get('URL','url')
        cls.homeUrl = conf.get('URL','homeurl')
        username = conf.get('LOGIN','username')
        cls.password = conf.get('LOGIN','password')
        cls.checkKey = conf.get('LOGIN', 'checkKey')
        cls.modulename = conf.get('MODULE','modulename')
        cls.moduleurl = conf.get('MODULE','moduleurl')
        cls.modulesort = conf.get('MODULE','modulesort')
        cls.parentname = conf.get('MODULE', 'parentname')
        cls.isvisible_add = conf.get('MODULE','isvisible_add')
        cls.ispublic_add = conf.get('MODULE','ispublic_add')
        cls.target = conf.get('MODULE','target')
        cls.alert_url = conf.get('MODULE','alert_url')
        cls.modulename_new = conf.get('MODULE', 'modulename_new')
        cls.moduleurl_new = conf.get('MODULE', 'moduleurl_new')
        cls.modulesort_new = conf.get('MODULE', 'modulesort_new')
        cls.parentname_new = conf.get('MODULE','parentname_new')
        cls.module1 = conf.get('MODULE','module1')
        cls.module2 = conf.get('MODULE', 'module2')
        cls.sort98 = conf.get('MODULE','sort98')
        cls.sort99 = conf.get('MODULE','sort99')
        cls.modulename_public = conf.get('MODULE','modulename_public')
        cls.userid = conf.get("MODULE",'userid')
        cls.modulename_visible=conf.get('MODULE','modulename_visible')
        print('开始执行模块管理脚本')

        cls.parentmodule1 = conf.get('MODULE', 'parentmodule1')
        cls.parentmodule2 = conf.get('MODULE', 'parentmodule2')
        cls.dept = conf.get('MODULE','dept')
        cls.user = conf.get('MODULE', 'user')
        # 清空自己创建的历史数据并创建上级模块
        test_dataForModule.init_data()
        print("通过数据库新增上级模块1:" + cls.parentmodule1 + "，模块2:" + cls.parentmodule2 + "，模块3：" + cls.modulename_public+"，模块4：" + cls.modulename_visible+"，部门：" + cls.dept+"，用户：" + cls.user)

        dr =webdriver.Chrome()  #打开Chrome浏览器
        cls.dr = dr
        print('登录统一开发平台')
        dr.get(cls.url)    #打开统一平台地址
        dr.maximize_window()  #将浏览器最大化
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
        print("结束执行模块管理脚本")
        test_dataForModule.delete_data()
        cls.dr.quit()  # 关闭chrome浏览器


    def setUp(self):
        print(time.strftime("%Y_%m_%d_%H_%M_%S"))
        dr =self.dr
        self.assertEqual(dr.current_url,self.homeUrl,msg="登录平台异常")#检查登陆是否成功或页面刷新后是否返回首页
        print('当前处于首页状态')
        sleep(2)
        #点击系统管理按钮
        Module(dr).sys_manger_btn.click()
        print("点击左侧菜单’系统管理‘")
        sleep(1)
        #点击用户管理标签页
        Module(dr).module_btn.click()
        print("点击左侧菜单’模块管理‘")
        sleep(1)
        self.assertNotEqual(Module(dr).curr_lable,False,msg="未打开模块管理标签页")
        self.assertEqual(Module(dr).curr_lable.get_attribute('textContent'),'模块管理',msg="打开的不是模块管理标签页")


    def tearDown(self):
        print("刷新页面，返回首页")
        print(time.strftime("%Y_%m_%d_%H_%M_%S"))
        self.dr.refresh()  # 刷新页面，返回首页
        sleep(1)

    def save_img(self, img_name):
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"./img"), img_name))

    @BeautifulReport.add_test_img("test_1_add_module")
    def test_1_add_module(self):
        '''新增模块'''
        print("--------------------新增模块-----------------------")
        dr = self.dr
        #添加模块
        Module(dr).add_module(parentmodule=self.parentname,modulename=self.modulename,module_url=self.moduleurl, modulesort=self.modulesort,isvisible=self.isvisible_add,ispublic=self.ispublic_add,target=self.target,alert_url=self.alert_url)
        sleep(1)
        try:
            text = Module(dr).toast_info.get_attribute('textContent')  # info消息偶尔会定位失败
            self.assertEqual(text, "提交成功")
            print("提示：提交成功")
        except:
            print("根据页面列表数据判断是否提交成功")
        sleep(5)
        Module(dr).tree_custom(self.parentname).click()
        sleep(1)
        table = variable.get_table(dr)
        for i in range(len(table)):
            if self.modulename in table[i]:
                print("表格内字段成功验证")
                break
            elif i == len(table) -1:
                print(table)
                raise ("test_1_add_module：新增表格内字段未查询到")
            else:
                continue

    @BeautifulReport.add_test_img("test_2_view_module")
    def test_2_view_module(self):
        '''查看模块'''
        print("--------------------查看模块-----------------------")
        dr =self.dr
        dr.switch_to.frame(Module(dr).iframe_sw[1])
        sleep(1)
        #点击测试模块资源树
        Module(dr).tree_name(self.parentname).click()
        sleep(1)
        tx = variable.get_table(dr)
        print("获取表格中的modulename字段进行验证")
        for i in range(len(tx)):
            if self.modulename in tx[i]:
                print("表格中新增模块字段信息：",str(tx[i]))
                self.assertEqual(self.modulename, tx[i][0])
                self.assertEqual(self.moduleurl, tx[i][2])
                break
            elif i ==len(tx)-1:
                raise("未查询到新增模块")
            else:
                continue

    @BeautifulReport.add_test_img("test_3_edit_module")
    def test_3_edit_module(self):
        '''编辑模块'''
        print("--------------------编辑模块-----------------------")
        dr = self.dr
        dr.switch_to.frame(Module(dr).iframe_sw[1])
        sleep(1)
        # 点击测试模块资源树
        Module(dr).tree_custom(self.parentname).click()
        sleep(2)
         #点击编辑按钮
        element = Module(dr).operation(self.modulename,'编辑')
        dr.execute_script("arguments[0].click();", element)
        sleep(1)
        Module(dr).edit_module(parentmodule=self.parentname_new,modulename=self.modulename_new,modulesort=self.modulesort_new,module_url=self.moduleurl_new,isvisible=self.isvisible_add,ispublic=self.ispublic_add,target=self.target,alert_url=self.alert_url)

        try:
            text = Module(dr).toast_info.get_attribute('textContent')  # info消息偶尔会定位失败
            self.assertEqual(text, "提交成功")
            print("提示：提交成功")
        except:
            print("根据页面列表数据判断是否提交成功")
        sleep(5)
        Module(dr).tree_custom(self.parentname_new).click()
        sleep(1)
        table = variable.get_table(dr)
        for i in range(len(table)):
            if self.modulename_new in table[i]:
                print("表格内字段成功验证")
                break
            elif i == len(table) -1:
                raise ("test_3_edit_module：编辑表格内字段未查询到")
            else:
                continue

    @BeautifulReport.add_test_img("test_4_search_module")
    def test_4_search_module(self):
        '''搜索'''
        print("-------------------搜索-----------------------")
        dr =self.dr
        dr.switch_to.frame(Module(dr).iframe_sw[1])
        sleep(1)
        #输入查询条件
        Module(dr).search_name.send_keys(self.parentmodule2)
        print("输入查询姓名字段：",str(self.parentmodule2))
        sleep(1)
        Module(dr).btn_search.click()
        print("点击查询按钮")
        sleep(1)
        tx = variable.get_table(dr)
        self.assertEqual(tx[0][0], self.parentmodule2)
        self.assertEqual(len(tx), 1)
        print("查询结果正确，列表只显示"+self.parentmodule2)

    @BeautifulReport.add_test_img("test_5_resetM")
    def test_5_resetM(self):
        '''重置'''
        print("--------------------重置-----------------------")
        dr = self.dr
        dr.switch_to.frame(Module(dr).iframe_sw[1])
        sleep(1)
        # 输入查询条件
        Module(dr).search_name.send_keys(self.modulename_new)
        print("输入查询姓名字段：", str(self.modulename_new))
        text_input_modulename = Module(dr).search_name.get_attribute('value')
        sleep(1)
        print("页面校验字段"+self.modulename_new +"存在")
        self.assertEqual(text_input_modulename,self.modulename_new)
        sleep(1)
        print("点击重置按钮")
        Module(dr).reset.click()
        sleep(1)
        text_input = Module(dr).search_name.get_attribute('value')
        sleep(1)
        print("页面校验字段" + self.modulename_new + "重置成功")
        self.assertEqual(text_input,'',msg="查询的字段未重置成功")

    @BeautifulReport.add_test_img("test_6_del_parent_module")
    def test_6_del_parent_module(self):
        '''删除父模块'''
        print("--------------------删除父模块-----------------------")
        dr = self.dr
        self.dr.switch_to.frame(Module(self.dr).iframe_sw[1])
        sleep(2)
        print("找到" + self.parentname_new + "模块后，点击删除按钮")
        sleep(1)
        element = Module(dr).operation(self.parentname_new, ope="删除")
        dr.execute_script("arguments[0].click();",element)
        sleep(1)
        try:
            text = User(dr).toast_info.get_attribute('textContent')  # info消息偶尔会定位失败
            self.assertEqual(text, "存在子模块无法删除")
            print("提示：存在子模块无法删除")
        except:
            print("根据页面列表数据判断是否提交成功")
        print("开始检查列表中模块是否被删除")
        tx = variable.get_table(dr)
        for i in range(len(tx)):
            if self.parentname in tx[i]:
                print ("列表中的" + self.parentname + "模块未被删除")
                break
            elif i == len(tx)-1:
                raise ("绑定子模块的父模块被成功删除")
            else:
                continue

    @BeautifulReport.add_test_img("test_7_del_module")
    def test_7_del_module(self):
        '''删除模块'''
        print("--------------------删除模块-----------------------")
        dr = self.dr
        self.dr.switch_to.frame(Module(self.dr).iframe_sw[1])
        #点击测试模块资源树
        Module(dr).tree_custom(self.parentname_new).click()
        sleep(1)
        print("找到" + self.modulename_new + "模块后，点击删除按钮")
        sleep(1)
        element = Module(dr).operation(self.modulename_new, ope="删除")
        dr.execute_script("arguments[0].click();",element)
        sleep(1)
        print("点击确定")
        Module(dr).submit.click()
        sleep(1)
        try:
            text = User(dr).toast_info.get_attribute('textContent')  # info消息偶尔会定位失败
            self.assertEqual(text, "删除成功")
            print("提示：删除成功")
        except:
            print("根据页面列表数据判断是否提交成功")
        tx = variable.get_table(dr)
        print("开始检查列表中模块是否被删除")
        for i in range(len(tx)):
            self.assertNotEqual(tx[i][0], self.modulename_new)
        sleep(1)
        print("列表中的" + self.modulename_new + "模块已经被删除")

    @BeautifulReport.add_test_img("test_8_sort_module")
    def test_8_sort_module(self):
        '''排序'''
        print("--------------------排序-----------------------")
        dr = self.dr
        # 新增模块1
        Module(dr).add_module(parentmodule=self.parentname, modulename=self.module1, modulesort = self.sort98, isvisible = self.isvisible_add, ispublic = self.ispublic_add, target = self.target, alert_url = self.alert_url)
        sleep(3)
        dr.switch_to.parent_frame()
        sleep(1)
        Module(dr).button_refresh.click()
        sleep(1)
        dr.switch_to.frame(Module(dr).iframe_sw[1])
        sleep(1)
        # 点击测试模块资源树
        Module(dr).tree_name(self.parentname).click()
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        # 新增模块2
        Module(dr).add_module(parentmodule=self.parentname, modulename=self.module2, modulesort = self.sort99, isvisible = self.isvisible_add, ispublic = self.ispublic_add, target = self.target, alert_url = self.alert_url)
        sleep(3)
        print("页面添加两个模块:" + self.module1 + '、' + self.module2 + "，排序分别为：" + self.sort98 + "、" + self.sort99)
        sleep(2)
        dr.switch_to.parent_frame()
        sleep(1)
        Module(dr).button_refresh.click()
        sleep(1)
        dr.switch_to.frame(Module(dr).iframe_sw[1])
        sleep(1)
        #点击测试模块资源树
        Module(dr).tree_name(self.parentname).click()
        sleep(1)
        tx = variable.get_table(dr)
        index = None
        index1 = None
        for i in range(len(tx)):
            if tx[i][0] == self.module1:
                index = i
            elif tx[i][0] == self.module2:
                index1 = i
            if index != None and index1 != None:
                break
        if index < index1:
            print("初始排序正确，模块" + self.module1 + "排在前面")
        else:
            raise ("排序错误")
        print("修改" + self.module2 + "的排序")
        sleep(2)
        element = Module(dr).operation(modulename=self.module2, ope="编辑")
        sleep(2)
        dr.execute_script("arguments[0].click();", element)
        sleep(1)
        dr.switch_to.frame(Module(dr).iframe_d)
        sleep(1)
        Module(dr).module_sort.clear()
        sleep(1)
        Module(dr).module_sort.send_keys(str(int(self.sort99) - 2))
        print("修改模块排序为：" + str(int(self.sort99) - 2))
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        Module(dr).submit.click()
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        Module(dr).button_refresh.click()
        sleep(1)
        dr.switch_to.frame(Module(dr).iframe_sw[1])
        sleep(1)
        # 点击测试模块资源树
        Module(dr).tree_name(self.parentname).click()
        sleep(1)
        tx = variable.get_table(dr)
        index = None
        index1 = None
        for i in range(len(tx)):
            if tx[i][0] == self.module1:
                index = i
            elif tx[i][0] == self.module2:
                index1 = i
            if index != None and index1 != None:
                break
        if index > index1:
            print("初始排序正确，模块" + self.module2 + "排在前面")
        else:
            raise ("排序错误")

    @BeautifulReport.add_test_img("test_9_del_batches")
    def test_9_del_batches(self):
        '''批量删除用户'''
        print("--------------------批量删除用户-----------------------")
        dr = self.dr
        dr.switch_to.frame(User(dr).iframe_sw[1])
        sleep(1)
        # 点击测试模块资源树
        Module(dr).tree_name(self.parentname).click()
        sleep(1)
        tx = variable.get_table(dr)
        for i in range(len(tx)):
            if tx[i][0] == self.module1:
                print("当前批量删除模块在列表行数：", str(i+1))
                sleep(1)
                User(dr).checkbox_del(i=str(i+1)).click()
                print("选择要删除模块前的复选框按钮")
                break
            elif i==len(tx)-1:
                raise ("test_9_del_batches:没有找到要删除的用户" + self.module1)
            else:
                continue
        for i in range(len(tx)):
            if tx[i][0] == self.module2:
                print("当前批量删除模块在列表行数：", str(i + 1))
                sleep(1)
                User(dr).checkbox_del(i=str(i + 1)).click()
                print("选择要删除模块前的复选框按钮")
                break
            elif i==len(tx)-1:
                raise ("test_9_del_batches:没有找到要删除的用户" + self.module2)
            else:
                continue
        sleep(2)
        User(dr).del_all_button.click()
        print("点击批量删除按钮")
        sleep(1)
        ts = User(dr).toast_info.get_attribute('textContent')
        self.assertEqual(ts, "确定删除吗？")
        print("提示：" + ts)
        User(dr).submit.click()
        sleep(1)
        print("点击确定")
        sleep(1)
        tx = variable.get_table(dr)
        for j in range(len(tx)):
            self.assertNotEqual(tx[j][0], self.module1)
            self.assertNotEqual(tx[j][0], self.module2)
        sleep(1)
        print("验证列表中数据被成功删除")

    @BeautifulReport.add_test_img("test_9a_public_module")
    def test_9a_public_module(self):
        '''公开模块验证'''
        print("--------------------公开模块验证-----------------------")
        dr =self.dr
        print("数据库初始化：插入模块不公开")
        dr.switch_to.frame(User(dr).iframe_sw[1])
        sleep(1)
        # 验证模块不公开
        element = variable.check_modules(dr, parent=self.modulename_public)
        self.assertEqual(element, False, msg="数据库插入模块公开")
        # 点击编辑按钮
        element = Module(dr).operation(self.modulename_public, '编辑')
        dr.execute_script("arguments[0].click();", element)
        sleep(1)
        dr.switch_to.frame(Module(dr).iframe_d)
        sleep(1)
        print("修改模块，设置为公开")
        Module(dr).module_ispublic.click()
        sleep(1)
        Module(dr).module_public.click()
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        Module(dr).confirm_button.click()
        sleep(1)
        print("点击确定按钮")
        sleep(1)
        #用户登录系统查看模块：公开
        dr1 = webdriver.Chrome()
        dr1.get(self.url)
        dr1.maximize_window()  # 将浏览器最大化
        login(dr1, self.userid, self.password, self.checkKey)  # 输入用户名、密码、验证码后登陆
        for i in range(10):
            if dr1.current_url == self.homeUrl:
                break
            else:
                print('登录等待中...')
                sleep(2)
        self.assertEqual(dr.current_url,self.homeUrl,msg="登录平台异常")
        try:
            element = variable.check_modules(dr1, parent=self.modulename_public)
            self.assertNotEqual(element, False)
            print(self.modulename_public + "模块公开展示")
        except:
            dr1.quit()
            raise ("设置公开的模块未公开展示")

    @BeautifulReport.add_test_img("test_9b_visible_module")
    def test_9b_visible_module(self):
        '''可见模块验证'''
        print("--------------------可见模块验证-----------------------")
        dr =self.dr
        print("数据库初始化：插入模块不可见")
        # 验证模块不可见
        element = variable.check_modules(dr, parent=self.modulename_visible)
        self.assertEqual(element, False, msg="数据库插入模块可见")
        sleep(1)
        dr.switch_to.frame(User(dr).iframe_sw[1])
        sleep(1)
        # 点击编辑按钮
        element = Module(dr).operation(self.modulename_visible, '编辑')
        dr.execute_script("arguments[0].click();", element)
        sleep(1)
        dr.switch_to.frame(Module(dr).iframe_d)
        sleep(1)
        print("修改模块，设置为可见")
        Module(dr).module_isvisible.click()
        sleep(1)
        Module(dr).module_visible.click()
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        Module(dr).confirm_button.click()
        sleep(1)
        print("点击确定按钮")
        sleep(1)
        # admin用户登录系统查看模块：可见
        dr.switch_to.parent_frame()
        sleep(1)
        Module(dr).button_refresh.click()
        sleep(1)
        try:
            element = variable.check_modules(dr, parent=self.modulename_public)
            self.assertNotEqual(element, False)
            print(self.modulename_public + "模块公开展示")
        except:
            raise ("设置公开的模块未公开展示")


if __name__=="__main__":
    unittest.main()

