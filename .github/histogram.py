def histogram(word):
    '''直方图'''
    wo = dict()
    for w in word:
        wo[w]= wo.get(w,0)+ 1                         
    return wo
