def is_palindrome_number():
    number_ori = 999999
    while number_ori > 100000:
        number = number_ori
        word = str(number)
        if is_palindrome(word) == True:
            word = str(number-1)
            if is_palindrome(word[1:]) == True:
                word = str(number-2)
                if is_palindrome(word[2:]) == True:
                    print(number_ori,number_ori-1,number_ori-2)
                    
        number_ori=number_ori - 1
                        
def is_palindrome(word):
    return word == word[::-1]
