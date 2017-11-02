#coding:utf-8
import pymssql as mssql_module
conn=mssql_module.connect(host='210.45.212.119',user='sa',password='admin@txsys2013',database='CPDB')
#conn=mysql_module.connect(host='172.24.9.35',port=1433,user='sa',password='123456',database='CPDB')
cur=conn.cursor()
cur.execute('select * from [dbo].[USERINFO]')
#print(cur.fetchall())
r=cur.fetchone()
i=1
while r:
	id,name,passwod,content=r
	print(name)
	r=cur.fetchone()
	i+=1
cur.close()
conn.close()
