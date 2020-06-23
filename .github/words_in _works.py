def make_split():
    import string
    s = input('filename:')
    fin = open(str(s))
    d = dict()
    for line in fin:
        line = line.lower()
        for i in line:
            if i in string.punctuation:
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

if __name__ == '__main__':
    words_dict = make_split()
    print_words(words_dict)
