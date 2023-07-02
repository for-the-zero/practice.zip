import sm
import ui
import el

import jieba
def cutwords(w):
    cut_list = list(jieba.cut(w,cut_all=False))
    #去除cut_list中的空格
    cut_list = [i for i in cut_list if i != '']
    #将cut_list中的每个元素转成字符串并以空格隔开
    cut_list = ' '.join(cut_list)
    return cut_list

def go():
    q = ui.ask()
    q = cutwords(q)
    all_e = sm.get_all(q)
    j = 0
    for i in all_e:
        if j == 0:
            answer = all_e[i]
        else:
            answer = el.inone(answer,all_e[i])
        j += 1
    ui.show(q,answer)
