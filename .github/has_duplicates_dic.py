def has_duplicates(t):
    '''字典方法检测列表重复对象'''
    t_dic = dict()
    for x in t:
        t_dic[x]= t_dic.get(x,0)+ 1
        if t_dic[x] > 1:
            return True,x
