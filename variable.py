# coding=utf-8

from BasePage import wait_element
from time import sleep

#公共方法
#1 登陆模块  samp：variable.login(dr)
def login(dr,username,password,checkKey):
    print("输入用户名"+username)
    wait_element(dr, 'By.ID', 'userId').clear()
    wait_element(dr,'By.ID','userId').send_keys(username)
    sleep(1)
    print("输入密码"+password)
    wait_element(dr, 'By.ID', 'pwd').clear()
    wait_element(dr, 'By.ID', 'pwd').send_keys(password)
    sleep(1)
    print("输入验证码"+checkKey)
    wait_element(dr, 'By.ID', 'captcha').clear()
    wait_element(dr, 'By.ID', 'captcha').send_keys(checkKey)
    sleep(1)
    print("点击登陆按钮")
    wait_element(dr, 'By.CLASS_NAME', 'btn').click()
    sleep(5)

#获取页面表格数据，返回二维数组
def get_table(dr):
    table=[]
    x = 1
    j = 2
    print("开始获取表格中的数据")
    for i in range(300):  #列表中最多显示300条数据
        xpath = "/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/"+"tr["+str(x)+"]/"+"td["+str(j)+"]/div"
        if wait_element(dr,"By.XPATH",xpath) != False:
            table_char=[]
            for i in range(10):
                tr = wait_element(dr, "By.XPATH", xpath)
                if tr == False:
                    table.append(table_char)
                    break
                else:
                    text = tr.get_attribute('textContent')
                    table_char.append(text)
                    j = j+1
                    xpath = "/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/" + "tr[" + str(
                        x) + "]/" + "td[" + str(j) + "]/div"
            x = x + 1
            j = 2
        else:
            break
    return table

def check_modules(dr,parent,child=None):
    if child == None:
        return wait_element(dr,"By.CSS_SELECTOR",attribute="a[lay-tips='"+parent+"']")
    elif child !=None:
        wait_element(dr,"By.CSS_SELECTOR",attribute="a[lay-tips='"+parent+"']").click()
        sleep(1)
        return wait_element(dr, 'By.LINK_TEXT', attribute=u"%s"%(child))
    else:
        raise ("请正确填写入参")













