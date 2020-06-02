def reverse_words():
    fin = open('words.txt')
    for x in fin:
        word = list(x.strip())
        word_reverse = word[::-1]
        for y in fin:
            word_chk = list(y.strip())
            if word_chk == word_reverse:
                print(x.strip(),y.strip())
    fin.close()
