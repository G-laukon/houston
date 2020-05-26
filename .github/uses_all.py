def uses_all(word,letters) :
    n = len(word)
    m = 0
    x = letters[m]
    for x in letters:
        if word.find(x) > -1:
            return True
        if m == n-1:
            return word.find(x) > -1  
        m = m + 1
