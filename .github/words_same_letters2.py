words_sld = dict()
def words_same_letters():
'''效率更高的异位构词
   words_sld:异位构词字典
'''
    fin = open('words.txt')
    t = dict()
    s = dict()
    
    for word in fin:
        t[word.strip()] = tuple(sorted(word.strip()))
        
    fin.close()
    
    for k in t:       
        if t[k] in s:
            s[t[k]].append(k)
        s.setdefault(t[k],[k])
        
    for m in s:
        if len(s[m])> 1:
            words_sld.setdefault(m,s[m])
           
    return words_sld
