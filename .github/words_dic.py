words_d = dict()
def words_dic():  
    '''生成字典'''
    fin = open('words.txt')
    for word in fin:
        if word not in words_d:
            words_d[word.strip()]= 1
    fin.close()
