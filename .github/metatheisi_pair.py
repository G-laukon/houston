def words_pair():
    '''找出换位对单词，使用异位构词字典'''

    words_sld = words_same_letters()   # 调用异位构词字典函数
    
    for x in words_sld:       
        for y in words_sld[x]:
            for z in words_sld[x]:
                n = 0
                for j,k in zip(y,z):                   
                    if j != k:
                        n = n + 1                  
                if n == 2:          # n可以泛化为实参
                    print (y,z)


def words_same_letters():
    words_sld = dict()
    fin = open('words.txt')
    t = dict()
    s = dict()
    
    for word in fin:
        t[word.strip()] = tuple(sorted(word.strip()))   #单词的字母生序排列生成元组储存为值
        
    fin.close()
    
    for k in t:      # k: key 
        if t[k] in s:
            s[t[k]].append(k)   # 合并相同键的值
        s.setdefault(t[k],[k]) # 转换字典 t 的键和映射
        
    for m in s:
        if len(s[m])> 1:        # 剔除没有异形词的项
            words_sld.setdefault(m,s[m]) # for 语句内好像不能删除字典项，只能生成新的字典

    return words_sld
