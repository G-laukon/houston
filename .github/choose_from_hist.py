def choose_from_hist():
    word = input('word:')
    d = histogram(word)
    t = []
    for i in d:
        t = t + [i]*(d[i])
    print(t)
    import random
    s = random.choice(t)
    print(s)

    


def histogram(word):
    wo = dict()
    for w in word:
        wo[w]= wo.get(w,0)+ 1                         
    return wo

if __name__ == '__main__':
    choose_from_hist()
