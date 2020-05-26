def uses_only(word,letters) :
    n = len(word)
    m = 0
    x = word[m]
    for x in word:
        if letters.find(x) < 0:
            return False
        if m == n-1:
            return letters.find(x) > -1  
        m = m + 1
