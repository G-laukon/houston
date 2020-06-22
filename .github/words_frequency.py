def make_split(title):
    import string
    fin = open(title)
    for line in fin:
        for i in line:
            if i in string.punctuation:
                line = line.replace(i,' ')           
                res = line.split()
                d = make_dict(res)
    fin.close()
    return d
    
    
    
def make_dict(words):
    d = dict()
    for word in words:
        d[word] = d.setdefault(word,0)+ 1
    return d

def print_words(words_dict):
    num = make_dict(words)
    print('the number of words_used in the works:',len(num))
    res = []
    for i in words_dict:
        res.append(words_dict[i],i)

    res.sort(reverse = True )

    for n,word in res[0:20]:
        print(word,n)
    
   

if __name__ == '__main__':
    words_dict = make_split(title)
    print_words(words_dict)
