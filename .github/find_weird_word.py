def find_weird_word():
    fin = open('words.txt')   
    for word_raw in fin:
        word = word_raw.strip()
        n = len(word)
        while n>5:
            if word[n-1] == word[n-2] and word[n-3] == word[n-4] and word[n-5] == word[n-6]:
                print(word)
                break           
            n = n-1
    fin.close()
