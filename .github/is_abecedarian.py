def is_abecedarian(word):
    n = len(word)
    for letter in word:
        letter= word[n-1]
        while n - 1 == 0:
            return True
        if letter >= word[n-2]:
            n = n - 1
