import sqlite3
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')
con = sqlite3.connect('db.sqlite3')
cur = con.cursor()
pattern='([a-zA-Z-]+(?:\.[\w-]+)*@%s)'%sys.argv[1]
#re_mail = re.compile(r"([a-zA-Z-]+(?:\.[\w-]+)*@[\w-]+(?:\.[a-zA-Z-]+)+)")
re_mail = re.compile(pattern)
def sqlemployer():
    select_sql = "select * from graber_employee"
    cur.execute(select_sql)
    date_set = cur.fetchall()
    for row in date_set:
        print(row)
    con.commit()
def deletesql():
    delete_sql='delete from graber_employee'
    cur.execute(delete_sql)
    con.commit()
def insertsql(email,name):
    insert_sql='insert into graber_employee(email,name) values(\'%s\',\'%s\')'%(email,name)
    cur.execute(insert_sql)
    con.commit()
if __name__ =='__main__':
    f=open('usr.txt','r')
    sqlemployer()
    deletesql()
    lines=f.readlines()
    for line in lines:
        email = re_mail.findall(line)
        #if email== null
        if len(email):
            rname=line.lstrip(email[0])
            name=rname.strip()
            print email[0],name
            insertsql(email[0], name)
    f.close()
    cur.close()
    con.close()