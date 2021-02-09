import unittest
from selenium import webdriver
from time import sleep
import variable
from PO.department import Department
from BasePage import wait_element
from configparser import ConfigParser
from BasePage import skip_dependon
from db_fixture import test_dataForDepartment
from BeautifulReport import BeautifulReport

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
        cls.deptname = conf.get('DEPARTMENT', 'deptname')
        cls.deptnameEdit = conf.get('DEPARTMENT', 'deptnameEdit')
        cls.childDepartname = conf.get('DEPARTMENT','childDepartName')
        cls.deptnameinit1 = conf.get('DEPARTMENT','deptnameinit1')
        cls.deptnameinit2 = conf.get('DEPARTMENT','deptnameinit2')
        cls.sort4 = conf.get('DEPARTMENT', 'sort4')
        cls.sort1 = conf.get('DEPARTMENT', 'sort1')
        cls.department1 = conf.get('DEPARTMENT', 'department1')
        cls.department2 = conf.get('DEPARTMENT', 'department2')
        cls.sort98 = conf.get('DEPARTMENT', 'sort98')
        cls.sort99 = conf.get('DEPARTMENT', 'sort99')

        print("开始执行部门管理脚本")
        dr =webdriver.Chrome()            #启动chrom浏览器
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
        Department(dr).sys_manger_btn.click()
        print("点击左侧菜单’系统管理‘")
        sleep(1)
        #点击部门管理标签页
        Department(dr).department_btn.click()
        print("点击左侧菜单’部门管理‘")
        sleep(1)
        #检查是否打开部门管理标签页
        self.assertNotEqual(Department(dr).curr_lable,False,msg="未打开部门管理标签页")
        self.assertEqual(Department(dr).curr_lable.get_attribute('textContent'),'部门管理',msg="打开的不是部门管理标签页")

    def tearDown(self):
        print("刷新页面，返回首页")
        self.dr.refresh() #刷新页面，返回首页
        sleep(1)



    def test_1_init_tree(self):
        print("--------------------开始执行第一条用例，检查初始组织结构树-----------------------")
        dr = self.dr
        #定位到树形结构所属的iframe
        dr.switch_to.frame(Department(dr).iframe_sw[1])
        sleep(1)
        print("检查初始页面，左侧的一级角色与列表中展示的一级角色是否一致")
        rx = Department(dr).tree_level1
        tree = []
        print("开始获取左侧一级角色")
        for i in range(len(rx)):
            tree.append(rx[i].get_attribute('textContent'))
        tx = variable.get_table(dr)
        table = []
        print("开始获取列表中一级角色")
        for i in range(len(tx)):
            table.append(tx[i][0])

        self.assertEqual(tree, table, msg="左侧结构图中的角色与列表中的角色不一致")
        print("左侧结构图中的角色与列表中的角色一致")


    def test_3_add(self):
        print("--------------------开始执行第三条用例，添加部门-----------------------")
        dr = self.dr
        Department(dr).add_dep(deptname=self.deptname,sort=self.sort4)
        sleep(1)
        try:
            text = Department(dr).toast_info.get_attribute('textContent')  #info消息偶尔会定位失败
            self.assertEqual(text, "提交成功")
            print("提示：提交成功")
        except:
            print("根据页面列表数据判断是否提交成功")
        print("列表内容正确，部门列表最下方新增一个部门："+self.deptname)
        Department(dr).operation(depName=self.deptname,ope="查看").click()
        sleep(1)
        print("点击查看按钮，检查弹框内的内容")
        self.dr.switch_to.frame('layui-layer-iframe3')
        sleep(1)
        Department(dr).backToList.click()
        sleep(2)
        dr.switch_to.parent_frame()

    @skip_dependon(depend='test_3_add')
    def test_4_edit(self):
        print("--------------------开始执行第四条用例，编辑部门-----------------------")
        dr = self.dr
        self.dr.switch_to.frame(Department(self.dr).iframe_sw[1])
        sleep(1)
        print("点击"+self.deptname+"部门的编辑按钮")
        Department(dr).operation(depName=self.deptname, ope="编辑").click()
        sleep(1)
        self.dr.switch_to.frame('layui-layer-iframe1')
        sleep(1)
        print("修改部门名称为："+self.deptnameEdit)
        Department(dr).input_deptname.clear()
        sleep(1)
        Department(dr).input_deptname.send_keys(self.deptnameEdit)
        sleep(1)
        Department(dr).input_sort.clear()
        sleep(1)
        Department(dr).input_sort.send_keys(self.sort1)
        print("修改部门排序为："+str(self.sort1))
        sleep(1)
        dr.switch_to.parent_frame()
        Department(dr).submit.click()
        print("点击确认")
        try:
            text = Department(dr).toast_info.get_attribute('textContent')  #info消息偶尔会定位失败
            self.assertEqual(text, "提交成功")
            print("提示：提交成功")
        except:
            print("根据页面列表数据判断是否提交成功")
        sleep(1)
        Department(dr).operation(depName=self.deptnameEdit, ope="查看").click()
        print("点击该部门的查看按钮")
        sleep(1)
        self.dr.switch_to.frame('layui-layer-iframe3')
        sleep(1)
        self.assertEqual(Department(dr).input_sort.get_attribute("value"),self.sort1)
        self.assertEqual(Department(dr).input_deptname.get_attribute("value"),self.deptnameEdit)
        print("查看页面显示正确，部门："+self.deptnameEdit+"排序："+str(self.sort1))


    @skip_dependon(depend='test_4_edit')
    def test_5_del(self):
        print("--------------------开始执行第五条用例，删除部门-----------------------")
        dr = self.dr
        self.dr.switch_to.frame(Department(self.dr).iframe_sw[1])
        sleep(1)
        print("找到"+self.deptnameEdit+"部门后，点击删除按钮")
        Department(dr).operation(depName=self.deptnameEdit, ope="删除").click()
        sleep(1)
        print("点击确定")
        Department(dr).submit.click()
        try:
            text = Department(dr).toast_info.get_attribute('textContent')  #info消息偶尔会定位失败
            self.assertEqual(text, "删除成功")
            print("提示：删除成功")
        except:
            print("根据页面列表数据判断是否提交成功")
        tx = variable.get_table(dr)
        print("开始检查列表中部门是否被删除")
        for i in range(len(tx)):
            self.assertNotEqual(tx[i][0],self.deptnameEdit)
        sleep(1)
        print("列表中的"+self.deptnameEdit+"部门已经被删除")

    def test_6_childadd(self):
        print("--------------------开始执行第六条用例，创建子级部门-----------------------")
        dr = self.dr
        Department(dr).add_dep(deptname=self.childDepartname, sort=self.sort4,group=self.deptnameinit1)
        sleep(1)
        try:
            text = Department(dr).toast_info.get_attribute('textContent')  # info消息偶尔会定位失败
            self.assertEqual(text, "提交成功")
            print("提示：提交成功")
        except:
            print("根据页面列表数据判断是否提交成功")

        Department(dr).btn_switch_close.click()
        sleep(1)
        lev =Department(dr).tree_name(departName=self.childDepartname).get_attribute('class')
        print(lev)
        self.assertEqual(lev,"level2")
        print("结构树中%s"%(self.childDepartname)+"的级别为：%s"%(lev)+",级别显示正确")
        Department(dr).tree_name(departName=self.deptnameinit1).click()
        sleep(1)
        tx = variable.get_table(dr)
        self.assertEqual(len(tx),1)
        self.assertEqual(tx[0][0],self.childDepartname)
        print("列表中数据显示正确")

    @skip_dependon(depend='test_6_childadd')
    def test_7_del_batches(self):
        print("--------------------开始执行第七条用例，批量删除部门-----------------------")
        dr = self.dr
        self.dr.switch_to.frame(Department(self.dr).iframe_sw[1])
        sleep(1)
        Department(dr).btn_switch_close.click()
        sleep(1)
        Department(dr).tree_name(departName=self.deptnameinit1).click()
        sleep(1)
        tx = variable.get_table(dr)
        self.assertEqual(len(tx), 1)
        self.assertEqual(tx[0][0], self.childDepartname)
        print("点击左侧管理部门，该部门下含有1个子部门")
        Department(dr).checkBoxs_all.click()
        sleep(1)
        print("点击全选按钮")
        Department(dr).btn_del_all.click()
        sleep(1)
        ts = Department(dr).toast_info.get_attribute('textContent')
        self.assertEqual(ts,"确定删除吗？")
        print("提示："+ts)
        Department(dr).submit.click()
        sleep(1)
        print("点击确定")
        sleep(1)
        tx = variable.get_table(dr)
        self.assertEqual(len(tx), 0)
        print("列表中所有数据成功被删除")

    def test_8_search(self):
        print("--------------------开始执行第八条用例，搜索-----------------------")
        dr =self.dr
        self.dr.switch_to.frame(Department(self.dr).iframe_sw[1])
        tx1 = variable.get_table(dr)      #保留初始列表的数据与最后重置后搜索的结果对比
        lenth = len(tx1)
        print("初始状态下，页面有%s"%(lenth)+"条数据")
        Department(dr).input_deptname.send_keys(self.deptnameinit1+"123")
        sleep(1)
        Department(dr).btn_search.click()
        print("搜索框中输入"+self.deptnameinit1+"123后点击搜索")
        sleep(1)
        tx = variable.get_table(dr)
        self.assertEqual(len(tx),0)
        print("查询结果为空")
        Department(dr).btn_reset.click()
        sleep(1)
        print("点击重置按钮")
        Department(dr).input_deptname.send_keys(self.deptnameinit1)
        sleep(1)
        Department(dr).btn_search.click()
        print("搜索框中输入" + self.deptnameinit1 + "后点击搜索")
        tx = variable.get_table(dr)
        self.assertEqual(len(tx), 1)
        print("查询到一条数据")
        Department(dr).btn_reset.click()
        sleep(1)
        print("点击重置按钮后直接点击查询")
        sleep(1)
        Department(dr).btn_search.click()
        sleep(1)
        tx = variable.get_table(dr)
        self.assertEqual(tx1,tx)
        print("数据与初始数据一致")


    def test_9_sort(self):
        print("--------------------开始执行第九条用例，排序-----------------------")
        dr = self.dr
        self.dr.switch_to.frame(Department(self.dr).iframe_sw[1])
        test_dataForDepartment.init_data()
        print("数据库直接插入两个部门:"+self.department1+'、'+self.department2+"，排序分别为："+self.sort98+"、"+self.sort99)
        tx = variable.get_table(dr)
        index = None
        index1 = None
        for i in range(len(tx)):
            if tx[i][0] == self.department1:
                index = i
            elif tx[i][0] == self.department2:
                index1 = i
            if index != None and index1 != None:
                break
        if index < index1:
            print("初始排序正确，部门"+self.department1+"排在前面")
        else:
            raise ("排序错误")
        print("修改"+self.department2+"的排序")
        Department(dr).operation(depName=self.department2, ope="编辑").click()
        sleep(1)
        self.dr.switch_to.frame('layui-layer-iframe1')
        sleep(1)
        Department(dr).input_sort.clear()
        sleep(1)
        Department(dr).input_sort.send_keys(str(int(self.sort98)-2))
        print("修改部门排序为：" + str(int(self.sort98)-2))
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        Department(dr).submit.click()
        tx = variable.get_table(dr)
        index = None
        index1 = None
        for i in range(len(tx)):
            if tx[i][0] == self.department1:
                index = i
            elif tx[i][0] == self.department2:
                index1 = i
            if index != None and index1 != None:
                break
        if index > index1:
            print("初始排序正确，部门" + self.department2 + "排在前面")
        else:
            raise ("排序错误")















if __name__ == '__main__':
    testsuite = unittest.TestSuite()
    testsuite.addTest(MyTestCase("test_1_init_tree"))
    testsuite.addTest(MyTestCase("test_3_add"))
    testsuite.addTest(MyTestCase("test_4_edit"))
    testsuite.addTest(MyTestCase("test_5_del"))
    testsuite.addTest(MyTestCase("test_6_childadd"))
    testsuite.addTest(MyTestCase("test_7_del_batches"))
    testsuite.addTest(MyTestCase("test_8_search"))
    testsuite.addTest(MyTestCase("test_9_sort"))
    runner = unittest.TextTestRunner()
    runner.run(testsuite)















































