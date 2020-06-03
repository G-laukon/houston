def reverse_words():
    ‘’‘反转词对,for语句循环遍历’‘’
    fin = open('words.txt')
    words_list =[]
    for i in fin:
        words_list.append(i.strip())
    for x in words_list:
        for y in words_list:
            if list(y) == list(x)[::-1]:
                print(x,y)
    fin.close()

