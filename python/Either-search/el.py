
def inone(l1_link,l2_link):
    #将l1_link和l2_link去重
    l1_link = list(set(l1_link))
    l2_link = list(set(l2_link))
    #将l1_link和l2_link用字典存储从1开始的索引
    l1_link_dict = {}
    l2_link_dict = {}
    for i in range(len(l1_link)):
        l1_link_dict[l1_link[i]] = i+1
    for i in range(len(l2_link)):
        l2_link_dict[l2_link[i]] = i+1
    #将l1_link和l2_link的键合并至lf_link一个字典，如果键有重复，则取两个索引的平均值作为索引，否则将索引乘以1.5作为索引
    lf_link = {}
    for i in l1_link:
        if i in l2_link:
            lf_link[i] = (l1_link_dict[i]+l2_link_dict[i])/2
        else:
            lf_link[i] = l1_link_dict[i]*1.5
    for i in l2_link:
        if i in l1_link:
            continue
        else:
            lf_link[i] = l2_link_dict[i]*1.5
    #将lf_link按照索引排序，从小到大，如果有相同则按l1_link_dict中顺序排序，如果l1_link_dict没有相同则按l2_link_dict中顺序排序
    lf_link = sorted(lf_link.items(),key=lambda x:x[1])
    lf_link = [i[0] for i in lf_link]
    return lf_link
