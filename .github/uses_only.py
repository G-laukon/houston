def uses_only(word,letters) :
    for x in word:
        if letters.find(x) < 0:
            return None
    return True
