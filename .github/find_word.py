def find(word,letter,index):
    count = 0
    while True :
        while index == len(word):
            if count == 0:
                return 'Nope'
            else:
                return count,'Done'
        if word[index] == letter:
            count = count + 1
            print(index)     

        index = index + 1
  








        
    
    
