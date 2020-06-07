def rotate_word(word,n) :
    '''凯撒密码'''
    word_new = ''
    for letter in word:
        letter_new = chr(ord(letter) + n)
        word_new = word_new + letter_new
    return word_new
