def uses_all(word,letters) :
    for x in letters:   
        if word.find(x) == -1:
            return None
    return True
