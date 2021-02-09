from db_fixture.mysql_db import DB
from configparser import ConfigParser
import time
import os

# conf = ConfigParser()
# conf.read("../cfginfo.ini", encoding="utf-8")
# conf.sections()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
conf = ConfigParser()
conf.read(os.path.join(BASE_DIR, 'cfginfo.ini'), encoding='utf-8')
conf.sections()
user1 = conf.get('ROLE', 'user1')
password = '9C0DB863D780C6D990B65FCA29CDD5BA'
rolename3 = conf.get('ROLE', 'rolename3')
rolename4 = conf.get('ROLE', 'rolename4')
rolename5 = conf.get('ROLE', 'rolename5')
rolenamedel = conf.get('ROLE', 'rolenamedel')
departname = conf.get('ROLE', 'departnamesql')
tid = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
tid1 = time.strftime('%m%d%H%M%S',time.localtime(time.time()))
tid2 = time.strftime('%d%H%M%S',time.localtime(time.time()))
datas = {
    # 部门管理表
    'department': [
        {'id ': tid1, 'dept_name': departname, 'dept_code': 'D001', 'sort': 1, 'del_flag': 0},
    ],

    'users':[
        {"id":tid,'password':password,'dept_id':tid1,'name':user1,'user_id':user1,'last_change_pwd_time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))}
    ],
    'role': [
        {'id ': tid2, 'role_name': rolename3, 'sort': 1, 'del_flag': 0},
    ]
}

keys = {
        'department' : {'key':'dept_name','value':departname},
        'users':{'key':"name",'value':user1},
        'role':{'key':'role_name','value':"%"+rolenamedel+"%"},
}

datas1 = {

    'role': [
        {'id ': int(tid2)+1, 'role_name': rolename4, 'sort': 1, 'del_flag': 0},
{'id ': int(tid2)+2, 'role_name': rolename5, 'sort': 1, 'del_flag': 0}
    ]
}

def clear_data():
    db=DB()
    for table,data in datas.items():
        key = keys[table]['key']
        value = keys[table]['value']
        db.clear(table,key,value)
    db.close()
def insert_data():
    db =DB()
    for table,data in datas.items():
        key = keys[table]['key']
        value = keys[table]['value']
        for d in data:
            db.insert(table,d)
    db.close()
#添加两条角色数据测试批量删除
def insert_data2():
    db =DB()
    for table,data in datas1.items():
        key = keys[table]['key']
        value = keys[table]['value']
        for d in data:
            db.insert(table,d)
    db.close()



def init_data():
    clear_data()
    insert_data()

