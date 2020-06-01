def in_bisect(words,word):
    words_copy =[]+ words
    words_copy.sort()   
    if words != words_copy:
        return None
    m = int(len(words_copy))
    n = m
    while m > 1 :
        x = len(words_copy)%2
        if x == 0:
            m = int(len(words_copy)/2)
        if x == 1:
            m = int((len(words_copy)+1)/2)
            n = n + 1
        print(m,'s')
        word_m = words_copy[m]
        if word_m > word:
            words_copy = words_copy[:m]
            n = n - m
        else:
            words_copy = words_copy[m:]
            n = n
        print(words_copy)
    if words_copy[0] < word:
        return n
    else:
        return n -1
