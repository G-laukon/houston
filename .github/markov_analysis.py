
import string
import random



def markov_analysis(filename,n):    
    fin = open(str(filename))
    s = []
    hist = {}
    
    for line in fin:
        if line.startswith('*** START OF THIS'):
            break
        
    for line in fin:
        if line.startswith('*** END OF THIS'):
            break       
        t = process_line(line)
        u = s + t
    
        def words_map(hist,u,n)

        s = u
               
    fin.close()
    return hist

def process_line(line):
#    for i in line:
#        for i in string.punctuation:
#            while i in line:
#                line = line.replace(i,' ')                   
#    line = line.lower()
    line = line.split()      
    return line


def words_map(hist,u,n=2)
    while len(u) > n:
        key = tuple(u[:n]) 
        if key in hist:
            hist[key].append(u[n]:1)
        if key not in hist:
            hist[key] = [u[n]:1]
        u = u[1:]
    return u


'''
def words_map(u,n)
        while len(u) > n:
            key = tuple(u[:n]) 
            if key in hist:
                hist[key][u[n]] = hist[key].setdefault(u[n],0)+ 1
            if key not in hist:
                hist[key] = {u[n]:1}
            u = u[1:]
'''


def random_word(d,w):
    l = random.choice(d[w])
    w = w[1] + l
    return w

def make_issue(d,m = 20):
    issue = ''
    word = random.choice(list(d))
    for i in range(m):
        issue = issue + word
        word = random_word(d,w)
    return issue
    

def main():
    filename = input('Filename:')
    n = int(input('Prefix words number:'))
    d = anylise(filename,n)

    
if __name__ == '__main__':
    main()
