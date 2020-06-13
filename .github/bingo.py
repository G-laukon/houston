'''给定字母数n，输出异位构词最多的字母组合和单词序列'''

def bingo(n):
    res =[]
    words_sld = words_same_letters()
    for k in words_sld :
        if k not in res and len(k)== n:
            res = [[len(words_sld[k]),k,words_sld[k]]] + res
    
    res.sort(reverse = True)

    for i in res:                       # 最多构词数相同时，全部打印
        if i[0] == res[0][0]:
            print (i[1],i[2],i[0])



def words_same_letters():
    words_sld = dict()
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
