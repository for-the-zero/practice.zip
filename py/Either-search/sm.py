import threading
import sh
import time

all_e = {'google':'NO', 'bing':'NO', 'qwant':'NO'}
s = ''

# 将9个线程分别补充
def google():
	global s
	global all_e
	get = sh.get_url('https://google.com/search?q={}'.format(s))
	if get == 'error':
		get = sh.get_url('https://search.aust.cf/search?q={}'.format(s))
		if get == 'error':
			del all_e['google']
		else:
			all_e['google'] = get[0]('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[*]/div/div[1]/div/a/@href')
	else:
		all_e['google'] = get[0]('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[*]/div/div[1]/div/a/@href')
def bing():
	global s
	global all_e
	get = sh.get_url('https://cn.bing.com/search?q={}'.format(s))
	if get == 'error':
		del all_e['bing']
	else:
		all_e['bing'] = get[0]('//*[@id="b_results"]/li[*]/div[1]/h2/a/@href')
def qwant():
	global s
	global all_e
	get = sh.get_url('https://www.qwant.com/?q={}'.format(s))
	if get == 'error':
		del all_e['qwant']
	else:
		all_e['qwant'] = get[0]('//*[@id="root"]/div[2]/div[3]/div[1]/div[2]/section/div[1]/div/div/div[*]/div[2]/div[1]/a/@href')


def get_all(q):
	global s
	global all_e
	s = q
	
	t1 = threading.Thread(target=google)
	t1.run()
	t2 = threading.Thread(target=bing)
	t2.run()
	t3 = threading.Thread(target=qwant)
	t3.run()
	while True:
		j = 0
		for i in all_e:
			if all_e[i] != 'NO':
				j += 1
		if j == len(all_e):
			break
	return all_e
