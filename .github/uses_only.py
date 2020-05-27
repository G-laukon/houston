def uses_only(word,letters) :
    n = len(word)
    for x in word:
        if letters.find(x) >= 0:
            n = n - 1
        if n == 0:
            return True
