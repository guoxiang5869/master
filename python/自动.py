#!/usr/bin/python
#coding:utf-8
'''
date:9/2/17 18:03 PM
author:lockey
email:lockey@123.com
desc:python自动化安装用户指定版本的python环境
'''
#导入Python的系统编程操作模块
import os

#导入用来处理Python运行时配置以及资源，与前当程序之外的系统环境交互的模块
import sys

#判断当前用户是否是root用户
if os.getuid() == 0:
    pass
else:
    print 'Not under root mode, please switch user!'
    sys.exit(1)

#获取用户输入的python安装版本
version = raw_input('Please input wanted python version(2.7/3.6)')

#如果嫌官网下载速度太慢可以指定python3.6.2的链接地址为本人上传资源地址
#根据用户输入的python版本选择源码包下载地址
if version == '2.7':
    url = 'https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz'
elif version == '3.6':
    url = 'https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz'
else:
    print 'Please input given version number(2.7/3.5)'
    sys.exit(1)

#拼接源码包下载地址并执行下载命令
cmd = 'wget ' + url
res = os.system(cmd)
if res != 0 :
    print 'Failed to download python source package, please inspect your network!'
    sys.exit(1)

if version == '2.7':
    package_version = 'Python-2.7.13'
else:
    package_version = 'Python-3.6.2'

#解压下载的源码包
cmd = 'tar xf ' + package_version + '.tgz'
res = os.system(cmd)

#如果解压失败则删除下载的源码包并且提示用户重新执行脚本
if res != 0:
   os.system('rm ' + package_version + '.tgz')
   print 'Please reexcute the script to install python'
   sys.exit(1)

#解压成功则进入解压后的源码目录中依次执行配置、编译、安装过程
cmd = 'cd ' + package_version + ' && ./configure --prefix=/usr/local/python && make && make install'

res = os.system(cmd)

#安装失败则提示用户安装失败了，让用户检查环境依赖
if res != 0:
   print 'Failed to install python, please inspect dependencies for python install!'
   sys.exit(1)