def words_same_letters():
    '''异位构词'''
    fin = open('words.txt')
    t = dict()
    words_sld = dict()
    w = []
    for word in fin:
        t[word.strip()] = tuple(sorted(word.strip()))
        
    fin.close()

    for x in t:
        w = [x]
        for y in t:
            if t[x] == t[y] and x !=y :
                w = w + [y]
                words_sld[t[x]] = w
        w = []
            
    print(words_sld)
