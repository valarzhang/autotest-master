# coding=utf-8
"""
作者：
    缪香香
"""

from BasePage import wait_element
from BasePage import wait_elements
from time import sleep

class Module(object):
    """模块管理页面"""

    def __init__(self, dr):
        self.dr = dr
    #刷新按钮
    @property
    def button_refresh(self):
        return wait_element(self.dr,'By.CSS_SELECTOR','a[title="刷新"]')

    # 左侧菜单页
    @property
    def module_btn(self):
        return wait_element(self.dr, 'By.LINK_TEXT', u"模块管理")

    #左侧菜单页
    @property
    def sys_manger_btn(self):
        return wait_element(self.dr,'By.CSS_SELECTOR',"a[lay-tips='系统管理']")

    @property
    def curr_lable(self):
        return wait_element(self.dr,'By.XPATH',"//*[@class='layui-this']/span")

    #iframe
    @property
    def iframe_sw(self):
        return wait_elements(self.dr,'By.CLASS_NAME','layadmin-iframe')

    #添加按钮
    @property
    def button_add(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","button[lay-event='add']")

    #添加父模块弹框----------------------------------------------------------
    @property
    def iframe_d(self):
        return wait_element(self.dr,'By.ID',"layui-layer-iframe1")

    @property
    def iframe_d1(self):
        return wait_element(self.dr,'By.ID',"layui-layer-iframe2")

    #添加页面：父模块
    @property
    def parent_module(self):
        return wait_element(self.dr,'By.ID','parentModuleName')

    #选择父模块
    def selector_parent_module(self,i):
        return wait_element(self.dr,'By.ID','moduleTree_'+str(i)+'_span')

    def tree_name(self,moduleName):
        return wait_element(self.dr,"By.CSS_SELECTOR",'a[title = %s'%(moduleName)+"]")



    #确认/确定按钮
    @property
    def confirm_button(self):
        return wait_element(self.dr,'By.CLASS_NAME','layui-layer-btn0')

    #添加页面：模块名称
    @property
    def module_name(self):
        return wait_element(self.dr,'By.ID','moduleName')

    #添加页面：模块地址
    @property
    def module_url(self):
        return wait_element(self.dr,'By.ID','moduleAddr')

    #添加页面：模块序号
    @property
    def module_sort(self):
        return wait_element(self.dr,'By.ID','sortSq')

    #添加页面：模块图标
    @property
    def module_icon(self):
        return wait_element(self.dr,'By.ID','icon')

    #添加页面：模块图标hot
    @property
    def module_icon_Hot(self):
        return wait_element(self.dr,'By.XPATH',"/html/body/div/ul/li[11]/i")

    #添加页面：模块图标笑脸
    @property
    def module_icon_face(self):
        return wait_element(self.dr,'By.XPATH','/html/body/div/ul/li[19]/i')

    # 添加页面：是否可见
    @property
    def module_isvisible(self):
        return wait_element(self.dr, 'By.XPATH', '/html/body/form/div[6]/div/div/div/input')

    # 添加页面：是否可见：是
    @property
    def module_visible(self):
        return wait_element(self.dr, 'By.XPATH', '/html/body/form/div[6]/div/div/dl/dd[1]')

    # 添加页面：是否可见：否
    @property
    def module_visible_no(self):
        return wait_element(self.dr,'By.XPATH','/html/body/form/div[6]/div/div/dl/dd[2]')

    # 添加页面：是否公开
    @property
    def module_ispublic(self):
        return wait_element(self.dr, 'By.XPATH', '/html/body/form/div[7]/div/div/div/input')

    # 添加页面：是否公开：是
    @property
    def module_public(self):
        return wait_element(self.dr, 'By.XPATH', '/html/body/form/div[7]/div/div/dl/dd[1]')

    # 添加页面：是否公开：否
    @property
    def module_public_no(self):
        return wait_element(self.dr, 'By.XPATH', '/html/body/form/div[6]/div/div/dl/dd[2]')

    #添加页面：选择目标
    @property
    def module_target(self):
        return wait_element(self.dr,'By.CSS_SELECTOR','input[value="本窗口"]')

    #添加页面：点击本窗口
    @property
    def module_target_window(self):
        return wait_element(self.dr,'By.XPATH','/html/body/form/div[8]/div/div/dl/dd[1]')

    #添加页面：点击新窗口
    @property
    def module_target_window_new(self):
        return wait_element(self.dr,'By.XPATH','/html/body/form/div[8]/div/div/dl/dd[2]')

    # 添加页面：选择是否校验url
    @property
    def module_alert_url(self):
        return wait_element(self.dr, 'By.CSS_SELECTOR', 'input[value="否"]')

    # 添加页面：选择是否校验url
    @property
    def module_alert_url_no(self):
        return wait_element(self.dr, 'By.XPATH', '/html/body/form/div[9]/div/div/dl/dd[1]')

    # 添加页面：选择是否校验url
    @property
    def module_alert_url_yes(self):
        return wait_element(self.dr, 'By.XPATH', '/html/body/form/div[9]/div/div/dl/dd[2]')

    #添加页面：确定按钮
    @property
    def submit(self):
        return wait_element(self.dr,'By.CSS_SELECTOR',"a[class='layui-layer-btn0']")

    #提示toast
    @property
    def toast_info(self):
        return wait_element(self.dr,"By.CLASS_NAME","layui-layer-content",timeout=15)

    #模块资源树结构
    @property
    def tree_model(self):
        return wait_element(self.dr,'By.ID',"tree_2_span")

    #查询输入字段
    @property
    def search_name(self):
        return wait_element(self.dr, "By.NAME","moduleName")

    #查询按钮
    @property
    def btn_search(self):
        return wait_element(self.dr,'By.ID','LAY-app-search')

    #重置按钮
    @property
    def reset(self):
        return wait_element(self.dr,"By.CSS_SELECTOR","button[type='reset']")

    def tree_custom(self,value):
        title = "a[title='"+value+"']"
        return wait_element(self.dr, 'By.CSS_SELECTOR', title)

    #添加模块
    def add_module(self,modulename, modulesort,parentmodule=None,isvisible='可见',ispublic='公开',target='本窗口',alert_url='否',module_url=None):
        dr = self.dr
        dr.switch_to.frame(Module(dr).iframe_sw[1])
        sleep(1)
        # 点击模块添加按钮
        Module(dr).button_add.click()
        sleep(1)
        dr.switch_to.frame(Module(dr).iframe_d)
        sleep(1)
        print("点击添加按钮")
        if parentmodule!=None:
            # 点击父模块
            Module(dr).parent_module.click()
            sleep(1)
            dr.switch_to.frame(Module(dr).iframe_d)
            sleep(1)
            # 选择父模块
            if Module(dr).tree_name(moduleName=parentmodule)  != False:
                Module(dr).tree_name(moduleName=parentmodule).click()
                sleep(1)
            else:
                raise ("没有找到父模块")
            # 点击确认按钮
            dr.switch_to.parent_frame()
            sleep(1)
            Module(dr).confirm_button.click()
            # sleep(1)
            # dr.switch_to.parent_frame()
            sleep(1)
        # 输入模块名称
        Module(dr).module_name.send_keys(modulename)
        sleep(1)
        # 输入模块地址
        if module_url!=None:
            Module(dr).module_url.send_keys(module_url)
        sleep(1)
        # 输入模块序号
        Module(dr).module_sort.send_keys(modulesort)
        sleep(1)
        #点击模块图标
        Module(dr).module_icon.click()
        sleep(1)
        dr.switch_to.frame(Module(dr).iframe_d1)
        sleep(1)
        Module(dr).module_icon_Hot.click()
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        Module(dr).module_isvisible.click()
        sleep(1)
        if isvisible=='可见':
            Module(dr).module_visible.click()
            sleep(1)
        else:
            Module(dr).module_visible_no.click()
            sleep(1)
        Module(dr).module_ispublic.click()
        sleep(1)
        if ispublic == '公开':
             Module(dr).module_public.click()
             sleep(1)
        else:
            Module(dr).module_public_no.click()
            sleep(1)
        Module(dr).module_target.click()
        sleep(1)
        if target =='本窗口':
            Module(dr).module_target_window.click()
            sleep(1)
        else:
            Module(dr).module_target_window_new.click()
            sleep(1)
        Module(dr).module_alert_url.click()
        sleep(1)
        if alert_url=='否':
            Module(dr).module_alert_url_no.click()
            sleep(1)
        else:
            Module(dr).module_alert_url_yes.click()
            sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        Module(dr).confirm_button.click()
        sleep(1)
        print("点击确定按钮")

    #编辑模块
    def edit_module(self,modulename, modulesort,parentmodule=None,isvisible='可见',ispublic='公开',target='本窗口',alert_url='否',module_url=None):
        dr = self.dr
        dr.switch_to.frame(Module(dr).iframe_d)
        if parentmodule!=None:
            # 点击父模块
            Module(dr).parent_module.click()
            sleep(1)
            dr.switch_to.frame(Module(dr).iframe_d)
            sleep(1)
            # 选择父模块
            if Module(dr).tree_name(moduleName=parentmodule) != False:
                Module(dr).tree_name(moduleName=parentmodule).click()
                sleep(1)
            else:
                raise ("没有找到父模块")
            dr.switch_to.parent_frame()
            sleep(1)
            # 点击确认按钮
            Module(dr).confirm_button.click()
            print("选择父模块")
        sleep(1)
        # 输入模块名称
        Module(dr).module_name.clear()
        sleep(1)
        Module(dr).module_name.send_keys(modulename)
        sleep(1)
        # 输入模块地址
        if module_url!=None:
            Module(dr).module_url.clear()
            sleep(1)
            Module(dr).module_url.send_keys(module_url)
            sleep(1)
        # 输入模块序号
        Module(dr).module_sort.clear()
        sleep(1)
        Module(dr).module_sort.send_keys(modulesort)
        sleep(1)
        #点击模块图标
        Module(dr).module_icon.click()
        sleep(1)
        dr.switch_to.frame(Module(dr).iframe_d1)
        sleep(1)
        Module(dr).module_icon_face.click()
        sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        Module(dr).module_isvisible.click()
        sleep(1)
        if isvisible=='可见':
            Module(dr).module_visible.click()
            sleep(1)
        else:
            Module(dr).module_visible_no.click()
            sleep(1)
        Module(dr).module_ispublic.click()
        sleep(1)
        if ispublic == '公开':
            Module(dr).module_public.click()
            sleep(1)
        else:
            Module(dr).module_public_no.click()
            sleep(1)
        Module(dr).module_target.click()
        sleep(1)
        if target == '本窗口':
            Module(dr).module_target_window.click()
            sleep(1)
        else:
            Module(dr).module_target_window_new.click()
            sleep(1)
        Module(dr).module_alert_url.click()
        sleep(1)
        if alert_url == '否':
            Module(dr).module_alert_url_no.click()
            sleep(1)
        else:
            Module(dr).module_alert_url_yes.click()
            sleep(1)
        dr.switch_to.parent_frame()
        sleep(1)
        Module(dr).confirm_button.click()
        sleep(1)
        print("点击确定按钮")

    def operation(self, modulename, ope):
        # self.dr.switch_to.frame(Department(self.dr).iframe_sw[1])
        x = 1
        if ope == "编辑":
            j = 1
        elif ope == "删除":
            j = 2
        else:
            raise ("ope输入错误")
        for i in range(300):
            xpath = "/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/tr["+str(x)+"]/td[2]/div"
            # print(xpath)
            tr = wait_element(self.dr, "By.XPATH", xpath)
            if tr == False:
                print("未检查到名称为" + modulename + "的模块")
                break
            else:
                if tr.get_attribute('textContent') == modulename:
                    xpath="/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/tr["+str(x)+"]/td[7]/div/a["+str(j)+"]"
                    btn = wait_element(self.dr, "By.XPATH", xpath)
                    return btn
                else:
                    x = x + 1

