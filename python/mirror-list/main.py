import sh

import re


def get():
	xpath = sh.get_url('https://www.library.ac.cn/')[0]
	google = xpath('/html/body/div/div[2]/div/div/table/tbody/tr[1]/td[2]/a/@href')
	google_scholar = xpath('/html/body/div/div[2]/div/div/table/tbody/tr[2]/td[2]/a/@href')
	wiki = xpath('/html/body/div/div[2]/div/div/table/tbody/tr[3]/td[2]/a/@href')
	other = xpath('/html/body/div/div[2]/div/div/table/tbody/tr[4]/td[2]/a/@href')
	github = xpath('/html/body/div/div[2]/div/div/table/tbody/tr[5]/td[2]/a/@href')

	# 将other中所有链接分类为包含a0或ddg0或.php的
	archive = [] # a0
	ddg = [] # ddg0
	free = [] # .php
	for i in other:
		if re.search(r'a0', i):
			archive.append(i)
		elif re.search(r'ddg0', i):
			ddg.append(i)
		elif re.search(r'\.php', i):
			free.append(i)

	return {
		'google': google,
		'google_scholar': google_scholar,
		'wiki': wiki,
		'github': github,
		'archive': archive,
		'ddg': ddg,
		'free': free
	}

if __name__ == '__main__':
	wl = get()

	#rich 表格 填色（一种网站一个随机颜色）
	from rich.console import Console
	from rich.table import Table
	from rich.style import Style
	#打印表格
	console = Console()
	table = Table(show_header=True, header_style=Style(color='white'))
	table.add_column('网站', style=Style(color='yellow'))
	table.add_column('链接', style=Style(color='blue'))
	for i in wl['google']:
		table.add_row('google', i)
	for i in wl['google_scholar']:
		table.add_row('google_scholar', i)
	for i in wl['wiki']:
		table.add_row('wiki', i)
	for i in wl['github']:
		table.add_row('github', i)
	for i in wl['archive']:
		table.add_row('archive', i)
	for i in wl['ddg']:
		table.add_row('ddg', i)
	for i in wl['free']:
		table.add_row('free', i)
	console.print(table)
	