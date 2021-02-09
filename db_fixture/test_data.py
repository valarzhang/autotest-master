from db_fixture.mysql_db import DB
import time,os
from configparser import ConfigParser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
conf = ConfigParser()
conf.read(os.path.join(BASE_DIR, 'cfginfo.ini'), encoding='utf-8')
conf.sections()
parentdept1 = conf.get('USER','parentdept1')
parentdept2 = conf.get('USER', 'parentdept2')
parentdept3 = conf.get('USER', 'parentdept3')
relate_role = conf.get('USER','relate_role')
relate_role_new = conf.get('USER','relate_role_new')

tid = "0"+time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
tid1 = "1"+time.strftime('%m%d%H%M%S',time.localtime(time.time()))
tid2 = "2"+time.strftime('%d%H%M%S',time.localtime(time.time()))
tid3 = "3"+time.strftime('%d%H%M%S',time.localtime(time.time()))
tid4 = "4"+time.strftime('%d%H%M%S',time.localtime(time.time()))
#create data
datas = {
    #部门管理表
    'department':[
        {'id': tid, 'dept_name': parentdept1, 'dept_code': 'D001', 'sort': 1, 'del_flag': 0},
        {'id': tid1, 'dept_name': parentdept2, 'dept_code': 'D002', 'sort': 1, 'del_flag': 0},
        {'id': tid2, 'dept_name': parentdept3, 'dept_code': 'D003', 'sort': 1, 'del_flag': 0},
    ],
    'role':[
        {'id': tid3, 'role_name':relate_role, 'del_flag': 0},
        {'id': tid4, 'role_name':relate_role_new, 'del_flag': 0}
    ],
    'users':[]
}
datas1 = {
    #部门管理表
    'department':[
        {'id': tid, 'dept_name': parentdept1, 'dept_code': 'D001', 'sort': 1, 'del_flag': 0},
    ],
    'users':[],
    'role':[]
}
# 删除数据条件
keys = {
    'users':{'key':'name','value':'测试用户%'},
    'role':{'key':'role_name','value':'测试角色%'},
    'department':{'key':'dept_name','value':'测试部门%'}
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

# insert table datas
def insert_data1():
    db=DB()
    for table,data in datas1.items():
        key = keys[table]['key']
        value = keys[table]['value']
        db.clear(table,key,value)
        for d in data:
            db.insert(table,d)
    db.close()

def delete_data():
    db=DB()
    for table,data in datas.items():
        key = keys[table]['key']
        value = keys[table]['value']
        db.clear(table,key,value)
    db.close()

if __name__=='__main__':
    init_data()