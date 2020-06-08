def rotate_word_dic():
'''字典方法查找反转词对'''
    fin = open('words.txt')
    d = dict()
    for word in fin:
        d.setdefault(word.strip(),None)

    for x in d:
        if x[::-1] in d and x != x[::-1]:
            print (x,x[::-1])
