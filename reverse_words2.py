def reverse_words():
'''反转词对，使用二叉树搜索函数‘’‘
    fin = open('words.txt')
    words_list =[]
    for i in fin:
        words_list.append(i.strip())
    fin.close()
    length_list = int(len(words_list))

    while length_list > 1:
        in_bisect(words_list[1:],words_list[0])
        words_list = words_list[1:]
        length_list = int(len(words_list))    
            
def in_bisect(words,word):
    words_copy =[]+ words
    word_reverse = word[::-1]
    m = int(len(words_copy))
    while m > 1:
        if len(words_copy)%2 == 1:
            if words_copy[-1]== word_reverse:
                print (word,word_reverse)
                return
            del words_copy[-1]
        m = int(len(words_copy)/2)
        if words_copy[m] > word_reverse:
            words_copy = words_copy[:m]
        else:
            words_copy = words_copy[m:]        
    if words_copy[0] == word_reverse:
        print (word,word_reverse)
