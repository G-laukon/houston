def is_palindrome(word):
    if not isinstance(word, str) or word == '' or word[0]==' ':
        word = input('OOps!Please input a word:\n')
        return is_palindrome(word)
           
    else:
        return word == word[::-1]
