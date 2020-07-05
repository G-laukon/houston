import string
import random

def anylise(filename):    
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

def process_line(line):
    for i in line:
        for i in string.punctuation:
            while i in line:
                line = line.replace(i,' ')
                    
    line = line.lower()
    line = line.split():      
    return line


def prefix_words(line,n)
    s = []
    t = line[:]
    u = s + t
    memo = {}
    val = {}
    while len(u)> n:
        key = tuple(u[:n])
        val = val.setdefault(u[n],0)+ 1
        memo[key] = val
        u = u[1:]

    s = u

    return memo
