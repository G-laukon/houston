ack = {'0,0':1}
def ackermann(m,n):
    '''阿克曼函数字典方法'''
    x =str(m)+ ','+ str(n)
    if x in ack:
        return ack[x]
    if m == 0:
        res= n+ 1
        ack[x] == res
        return res
    while m> 0 and n == 0:
        res = ackermann(m-1, 1)
        ack[x]= res      
        return res
    while m> 0 and n > 0:
        res = ackermann(m-1, ackermann(m, n- 1))
        ack[x]= res
        return res
