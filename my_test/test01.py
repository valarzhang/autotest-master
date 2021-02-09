# coding=utf-8
"""
作者：
    王波
"""

from BasePage import wait_element
from BasePage import wait_elements
from time import sleep
class Department(object):
    """摄像机设置页面"""

    def __init__(self, dr):
        self.dr = dr

    #左侧菜单页
    @property
    def sys_manger_btn(self):
        return wait_element(self.dr,'By.CSS_SELECTOR',"a[lay-tips='系统管理']")

    # 左侧菜单页
    @property
    def department_btn(self):
        return wait_element(self.dr, 'By.LINK_TEXT', u"部门管理")

    #页面去后首页后的第一个标签页
    @property
    def fist_lable(self):
        return wait_element(self.dr,'By.XPATH','//*[@id="LAY_app_tabsheader"]/li[2]/span')
    #当前定位到的标签页
    @property
    def curr_lable(self):
        return wait_element(self.dr,'By.XPATH',"//*[@class='layui-this']/span")

    #定位iframe嵌套元素
    @property
    def iframe_sw(self):
        return wait_elements(self.dr,'By.CLASS_NAME','layadmin-iframe')

    #结构树-----------------------------------------------------

    #######获取结构树名称元素：
    @property
    def root_tree(self):
        return wait_element(self.dr,'By.ID','tree_1_span')

    @property
    def second_tree(self):
        return wait_element(self.dr, 'By.ID', 'tree_2_span')

    @property
    def third_tree(self):
        return wait_element(self.dr, 'By.ID', 'tree_3_span')

    @property
    def fourth_tree(self):
        return wait_element(self.dr, 'By.ID', 'tree_4_span')

    #操作结构树元素：
    @property
    def tree_sw1(self):
        return wait_element(self.dr, 'By.ID', 'tree_1_switch')

    @property
    def tree_u(self): #根据该元素判断树状结构是否被收缩
        return wait_element(self.dr, 'By.ID', 'tree_1_ul')
    @property
    def tree_level1(self):
        return wait_elements(self.dr,"By.CSS_SELECTOR","a[class='level1']")

    @property
    def btn_switch_close(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","span[class = 'button level1 switch center_close']")


    def tree_name(self,departName):
        return wait_element(self.dr,"By.CSS_SELECTOR",'a[title = %s'%(departName)+"]")



    #操作------------------------------------------------------------
    @property
    def add_department(self):
        return wait_element(self.dr,'By.CSS_SELECTOR',"button[lay-event='add']")

    @property
    def checkBoxs_all(self):
        return wait_element(self.dr,'By.XPATH',"/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/table/thead/tr/th/div/div/i")

    @property
    def btn_del_all(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","button[lay-event='batchdel']")

    @property
    def btn_search(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","button[lay-filter='LAY-app-search']")

    @property
    def btn_reset(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","button[type='reset']")





    #添加部门弹框----------------------------------------------------------
    @property
    def input_deptname(self):
        return wait_element(self.dr,"By.ID","deptName")

    @property
    def read_code(self):
        return wait_element(self.dr,"By.ID","deptCode")

    @property
    def chose_department(self):
        return wait_element(self.dr,"By.ID","parentDeptName")

    @property
    def input_sort(self):
        return wait_element(self.dr,"By.ID","sort")

    @property
    def submit(self):
        return wait_element(self.dr,'By.CLASS_NAME',"layui-layer-btn0")


    @property
    def add_cancel(self):
        return wait_element(self.dr,'By.CLASS_NAME','layui-layer-btn1')

    #提示toast
    @property
    def toast_info(self):
        return wait_element(self.dr,"By.CLASS_NAME","layui-layer-content",timeout=15)

    #查看弹框中的返回
    @property
    def backToList(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","button[onclick='backToList()']")





    #添加部门
    def add_dep(self,deptname=None,sort=None,group=None):
        if deptname == None or sort == None:
            raise ("deptname和sort不能为空")
        self.dr.switch_to.frame(Department(self.dr).iframe_sw[1])
        sleep(2)
        Department(self.dr).add_department.click()
        print("添加一级部门，点击添加按钮")
        sleep(1)
        self.dr.switch_to.frame('layui-layer-iframe1')  # 定位到添加弹框
        sleep(1)
        Department(self.dr).input_deptname.send_keys(deptname)
        print("输入部门名称：" + deptname)
        sleep(1)
        Department(self.dr).input_sort.send_keys(sort)
        print("输入排序：" + str(sort))
        sleep(1)
        if group != None:
            print("点击上级部门")
            Department(self.dr).chose_department.click()
            sleep(1)
            self.dr.switch_to.frame('layui-layer-iframe1')
            sleep(1)
            h = 2
            for i in range(30):
                id = "tree_" + str(h) + "_span"

                tree = wait_element(self.dr, "By.ID", id)
                if tree != False:
                    if tree.get_attribute('textContent') == group:
                        tree.click()
                        self.dr.switch_to.parent_frame()
                        sleep(1)
                        Department(self.dr).submit.click()
                        sleep(1)
                        break
                    else:
                        h = h+1
                else:
                    raise ("未找到指定的上级部门")

        self.dr.switch_to.parent_frame()  # 确定按钮和弹框不在一个iframe里，需要跳到上级ifranme中
        Department(self.dr).submit.click()
        print("点击确定按钮")


    def operation(self,depName,ope):
        #self.dr.switch_to.frame(Department(self.dr).iframe_sw[1])
        x = 1
        if ope == "查看":
            j = 1
        elif ope == "编辑":
            j= 2
        elif ope == "删除":
            j = 3
        else:
            raise ("ope输入错误")
        for i in range(300):
            xpath = "/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/" + "tr[" + str(x) + "]/" + "td[2]/div"
            tr = wait_element(self.dr,"By.XPATH",xpath)
            if tr == False:
                print("未检查到名称为" + depName + "的部门")
                break
            else:
                if tr.get_attribute('textContent') == depName:
                    xpath = "html/body/div/div/div[2]/div/div/div[2]/div[1]/div[4]/div[2]/table/tbody/" + "tr[" + str(x) + "]/" + "td/div/a["+str(j)+"]"
                    btn = wait_element(self.dr,"By.XPATH",xpath)
                    return btn
                else:
                    x=x+1



    def open_tree(self,departname):
        xpath = "//*[@title=%s"%(departname)+"]/preceding-sibling::span[1]"
        btn = wait_element(self.dr,"By.XPATH",xpath)
        if btn != False:
            btn.click()
        else:
            raise ("未找到指定元素")



