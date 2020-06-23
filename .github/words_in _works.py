def make_split():
    import string
    s = input('filename:')
    fin = open(str(s))
    d = dict()
    for line in fin:
        line = line.lower()
        for i in line:
            for i in string.punctuation:
                while i in line:
                
                    line = line.replace(i,' ')

                
        words = line.split()
                
                
        for word in words:
            d[word] = d.setdefault(word,0)+ 1
    fin.close()
    return d



def print_words(words_dict):
    num = len(words_dict)
    print('the number of words used in the works:',num)
    print('\n')
    res = []
    for i in words_dict:
        res.append((words_dict[i],i))

    res.sort(reverse = True )

    for n,word in res[0:20]:
        print(word,n)

def print_no_words(words_dict):
    d = words_dic()
    print('\n')
    print('Words not in dictionary')
    print('\n')
    for i in words_dict:
        if i not in d:
            print(i)
    

def words_dic():  
    words_d = dict()
    fin = open('words.txt')
    for word in fin:
        if word not in words_d:
            words_d[word.strip()]= 1
    fin.close()
    return words_d

if __name__ == '__main__':
    words_dict = make_split()
    print_words(words_dict)
    print_no_words(words_dict)
