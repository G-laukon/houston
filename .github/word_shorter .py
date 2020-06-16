def word_shorter():
    words_d = dict()
    know = dict()
    fin = open('words.txt')
    for word in fin:
        n = len(word)
        if word not in words_d:
            words_d[(word.strip())]= 1
            know[(n,word.strip())]= [1]
    fin.close()
    
    for w in sorted(know, reverse = True):
        word = list(w[1])
        t = sorted(know, reverse = True)
        if know[w] == [1]:
            while len(word)>0:
                
                for i in word:
                    res = word
                    res.remove(i)
                    wd = make_word(res)
                    
                    if wd in words_d:
                        if wd not in know[w]:
                        
                            know[w] = know[w]+ [wd]
                        
                        word = res
                                      

        if know[w][-1] == 'a' or know[w][-1] == 'i':
            return w,know[w]




            
def make_word(word_list):
    word = ''
    for i in word_list:
        word = word + i
    return word
