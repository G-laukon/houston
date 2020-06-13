def bingo(n):
'''可组合出最多单词的n字母,使用words_same_letter()生成的异位构词字典'''

    for key in words_sld.sort(reverse = True):
        if len(key) == n:
            return words_sld[key],key
