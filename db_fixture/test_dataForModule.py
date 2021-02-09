from db_fixture.mysql_db import DB
import time
import os
from configparser import ConfigParser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
conf = ConfigParser()
conf.read(os.path.join(BASE_DIR, 'cfginfo.ini'), encoding='utf-8')
conf.sections()
parentmodule1 = conf.get('MODULE', 'parentmodule1')
parentmodule2 = conf.get('MODULE', 'parentmodule2')
modulename_public = conf.get('MODULE', 'modulename_public')
modulename_visible = conf.get('MODULE', 'modulename_visible')
department1 = conf.get('MODULE', 'deptname')
user = conf.get('MODULE', 'userid')
user1 = conf.get('ROLE', 'user1')
tid = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
tid1 = time.strftime('%m%d%H%M%S',time.localtime(time.time()))
tid2 = time.strftime('%d%H%M%S',time.localtime(time.time()))
tid3 = time.strftime('%H%M%S',time.localtime(time.time()))
tid4 = time.strftime('%M%S',time.localtime(time.time()))
tid5 = time.strftime(time.strftime('%Y%m%d%S',time.localtime(time.time())))
#create data
datas = {
    #模块管理表
    'module':[
        {'id ': tid, 'is_public': '1', 'is_visible': '1', 'module_code':'M011',  'module_name':parentmodule1, 'del_flag': 0},
        {'id ': tid1, 'is_public': '1', 'is_visible': '1', 'module_code': 'M012', 'module_name':parentmodule2,'del_flag': 0},
        {'id ': tid2, 'is_public': '0', 'is_visible': '1', 'module_code': 'M013', 'module_name':modulename_public,'del_flag': 0,'sort_sq': 1},
        {'id ': tid3, 'is_public': '1', 'is_visible': '0', 'module_code': 'M014', 'module_name':modulename_visible,'del_flag': 0,'sort_sq': 1}
    ],
    #部门表
    'department':[
        {'id ': tid4, 'dept_name': department1, 'dept_code': 'D009', 'sort': 1, 'del_flag': 0}
    ],
    #用户表
    'users':[
        {'id':tid5,'password':'9C0DB863D780C6D990B65FCA29CDD5BA','dept_id':tid4,'user_id':user,'name':"测试",'last_change_pwd_time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))},

    ],
}
# 删除数据条件
keys = {
    'users':{'key':'name','value':'测试%'},

    'department':{'key':'dept_name','value':'M测试%'},
    'module':{'key':'module_name','value':'测试%'},
}

# insert table datas
def init_data():
    db=DB()
    for table,data in datas.items():
        key = keys[table]['key']
        value = keys[table]['value']
        db.clear(table,key,value)
        for d in data:
            db.insert(table,d)
    db.close()

# delete table datas
def delete_data():
    db=DB()
    for table,data in datas.items():
        key = keys[table]['key']
        value = keys[table]['value']
        db.clear(table,key,value)
    db.close()

if __name__=='__main__':

    init_data()