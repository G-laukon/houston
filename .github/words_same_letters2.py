words_sld = dict()
def words_same_letters():
'''效率更高的异位构词
   words_sld:异位构词字典
'''
    fin = open('words.txt')
    t = dict()
    s = dict()
    
    for word in fin:
        t[word.strip()] = tuple(sorted(word.strip()))   #单词的字母升序排列，生成元组
        
    fin.close()
    
    for k in t:      # k: key 
        if t[k] in s:
            s[t[k]].append(k)   # 合并相同键的值
        s.setdefault(t[k],[k]) # 转换字典 t 的键和映射
        
    for m in s:
        if len(s[m])> 1:        # 剔除没有异形词的项
            words_sld.setdefault(m,s[m]) # for 语句内好像不能删除字典项，只能生成新的字典

    return words_sld
