import string
import random

def skip_gutenberg(filename):    
    fin = open(str(filename))
    hist = {}
    d = {}
    for line in fin:
        if line.startswith('*** START OF THIS'):
            break
        
    for line in fin:
        if line.startswith('*** END OF THIS'):
            break       
        hist = process_line(line,hist)
    fin.close()
    d2 = words_dic()
    for i in hist:       
        if i in d2:
            d[i] = hist[i]
    return d
        

def process_line(line,d):
#    line = line.replace('-', ' ')

    for i in line:
        for i in string.punctuation:
            while i in line:
                line = line.replace(i,' ')
    
    for word in line.split():
        word = word.lower()
        
#        word = word.strip(string.punctuation + string.whitespace)
       
        d[word] = d.setdefault(word,0)+ 1
    return d


def words_dic():  
    words_d = dict()
    fin = open('words.txt')
    for word in fin:
        words_d[word.strip()]= 1
    fin.close()
    return words_d


def most_commn(d):
    res = []
    for key,value in d.items():
        res.append((value,key))
    res.sort(reverse = True )
    return res
        

def random_word(d):
    res = []
    n = 0
    d.sort()
    for i in d:
        j = i[0]      
        n = n + j
        res.append(n)      
    ran = random.randint(1,n)
    m = in_bisect(res,ran)
    word = d[m]
    return word
    
    
def in_bisect(d,r):
    res = d[:]
    m = len(res)
    while m > 0 :   
        if len(res)%2 == 1:  #当m为1时，余数也为1
            if res[0] >= r:
                return d.index(res[0])
            del res[0]

        m = int(len(res)/2)  # int函数保证m为整数值
        if res[m-1] >= r:
            res = res[:m]
        else:
            res = res[m:]
         

def print_words(d,m = 10):
    hist = most_commn(d)   
    print('the number of words used in the works:',sum(d.values()))
    for n,word in hist[:m]:
        print(word,n)      
    w = random_word(hist)
    print('the random word with the sequence:',w)


def main():
    filename = input('Filename:')
    d = skip_gutenberg(filename)

    print_words(d)
    
if __name__ == '__main__':
    main()
