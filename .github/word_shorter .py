def make_word_dict():
    words_d = dict()
    fin = open('words.txt')
    
    for word in fin:
        if word not in words_d:
            words_d[(word.strip())]= None        
    fin.close()
    for i in ['a','b','']:
        words_d[i] = None

    return words_d
    
memo = {}
memo[''] = ['']


def reducible_word(word,words_d):
    if word in memo:
        return memo[word]
    
    res = []
    for child in children(word,words_d):
        if reducible_word(word,words_d):
            res.append(child)
    memo[word] = res
    return res


def children(word,words_d):
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in words_d:
            res.append(child)
    return res

def all_reducilble(words_d):
    res = []
    for word in words_d:
        t = reducible_word(word,words_d)
        if t != []:
            res.append(word)
        return res

def print_trail(word):
    if len(word)== 0:
        return
    print(word,end ='')
    t = reducible_word(word,words_d)
    print_trail(t[0])

def print_longest_words(words_d):
    words = all_reducilble(words_d)
    t= []
    for word in words:
        t.append(len(word),word)
    t.sort(reverse = True)

    for n, word in t[0:5]:
        print_trail(word)
        print('\n')

if __name__ == '__main__':
    words_d = make_word_dict()
    print_longest_words(words_d)


'''def word_shorter():
    words_d = dict()
    know = dict()
    fin = open('words.txt')
    for word in fin:
        n = len(word)
        if word not in words_d:
            words_d[(word.strip())]= 1
            know[(n,word.strip())]= [1]
    fin.close()
    
    for w in sorted(know, reverse = True):
        word = list(w[1])
        t = sorted(know, reverse = True)
        if know[w] == [1]:
            while len(word)>0:
                
                for i in word:
                    res = word
                    res.remove(i)
                    wd = make_word(res)
                    
                    if wd in words_d:
                        if wd not in know[w]:
                        
                            know[w] = know[w]+ [wd]
                        
                        word = res
                                      

        if know[w][-1] == 'a' or know[w][-1] == 'i':
            return w,know[w]




            
def make_word(word_list):
    word = ''
    for i in word_list:
        word = word + i
    return word'''
