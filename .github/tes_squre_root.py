def tes_squre_root():
    import math
    print('a    mysqrt(a)        math.sqrt(a)   diff                 ')
    print('-    ---------        ------------   ----                 ')
    a = 1.0
    while True:
        mysqrt(a)
        l = mysqrt(a)
        m = math.sqrt(a)
        n = abs(l - m)
        print(a,'',l,' ',m,' ',n)
        if a == 9:       
            break
        a = a + 1.0
    

def mysqrt(a):
    x = a
    while True:     
        y = (x + a/x) / 2
        if abs(x-y) < 0.0000000001:
            return y
           
        x = y
        
