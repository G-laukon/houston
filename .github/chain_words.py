def chain_words():
    fin = open('words.txt')
    words_list =[]
    for i in fin:
        words_list.append(i.strip())
    fin.close()
    for word in words_list:       
        if len(word) > 1:
            x= word[::2]
            y= word[1::2]
            if in_bisect(words_list,x) == True and in_bisect(words_list,y) == True:
                print(word,x,y)
     
            
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
