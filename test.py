#coding:utf-8
import pymssql as mssql_module
conn=mssql_module.connect(host='210.45.212.119',user='sa',password='admin@txsys2013',database='CPDB')
#conn=mysql_module.connect(host='172.24.9.35',port=1433,user='sa',password='123456',database='CPDB')
cur=conn.cursor()
cur.execute('select * from [dbo].[USERINFO]')
#print(cur.fetchall())
r=cur.fetchone()
i=1
f=open('userdata.txt','a')#区分a模式和w模式
while r:
	id,name,pwd,content=r
	print(name)
	f.write(name.encode('gb2312'))
	f.write(',')
	f.write(pwd.encode('gb2312'))
	f.write('\n')
	r=cur.fetchone()
	i+=1
f.close()
cur.close()
conn.close()
