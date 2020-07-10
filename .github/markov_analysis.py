import string
import random

def skip_gutenberg_header(filename,n=2):    
    fin = open(str(filename))
    s = []
    hist = {}  
   
    for line in fin:
        skip_header(line)
        if line.startswith('*** END OF THIS'):
            break       
        
        u = s + process_line(line)
        s = words_map(hist,u,n)

               
    fin.close()
    return hist

def skip_header(line):
    if line.startswith('*** START OF THIS'):
        breaks

def process_line(line):
    for i in line:
        for i in string.punctuation:
            while i in line:
                line = line.replace(i,' ')                   
#    line = line.lower()
    line = line.split()
    
    return line


def words_map(hist,u,n):

    while len(u) > n:
        key = tuple(u[:n]) 
        if key in hist:
            hist[key].append(u[n])
        if key not in hist:
            hist[key] = [u[n]]
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


def make_issue(d,m = 20):
    word = random.choice(list(d))
    issue = word
    for i in range(m):
        w = random_word(d,word)
        issue = issue + (w[-1],)
        word = w
    return issue


def random_word(d,w):
    l = random.choice(d[w])
    word = (w[1:])+(l,)
    return word


def main():
    filename = input('Filename:')
    
    n = input('Prefix words number :')
    if n == '':
        d = skip_gutenberg_header(filename)
    else:
        n = int(n)
        d = skip_gutenberg_header(filename,n)
    
        
    m =input('Used prefix number :')
    if m == '':
        issue = make_issue(d)    
    else:
        m = int(m)
        issue = make_issue(d,m)
    file = ''
    for i in issue:
        file = file +i+' '
    print(file)
    
if __name__ == '__main__':
    main()  
