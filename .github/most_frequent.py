def most_frequent(text):
'''给定字符串检测字符出现频率，降序打印'''
    t = dict()
    n = []
    for letter in text.lower():
        t[letter] = t.setdefault(letter,0) + 1

    for x in t.items() :   
        n = n + list([x[::-1]])

    n.sort(reverse= True)
    for y in n:
        print(y)
