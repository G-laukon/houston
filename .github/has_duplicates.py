def has_duplicates(t):
    '''检测列表重复元素'''
    for x in t:
        t_copy = t + []
        t_copy.remove(x)
        for y in t_copy :
            if x == y:
                return True
                
