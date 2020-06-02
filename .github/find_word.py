def find(word,letter):
    '''给定单词与字母，计算字母出现频率与位置'''
    count = 0
    index = 0
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
  








        
    
    
