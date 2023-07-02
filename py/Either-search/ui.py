import pywebio.output as o
import pywebio.input as i
import re

def ask():
	q = i.input('搜索什么？')
	o.put_markdown('#### 这个有点久，你要等亿下')
	return q

#[href,[text,text]]
def show(title,list):
	o.put_markdown('''
		{} | search
		:--: | :--:
		'''.format(title))
	# list的项目数
	for j in range(len(list)):
		o.put_markdown('## [{link}]({link})'.format(link=list[j]))
		#用正则表达式识别list[j]中的链接是否含有‘*://github.com/’
		if re.search('.*://github.com/*',list[j]) != None:
			# 将list[j]中的'*://github.com/'替换为'*://hub.nuaa.cf/*'
			mirror_a = re.sub('.*://github.com/*','https://hub.nuaa.cf/',list[j])
			mirror_b = re.sub('.*://github.com/*','https://hub.連接.台灣/',list[j])
			mirror_c = re.sub('.*://github.com/*','https://hub.おうか.tw/',list[j])
			mirror_d = re.sub('.*://github.com/*','https://hub.fastgit.xyz/',list[j])
			o.put_html('''<details>
				<summary>镜像</summary>
				<h3><a href='{a}'>{a}</a>     <a href='{b}'>{b}</a>     <a href='{c}'>{c}</a>     <a href='{d}'>{d}</a></h3>
				</details>'''.format(a=mirror_a,b=mirror_b,c=mirror_c,d=mirror_d))
		if re.search('.*.wikipedia.org/*',list[j]) != None:
			mirror_a = re.sub('.*.wikipedia.org/*','https://www.wikipedia.ahmu.cf/',list[j])
			mirror_b = re.sub('.*.wikipedia.org/*','https://www.wikipedia.iwiki.eu.org/',list[j])
			mirror_c = re.sub('.*.wikipedia.org/*','https://www.wikipedia.ahau.cf/',list[j])
			mirror_d = re.sub('.*.wikipedia.org/*','https://www.wikipedia.iwiki.uk/',list[j])
			mirror_e = re.sub('.*.wikipedia.org/*','https://www.wikipedia.維基.台灣/',list[j])
			o.put_markdown('''
				<details>
				<summary>镜像</summary>
				<h3><a href='{a}'>{a}</a>	 <a href='{b}'>{b}</a>     <a href='{c}'>{c}</a>     <a href='{d}'>{d}</a>     <a href='{e}'>{e}</a></h3>
				</details>'''.format(a=mirror_a,b=mirror_b,c=mirror_c,d=mirror_d,e=mirror_e))
		if re.search('.*.bilibili.com/video/BV*',list[j]) != None or re.search('.*.bilibili.com/s/video/BV*',list[j]) != None:
			bv = list[j]
			#如果bv中含有问号，则去除问号及其后的内容
			bv = re.sub('\?.*','',bv)
			#将bv中video/及前面的东西全部去掉
			bv = re.sub('.*video/','',bv)
			#如果bv最后有斜杠，则去掉
			bv = re.sub('/','',bv)
			o.put_html('''
				<details>
					<summary>预览</summary>
					<iframe src="//player.bilibili.com/player.html?bvid={}&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="820" height="500">></iframe>
				</details>
				'''.format(bv))


