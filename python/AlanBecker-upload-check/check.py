import sh
import re
import cn2an
import json

import wx
#初始化wxpython
app = wx.App()

#请求
get = sh.get_url('https://api.bilibili.com/x/space/arc/search?mid=519253600')[1]
#get将json转字典
get = json.loads(get)
#获取到的数据筛选出['data']里['list']里['vlist']中每一项中的['title']
title = [i['title'] for i in get['data']['list']['vlist']]
#去空格
for i in range(len(title)):
	title[i] = re.sub(' ','',title[i])
#筛选出含有‘火柴人VS我的世界系列第’的项目
title = [i for i in title if re.search(r'火柴人VS我的世界系列第', i)]
title = title[0]
#将title去除‘火柴人 VS 我的世界系列 第’
title = re.sub(r'火柴人VS我的世界系列第', '', title)
#将title去除‘集 ’及其后面的内容
title = re.sub(r'集.*', '', title)
#将title转为数字
title = cn2an.cn2an(title, "smart")
#读写模式打开文件last.txt
f = open('last.txt', 'r+')
last = int(f.read())
if last <= title-1:
	#title覆盖文件所有内容
	f.seek(0)
	f.truncate()
	f.write(str(title))
	#弹窗提示
	wx.MessageBox('Alan更新了！', '好消息', wx.OK | wx.ICON_INFORMATION)
f.close()
