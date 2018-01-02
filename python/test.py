#/usr/bin/env 
# -*- coding: utf-8 -*-

#if True:
#	print 'No.1'
#	print 'No.2'
#else:
#	print 'No.3'
#	print 'No.4'

print u'中文测试'#将ASCII编码字符串转为Unicod编
#码输出，Unicod编码已将中文GB2312编码融入，不会乱码；
print '中文测试'#ASCII编码仅支持数字、字母和符号，只有255个转码；

print u'转换测试'.encode('utf-8')

print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')