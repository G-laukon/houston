def is_palindrome(word):
        n = len(word)
        while n<2:
            return True
        if word[0] != word[-1]:
            return False
        if word[0] == word[n-1]:
            return is_palindrome(word[1:-1])
