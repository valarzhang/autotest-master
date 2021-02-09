#coding=utf-8
#
import pymysql.cursors
import os
import configparser as cparser

# ======== Reading db_config.ini setting ===========

base_dir=str(os.path.dirname(os.path.dirname(__file__)))
base_dir=base_dir.replace('\\','/')
file_path=base_dir+'/cfginfo.ini'

cf=cparser.ConfigParser()

cf.read(file_path,encoding='utf-8')
host=cf.get('mysqlconf','host')
port=cf.get('mysqlconf','port')
db = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")

# ======== MySql base operating ===================

class DB:
    def __init__(self):
        try:
            #connect to database
            self.connection=pymysql.connect(host=host,
                                            user=user,
                                            password=password,
                                            port = int(port),
                                            db=db,
                                            charset='utf8mb4',
                                            cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print('Mysql Error %d:%s' %(e.args[0], e.args[1]))

    #clear table data
    def clear(self,table_name,key,value):
        #real_sql="truncate table " + table_name + ";"
        real_sql='delete from '+table_name+' where %s like "%s";'%(key,value)
        # real_sql='delete from information_content where title="title_a";'
        with self.connection.cursor() as cursor:
            cursor.execute('SET FOREIGN_KEY_CHECKS=0;')
            cursor.execute(real_sql)
        self.connection.commit()

    #insert sql statement
    def insert(self,table_name,table_data):
        for key in table_data:
            table_data[key]="'"+str(table_data[key])+"'"
        key=",".join(table_data.keys())
        value=",".join(table_data.values())
        real_sql="INSERT INTO "+table_name+" (" + key + ") VALUES (" + value+ ")"
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()

    def select(self,real_sql):
        try:
            #connect to database
            self.connection=pymysql.connect(host=host,
                                            user=user,
                                            password=password,
                                            port = int(port),
                                            db=db,
                                            charset='utf8mb4',
                                            cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print('Mysql Error %d:%s' %(e.args[0], e.args[1]))
        with self.connection.cursor() as cursor:
            return cursor.execute(real_sql)

    # close database
    def close(self):
        self.connection.close()

if __name__ == '__main__':
    db = DB()
    # table_name = "test_table"
    table_name = "department"
    data = {'id':'123', 'dept_name':'测试部门2020', 'dept_code':'D001', 'del_flag': 0}
    db.insert(table_name,data)
    db.close()
