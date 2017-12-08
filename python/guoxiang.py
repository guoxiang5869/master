#/usr/bin/env 
# -*- coding: utf-8 -*-

#输出
#在python2中print是调用并非函数，而python3中归入了函数范畴，因此
#在python3中print的函数的书写格式就变为了print()的格式；
#print '输出单引内的内容','1',2,3+4,50/2,50*0.2,((5+3)-2)*3

#输入
#输入指令，输入到了那里去，首先要创建变量，并给这个变量定义，可
#理解为创建一个空文档，你输入不同的后缀，赋予了他到底是什么格式；
#name = raw_input("shuru：")
#print "hello", name

name = raw_input ('_id: ')
print 'hello: ', name

age = int(raw_input('age: '))#年龄=

if age >= 18:	
	print 'ok'
else:
	age = int(raw_input('age: '))



#import sys
#print(sys.version_info >= (3,3))  #判断系统版本是否大于或等于3.3
#print sys.version_info.major,'.',sys.version_info.minor









