#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import psutil
import os
import sys
import wmi ##
from sympy.physics.optics.gaussopt import FreeSpace
from Cython.Compiler.Errors import message

##获取物理磁盘信息
def get_disk_info():
    tmplist=[]
    c=wmi.WMI()
    for physical_disk in c.Win32_DiskDrive():
        tmpdict={}
        tmpdict["Caption"]=physical_disk.caption
        tmpdict["Size"]=int(physical_disk.Size)/1024/1024/1024 #总容量 单位G
        tmplist.append(tmpdict)
    return tmplist

#获取文件系统信息
def get_fs_info():
    tmplist=[]
    c=wmi.WMI()
    for physical_disk in c.Win32_DiskDrive():
        for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
            for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
                tmpdict={}
                tmpdict["Caption"]=logical_disk.caption #磁盘序号
                tmpdict["DiskTotal"]=int(logical_disk.Size)/1024/1024/1024 #该磁盘总空间
                tmpdict["UseSpace"]=(int(logical_disk.Size)-int(logical_disk.FreeSpace))/1024/1024/1024 #已使用空间
                tmpdict["FreeSpace"]=int(logical_disk.FreeSpace)/1024/1024/1024 #空闲空间
                #使用空间所占比重
                tmpdict["Percent"]=int(100.0*(int(logical_disk.Size)-int(logical_disk.FreeSpace))/int(logical_disk.Size)) 
                tmplist.append(tmpdict)
    return tmplist            
my_sender='m18110861586@163.com' #发件人邮箱账号
my_user='13665511056@163.com' #收件人邮箱账号
def mail():
    ret=True
    isSend=False
    fs=get_fs_info()
    num=len(fs) #磁盘数目
    message=[]
    try:
        for i in range (0,num):
            message.append(str(fs[i]))
            per=fs[i]["Percent"]
            if(per>10):
                isSend=True
        
        msg=MIMEText(str(message),'plain','utf-8')
        msg['From']=formataddr(["dl", my_sender]) #发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["zp", my_user]) #收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="实验室176服务器磁盘空间信息" #邮件主题
        
        server=smtplib.SMTP("smtp.163.com",25) #收件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,"dl3135031") #发件人邮箱账号、密码
        if(isSend==True):
            server.sendmail(my_sender,[my_user,],msg.as_string()) #发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit() #关闭连接
    except Exception:
        ret=False
    return ret


    

# disk=get_disk_info()
# print(disk)

ret=mail()
print(ret)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        