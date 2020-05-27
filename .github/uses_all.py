def uses_all(word,letters) :
    n = len(letters)
    for x in letters:   
        if word.find(x) > -1:
            n = n - 1
        if n == 0:
            return True
