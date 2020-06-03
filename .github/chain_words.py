def chain_words():
'''检索连锁词'''
    fin = open('words_test.txt')
    words_list =[]
    for i in fin:
        words_list.append(i.strip())
    fin.close()
    for word in words_list:
        letter= list(word)
        x= letter[::2]
        y= letter[1::2]
        if in_bisect(words_list,x) == True and in_bisect(words_list,y)==True            
            print(word,''join(x),''join(y))
        
       
            
def in_bisect(words,word):
    words_copy =[]+ words
    m = int(len(words_copy))
    while m > 1:
        if len(words_copy)%2 == 1:
            if words_copy[-1]== word:
                return True
            del words_copy[-1]
        m = int(len(words_copy)/2)
        if words_copy[m] > word:
            words_copy = words_copy[:m]
        else:
            words_copy = words_copy[m:]        
    if words_copy[0] == word:
        return True
