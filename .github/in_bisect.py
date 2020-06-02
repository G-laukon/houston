def in_bisect(words,word):
    words_copy =[]+ words
    words_copy.sort()   
    if words != words_copy:
        return None
    m = int(len(words_copy))
    n = m
    while m > 0 :   
        if len(words_copy)%2 == 1:
            while words_copy[0] >= word:
                return n-m
            while words_copy[-1] < word:
                return n
            del words_copy[-1]
            n = n - 1
        m = int(len(words_copy)/2)
        if words_copy[m] > word:
            words_copy = words_copy[:m]
            n = n - m
        else:
            words_copy = words_copy[m:]
