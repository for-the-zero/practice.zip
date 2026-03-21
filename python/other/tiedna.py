# 导入模块
import random
import msvcrt

# 列表
c_v = [
	'测量',
	'溶解',
	'混合',
	'加热',
	'过滤',
	'观察',
	'燃烧',
	'爆炸',
	'砸坏',
	'立即发生爆炸',
	'放热',
	'点燃',
	'通电',
	'产生白色沉淀',
	'发出尖锐爆鸣声',
	'搅拌',
	'旋转',
	'进行核裂变',
	'进行核聚变',
	'火星四射',
	'被吃掉',
	'吃掉了',
	'删除',
	'制取',
	'拿出',
	'喷射',
	'损坏',
	'在氧气中燃烧',
	'煮熟',
]
c_n = [
	'普通中学',
	'化学实验室',
	'集气瓶',
	'氢气',
	'氧气',
	'酒精灯',
	'浓硫酸',
	'钠欧欸齿(NaOH)',
	'水',
	'手',
	'眼睛',
	'化学老师',
	'自己',
	'汽油',
	'酒精',
	'试管',
	'集气瓶',
	'天平',
	'实验桌',
	'火星',
	'分液漏斗',
	'水槽',
	'白磷',
	'生石灰',
	'滴管',
]

print('Tiedna，让你的化学DNA打结的玩意')
print('1键=v+n 2键=把+n+v+n 3键=使+n+v 4键=用+n+把+n+v')
print('==========')
while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()
        key = key.decode('utf-8')
        if key == '1':
            print(random.choice(c_v) + random.choice(c_n))
        elif key == '2':
            print('把' + random.choice(c_n) + random.choice(c_v) + random.choice(c_n))
        elif key == '3':
            print('使' + random.choice(c_n) + random.choice(c_v))
        elif key == '4':
            print('用' + random.choice(c_n) + '把' + random.choice(c_n) + random.choice(c_v))
        elif key == 'q':
            print('退出')
            break
        else:
            pass
        # 等待松开按键
        while msvcrt.kbhit():
            ...



