# coding=utf-8
"""
作者：
    王波
"""

from BasePage import wait_element
from BasePage import wait_elements
from time import sleep
class Role(object):
    """摄像机设置页面"""

    def __init__(self, dr):
        self.dr = dr

    @property
    def role_btn(self):
        return wait_element(self.dr, 'By.LINK_TEXT', u"角色管理")

    @property
    def sys_manger_btn(self):
        return wait_element(self.dr,'By.CSS_SELECTOR',"a[lay-tips='系统管理']")

    #定位iframe嵌套元素
    @property
    def iframe_sw(self):
        return wait_elements(self.dr,'By.CLASS_NAME','layadmin-iframe')

    @property
    def iframe_auto(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","iframe[scrolling='auto']")

    #当前定位到的标签页
    @property
    def curr_lable(self):
        return wait_element(self.dr,'By.XPATH',"//*[@class='layui-this']/span")

    @property
    def tree_level1(self):
        return wait_elements(self.dr,"By.CSS_SELECTOR","a[class='level1']")

    #提示toast
    @property
    def toast_info(self):
        return wait_element(self.dr,"By.CLASS_NAME","layui-layer-content",timeout=15)

    #添加角色元素

    @property
    def input_rolename(self):
        return wait_element(self.dr,"By.ID","roleName")

    @property
    def list_parentrole(self):
        return wait_element(self.dr,"By.ID","parentRoleName")

    @property
    def input_sort(self):
        return wait_element(self.dr,"By.ID","sort")

    @property
    def input_remarks(self):
        return wait_element(self.dr,"By.ID","backup")

    @property
    def add_role(self):
        return wait_element(self.dr,'By.CSS_SELECTOR',"button[lay-event='add']")

    @property
    def del_user(self):
        return wait_element(self.dr,'By.CSS_SELECTOR',"a[lay-event='del']")

    @property
    def submit(self):
        return wait_element(self.dr,'By.CLASS_NAME',"layui-layer-btn0")

    @property
    def tree_admin(self):
        return wait_element(self.dr,'By.CSS_SELECTOR',"a[title='admin']")

    @property
    def role_add_user_btn(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","button[onclick='showAddUserForm()']")

    @property
    def input_user(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","input[placeholder='请选择'")

    @property
    def choose_list(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","dd[class='layui-this']")

    @property
    def add_user_submit(self):
        return wait_element(self.dr,"By.ID","addUserBtn")

    @property
    def add_Mod_submit(self):
        return wait_element(self.dr,"By.ID","btn-save")

    @property
    def btn_search(self):
        return wait_element(self.dr,"By.ID","LAY-app-search")

    @property
    def text_search(self):
        return wait_element(self.dr,"By.ID",'roleName')

    @property
    def btn_reset(self):
        return wait_element(self.dr, "By.CSS_SELECTOR", "button[type='reset']")

    @property
    def btn_batdel(self):
        return wait_element(self.dr, "By.CSS_SELECTOR", "button[lay-event='batchdel']")





    def role_add(self,rolename=None,parentrole=None,sort=None,Ismanger=None,remarks=None):
        print("点击添加角色按钮")
        Role(self.dr).add_role.click()
        sleep(1)
        self.dr.switch_to.frame('layui-layer-iframe1')  # 定位到添加弹框
        sleep(1)
        Role(self.dr).input_rolename.send_keys(rolename)
        print("输入角色名称：" + rolename)
        Role(self.dr).input_sort.send_keys(sort)
        if remarks != None:
            Role(self.dr).input_remarks.send_keys(remarks)
        if parentrole != None:
            Role(self.dr).list_parentrole.click()
            sleep(1)
            self.dr.switch_to.frame('layui-layer-iframe1')
            sleep(1)
            for i in range(30):
                id = "ztree_" + str(i+1) + "_span"
                tree = wait_element(self.dr, "By.ID", id)
                if tree != False:
                    if tree.get_attribute('textContent') == parentrole:
                        tree.click()
                        self.dr.switch_to.parent_frame()
                        sleep(1)
                        Role(self.dr).submit.click()
                        sleep(1)
                        break
                else:
                    raise ("未找到指定的上级角色")
        self.dr.switch_to.parent_frame()  # 确定按钮和弹框不在一个iframe里，需要跳到上级ifranme中
        Role(self.dr).submit.click()
        print("点击确定按钮")




    def operation(self,depName,ope):
        #self.dr.switch_to.frame(Department(self.dr).iframe_sw[1])
        x = 1
        if ope == "配置模块":
            j = 1
        elif ope == "配置用户":
            j= 2
        elif ope == "编辑":
            j = 3
        elif ope == "删除":
            j = 4
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

    def Module_checkBox(self,module):
        for i in range(50):
            i = i+1
            id = "moduleTree_"+str(i)
            element = wait_element(self.dr,"By.ID",id)
            if element == False:
                print("未找到指定元素")
                break
            else:
                if element.get_attribute("textContent") == module:
                    checkboxId = id + "_check"
                    return wait_element(self.dr,"By.ID",checkboxId)
                else:
                    continue





