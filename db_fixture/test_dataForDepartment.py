from db_fixture.mysql_db import DB
from configparser import ConfigParser
import os
import time
#create data
# conf = ConfigParser()
# conf.read("../cfginfo.ini", encoding="utf-8")
# conf.sections()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
conf = ConfigParser()
conf.read(os.path.join(BASE_DIR, 'cfginfo.ini'), encoding='utf-8')
conf.sections()
department1 = conf.get('DEPARTMENT', 'department1')
department2 = conf.get('DEPARTMENT', 'department2')
sort98 = conf.get('DEPARTMENT', 'sort98')
sort99 = conf.get('DEPARTMENT', 'sort99')
scandepart = conf.get('DEPARTMENT', 'scandepart')
tid = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
tid1 = time.strftime('%m%d%H%M%S',time.localtime(time.time()))
tid2 = time.strftime('%d%H%M%S',time.localtime(time.time()))
datas = {
    #部门管理表
    'department':[
        {'id': tid, 'dept_name': department1, 'dept_code': 'D0011', 'sort': sort98, 'del_flag': 0},
        {'id': tid1, 'dept_name': department2, 'dept_code': 'D0021', 'sort': sort99, 'del_flag': 0},
    ],
}
keys = {
    'department' : {'key':'dept_name','value':scandepart+"%"},
}



# insert table datas
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

def init_data():
    clear_data()
    insert_data()

