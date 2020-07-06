import string
import random

def anylise(filename,n):    
    fin = open(str(filename))
    s = []
    hist = {}
    val = {}
    for line in fin:
        if line.startswith('*** START OF THIS'):
            break       
    for line in fin:
        if line.startswith('*** END OF THIS'):
            break       
        t = process_line(line)
        u = s + t 
        while len(u) > n:
            key = tuple(u[:n])
            val[u[n]] = val.setdefault(u[n],0)+ 1
            hist[key] = val
            u = u[1:]
        s = u               
    fin.close()
    return hist

def process_line(line):
    for i in line:
        for i in string.punctuation:
            while i in line:
                line = line.replace(i,' ')                   
    line = line.lower()
    line = line.split()      
    return line

def main():
    filename = input('Filename:')
    n = int(input('Prefix words number:'))
    d = anylise(filename,n)
    print(d)

    
if __name__ == '__main__':
    main()
