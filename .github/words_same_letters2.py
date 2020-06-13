def words_same_letters():
'''效率更高异位构词'''
    fin = open('words.txt')
    t = dict()
    s = dict()
    words_sld = dict()
    for word in fin:
        t[word.strip()] = tuple(sorted(word.strip()))
        
    fin.close()
    
    for key in t:       
        if t[key] in s:
            s[t[key]].append(key)
        s.setdefault(t[key],[key])

    for m in s:
        if len(s[m])> 1:
            words_sld.setdefault(m,s[m])
           
    return words_sld