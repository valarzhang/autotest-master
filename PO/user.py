# coding=utf-8
"""
作者：
    缪香香
"""

from BasePage import wait_element
from BasePage import wait_elements
from time import sleep

class User(object):
    """用户管理页面"""

    def __init__(self, dr):
        self.dr = dr
    #登录成功之后修改密码：提交按钮
    @property
    def login_submit(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","button[class='layui-btn']")

    #登录成功之后：右侧个人中心账号
    @property
    def name(self):
        return wait_element(self.dr,'By.XPATH',"/html/body/div/div/div[1]/ul[2]/li[5]/a/cite")

    #修改密码按钮
    @property
    def modify_password(self):
        return wait_element(self.dr,'By.XPATH',"/html/body/div/div/div[1]/ul[2]/li[5]/dl/dd[1]/a")

    @property
    def logout(self):
        return wait_element(self.dr,"By.XPATH","/html/body/div[1]/div/div[1]/ul[2]/li[5]/dl/dd[2]/a")
    #旧密码
    @property
    def oldPassword(self):
        return wait_element(self.dr,"By.ID","oldPassword")
    #新密码
    @property
    def newPassword(self):
        return wait_element(self.dr,'By.ID',"newPassword")
    #确认密码
    @property
    def confirmPassword(self):
        return wait_element(self.dr,'By.ID',"confirmPassword")

    #登录页面提示信息
    @property
    def login_msg(self):
        return wait_element(self.dr,"By.ID","msg")

    @property
    def button_login_submit(self):
        return wait_element(self.dr, 'By.CLASS_NAME', 'btn')

    #登录页提示信息：关闭按钮
    @property
    def msg_close(self):
        return wait_element(self.dr,'By.CSS_SELECTOR',"button[data-dismiss='modal']")
    #刷新按钮
    @property
    def button_refresh(self):
        return wait_element(self.dr,'By.CSS_SELECTOR','a[title="刷新"]')

    #左侧菜单页
    @property
    def sys_manger_btn(self):
        return wait_element(self.dr,'By.CSS_SELECTOR',"a[lay-tips='系统管理']")

    # 左侧菜单页
    @property
    def user_btn(self):
        return wait_element(self.dr, 'By.LINK_TEXT', u"用户管理")

    #当前定位到的标签页
    @property
    def curr_lable(self):
        return wait_element(self.dr,'By.XPATH',"//*[@class='layui-this']/span")

    #定位iframe嵌套元素
    @property
    def iframe_sw(self):
        return wait_elements(self.dr,'By.CLASS_NAME','layadmin-iframe')

    #查询
    @property
    def search_name(self):
        return  wait_element(self.dr,"By.ID","name")

    #搜索按钮
    @property
    def btn_search(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","button[lay-filter='LAY-app-search']")

    #禁用用户：是/否
    @property
    def disable_user(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","input[placeholder='请选择']")

    #选择禁用用户：否
    @property
    def button_disable_user(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","dd[class='layui-this']")

    #选择禁用用户：是
    @property
    def button_able_user(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","dd[lay-value='0']")

    #重置按钮
    @property
    def reset(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","button[class='layui-btn layui-btn-primary']")

    #操作------------------------------------------------------------
    #添加用户按钮
    @property
    def add_user(self):
        return wait_element(self.dr,'By.CSS_SELECTOR',"button[lay-event='add']")

    #添加用户弹框----------------------------------------------------------
    @property
    def iframe_dep(self):
        return wait_element(self.dr,'By.ID',"layui-layer-iframe1")

    #添加用户打开后页面title
    @property
    def add_user_title(self):
        return wait_element(self.dr, 'By.CLASS_NAME', "layui-layer-title")

    #打开所属部门窗口
    @property
    def input_deptname(self):
        return wait_element(self.dr, "By.ID", "deptName")

    # 所属部门窗口title
    @property
    def assert_department(self):
        return wait_element(self.dr,"By.CLASS_NAME","layui-layer-title")

    # 选择所属部门
    @property
    def choose_department(self):
        return wait_element(self.dr, "CLASS_NAME", "layui-layer-title")

    def tree_name(self,departName):
        return wait_element(self.dr,"By.CSS_SELECTOR",'a[title = %s'%(departName)+"]")

    #选择所属部门提交按钮
    @property
    def submit(self):
        return wait_element(self.dr,'By.CLASS_NAME',"layui-layer-btn0")

    #输入姓名
    @property
    def input_name(self):
        return  wait_element(self.dr,"By.ID","name")

    #输入用户名
    @property
    def input_userId(self):
        return  wait_element(self.dr,"By.ID","userId")

    #输入mobile
    @property
    def input_mobile(self):
        return  wait_element(self.dr,"By.ID","mobile")

    #选择出生日期
    @property
    def input_birthday(self):
        return  wait_element(self.dr,"By.ID","birthday")

    #点击前一个年份
    @property
    def choose_year(self):
        return wait_element(self.dr,'By.XPATH',"/html/body/div/div[1]/div[1]/i[1]")

    #点击前一个月份
    @property
    def choose_month(self):
        return wait_element(self.dr,'By.XPATH',"/html/body/div/div[1]/div[1]/i[2]")

    #选择出生日期:确定按钮
    @property
    def commit_button_birthday(self):
        return wait_element(self.dr,"By.CLASS_NAME","laydate-btns-confirm")

    #选择性别
    @property
    def input_gender(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","input[placeholder='请选择']")

    #选择性别:女
    @property
    def commit_button_gender(self):
        return wait_element(self.dr,"By.XPATH","/html/body/form/div[6]/div/div/dl/dd[3]")

    #选择性别：男
    @property
    def commit_button_man(self):
        return wait_element(self.dr,"By.XPATH","/html/body/form/div[6]/div/div/dl/dd[2]")

    #输入email
    @property
    def input_email(self):
        return  wait_element(self.dr,"By.ID","email")

    #输入sort
    @property
    def input_sort(self):
        return  wait_element(self.dr,"By.ID","sort")

    #关联部门按钮："+"
    @property
    def relate_dept(self):
        return wait_element(self.dr,"By.ID","depts")

    #关联部门窗口title
    @property
    def relate_dept_title(self):
        return wait_element(self.dr,"By.CLASS_NAME","layui-layer-title")

    @property
    def iframe_relate_dep(self):
        return wait_element(self.dr,'By.CSS_SELECTOR',"iframe[scrolling='auto']")

    def delete_relate_dept(self,relate_dept):
        return wait_element(self.dr,'By.LINK_TEXT',relate_dept)

    #关联部门：确认按钮
    @property
    def commit_button_relate_dept(self):
        return wait_element(self.dr,"By.ID","btn-save")

    #关联角色按钮:"+"
    @property
    def relate_role(self):
        return wait_element(self.dr,"By.ID","roles")

    @property
    def iframe_relate_role(self):
        return wait_element(self.dr,'By.CSS_SELECTOR',"iframe[scrolling='auto']")

    #关联角色：确认按钮
    @property
    def commit_button_relate_role(self):
        return wait_element(self.dr,"By.ID","btn-save")

    #新增用户确定按钮
    @property
    def submit_button(self):
        return wait_element(self.dr,'By.CLASS_NAME','layui-layer-btn0')

    #查看用户页面title
    @property
    def user_title(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","div[class='layui-layer-title']")

    #查看用户页面：字段部门
    @property
    def view_deptname(self):
        return wait_element(self.dr,"By.ID","deptName")

    #查看用户页面：字段姓名
    @property
    def view_username(self):
        return wait_element(self.dr,"By.ID","name")

    #查看用户页面：字段用户名
    @property
    def view_userId(self):
        return wait_element(self.dr,"By.ID","userId")

    #查看用户页面：字段手机
    @property
    def view_mobile(self):
        return wait_element(self.dr,"By.ID","mobile")

    #查看用户页面：字段email
    @property
    def view_email(self):
        return wait_element(self.dr,"By.ID","email")

    #查看用户页面：关联部门
    @property
    def view_deptNames(self):
        return wait_element(self.dr,"By.ID","deptNames")

    #查看用户页面：关联角色
    @property
    def view_roleNames(self):
        return wait_element(self.dr,"By.ID","roleNames")

    #查看用户页面：禁用按钮
    @property
    def view_disable_user(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","button[onclick='userDisable()']")

    #查看用户页面：激活按钮
    @property
    def view_able_user(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","button[onclick='userEnable()']")

    #查看用户页面：初始化密码按钮
    @property
    def view_init_password(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","button[id='initPassword']")

    #查看用户页面：解除锁定按钮
    @property
    def view_clearUserLock(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","button[id='clearUserLock']")

    #查看页面：返回按钮
    @property
    def backToList(self):
        return wait_element(self.dr,"By.ID","backToList")

    @property
    def choose_all(self):
        return wait_element(self.dr,'By.XPATH','/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/table/thead/tr/th/div/div/i')

    #批量删除：复选框
    def checkbox_del(self,i):
        return wait_element(self.dr,"By.XPATH","/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/table/tbody/tr["+i+"]/td/div/div/i")

    #批量删除：按钮
    @property
    def del_all_button(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","button[lay-event='batchdel']")

    #提示toast
    @property
    def toast_info(self):
        return wait_element(self.dr,"By.CLASS_NAME","layui-layer-content",timeout=15)

    #页面刷新按钮
    @property
    def refresh_button(self):
        return wait_element(self.dr,'By.CSS_SELECTOR','a[layadmin-event="refresh"]')

    #添加用户
    def add_user_model(self,parentdept,username,userId,mobile,email,sort,relate_deptname=None,relate_role=None):
        dr = self.dr
        # 定位到树形结构所属的iframe
        dr.switch_to.frame(User(dr).iframe_sw[1])
        sleep(2)
        print("定位到添加按钮所在的iframe")
        User(dr).add_user.click()
        sleep(1)
        print("点击添加用户按钮")
        sleep(1)
        dr.switch_to.frame(User(dr).iframe_dep)  # 定位到添加弹框
        sleep(2)
        print("定位到选择所在部门的iframe")
        User(dr).input_deptname.click()
        sleep(2)
        dr.switch_to.frame(User(dr).iframe_dep)
        # 点击选择用户所属部门
        if User(dr).tree_name(departName=parentdept) != False:
            print("选择上级部门")
            User(dr).tree_name(departName=parentdept).click()
        else:
            raise ("未找到所属部门：",parentdept)
        dr.switch_to.parent_frame()  # 确定按钮和弹框不在一个iframe里，需要跳到上级iframe中
        User(dr).submit.click()
        print("点击确定按钮")
        sleep(1)
        # 输入姓名
        User(dr).input_name.send_keys(username)
        sleep(1)
        print("输入姓名")
        # 输入用户名
        User(dr).input_userId.send_keys(userId)
        sleep(1)
        print("输入用户名")
        # 输入手机号
        User(dr).input_mobile.send_keys(mobile)
        sleep(1)
        print("输入手机号")
        # 选择出生日期
        User(dr).input_birthday.click()
        sleep(1)
        # 选择当前年份之前的一年
        User(dr).choose_year.click()
        sleep(1)
        # 选择当前月份之前的一月
        User(dr).choose_month.click()
        sleep(1)
        # 点击确定按钮
        User(dr).commit_button_birthday.click()
        sleep(1)
        print("选择出生日期")
        # 输入性别
        User(dr).input_gender.click()
        sleep(1)
        User(dr).commit_button_gender.click()
        sleep(1)
        print("选择性别")
        # 输入邮箱
        User(dr).input_email.send_keys(email)
        sleep(1)
        print("输入邮箱")
        # 输入排序
        User(dr).input_sort.send_keys(sort)
        sleep(1)
        print("输入排序")
        sleep(2)
        if relate_deptname != None:
            # 关联部门
            User(dr).relate_dept.click()
            sleep(2)
            # 选择关联部门：测试部门002
            dr.switch_to.frame(User(dr).iframe_relate_dep)
            sleep(2)
            # 点击选择用户关联部门layui-layer-iframe1
            if User(dr).tree_name(departName=relate_deptname) != False:
                id = User(dr).tree_name(departName=relate_deptname).get_attribute("id")
                sleep(1)
                i = id.split("_")[1]
                id_checkbox = "tree_" + str(i) + "_check"
                sleep(1)
                dr.find_element_by_id(id_checkbox).click()
            else:
                raise ("未找到关联的部门名称")
            sleep(1)
            User(dr).commit_button_relate_dept.click()
            dr.switch_to.parent_frame()  # 跳转至角色添加按钮页
            sleep(2)
        if relate_role!= None:
            # 点击添加角色按钮
            User(dr).relate_role.click()
            sleep(1)
             # 选择关联角色：测试角色001
            dr.switch_to.frame(User(dr).iframe_relate_role)
            sleep(2)
            # 点击选择用户关联角色layui-layer-iframe1
            if User(dr).tree_name(departName=relate_role)  != False:
                id = User(dr).tree_name(departName=relate_role).get_attribute("id")
                sleep(1)
                i = id.split("_")[1]
                id_checkbox = "tree_" + str(i) + "_check"
                sleep(1)
                dr.find_element_by_id(id_checkbox).click()
            else:
                raise ("未找到关联的角色名称")
            print("添加用户角色")
            sleep(1)
            User(dr).commit_button_relate_role.click()
            sleep(1)
            dr.switch_to.parent_frame()
            sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        User(dr).submit_button.click()
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)

    def edit_user(self,parentdept,username,username_new,mobile_new,email_new,sort_new,relate_deptname_new=None,relate_role_new=None):
        dr = self.dr
        sleep(1)
        dr.switch_to.frame(User(dr).iframe_sw[1])
        sleep(2)
        print("点击" + username + "用户的编辑按钮")
        element = User(dr).operation(username, ope="编辑")
        sleep(1)
        dr.execute_script("arguments[0].click();",element)
        sleep(1)
        dr.switch_to.frame(User(dr).iframe_dep)  # 定位到添加弹框
        sleep(2)
        print("定位到选择所在部门的iframe")
        User(dr).input_deptname.click()
        sleep(2)
        dr.switch_to.frame(User(dr).iframe_dep)
        sleep(2)
        # 点击选择用户所属部门
        if User(dr).tree_name(departName=parentdept)  != False:
            print("选择上级部门")
            User(dr).tree_name(departName=parentdept).click()
        else:
            raise ("未找到所属部门：", parentdept)
        dr.switch_to.parent_frame()  # 确定按钮和弹框不在一个iframe里，需要跳到上级iframe中
        sleep(1)
        User(dr).submit.click()
        print("点击确定按钮")
        sleep(1)
        # 修改姓名
        User(dr).input_name.clear()
        sleep(1)
        User(dr).input_name.send_keys(username_new)
        sleep(1)
        print("修改姓名")
         # 修改手机号
        User(dr).input_mobile.clear()
        sleep(1)
        User(dr).input_mobile.send_keys(mobile_new)
        sleep(1)
        print("修改手机号")
        # 修改出生日期
        User(dr).input_birthday.click()
        sleep(1)
        # 选择当前年份之前的一年
        User(dr).choose_year.click()
        sleep(1)
        # 选择当前月份之前的一月
        User(dr).choose_month.click()
        sleep(1)
        # 点击确定按钮
        User(dr).commit_button_birthday.click()
        sleep(1)
        print("选择出生日期")
        # 修改性别
        User(dr).input_gender.click()
        sleep(1)
        User(dr).commit_button_man.click()
        sleep(1)
        print("选择性别")
        # 输入邮箱
        User(dr).input_email.clear()
        User(dr).input_email.send_keys(email_new)
        sleep(1)
        print("修改邮箱")
        # 输入排序
        User(dr).input_sort.clear()
        User(dr).input_sort.send_keys(sort_new)
        sleep(1)
        print("输入排序")
        sleep(2)
        if relate_deptname_new!= None:
            # 关联部门
            User(dr).relate_dept.click()
            sleep(1)
            # 选择关联部门：测试部门002
            dr.switch_to.frame(User(dr).iframe_relate_dep)
            sleep(2)
            # 点击选择用户关联部门layui-layer-iframe1
            if User(dr).tree_name(departName=relate_deptname_new)  != False:
                id = User(dr).tree_name(departName=relate_deptname_new).get_attribute("id")
                sleep(1)
                i = id.split("_")[1]
                id_checkbox = "tree_" + str(i) + "_check"
                sleep(1)
                dr.find_element_by_id(id_checkbox).click()
            else:
                raise ("未找到关联的部门名称")
            print("修改用户关联部门")
            sleep(1)
        if relate_deptname_new!=None:
            User(dr).commit_button_relate_dept.click()
            sleep(1)
            dr.switch_to.parent_frame()  # 跳转至角色添加按钮页
            sleep(2)
            # 点击添加角色按钮
            User(dr).relate_role.click()
            sleep(1)
            # 选择关联角色：测试角色001
            dr.switch_to.frame(User(dr).iframe_relate_role)
            sleep(2)
            # 点击选择用户关联角色layui-layer-iframe1
            if User(dr).tree_name(departName=relate_role_new)  != False:
                id = User(dr).tree_name(departName=relate_role_new).get_attribute("id")
                sleep(1)
                i = id.split("_")[1]
                id_checkbox = "tree_" + str(i) + "_check"
                sleep(1)
                dr.find_element_by_id(id_checkbox).click()
            else:
                raise ("未找到关联的角色名称")
            print("修改用户角色")
            sleep(1)
            User(dr).commit_button_relate_role.click()
            sleep(1)
            dr.switch_to.parent_frame()
            sleep(1)
            dr.switch_to.parent_frame()
            sleep(1)
        User(dr).submit_button.click()
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)

    def operation(self, username, ope):
        # self.dr.switch_to.frame(Department(self.dr).iframe_sw[1])
        x = 1
        if ope == "查看":
            j = 1
        elif ope == "编辑":
            j = 2
        elif ope == "删除":
            j = 3
        else:
            raise ("ope输入错误")
        for i in range(300):
            xpath = "/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/tr["+str(x)+"]/td[2]/div"
            tr = wait_element(self.dr, "By.XPATH", xpath)
            if tr == False:
                print("未检查到名称为" + username + "的用户")
                break
            else:
                if tr.get_attribute('textContent') == username:
                    xpath="/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/tr["+str(x)+"]/td[5]/div/a["+str(j)+"]"
                    btn = wait_element(self.dr, "By.XPATH", xpath)
                    return btn
                else:
                    x = x + 1
