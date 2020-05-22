import math
def estimate_pi():
    k = 0
    m = 0
    while True:
        m_1 = total(k)
        m = m + m_1
        k = k + 1 
        if m_1 < 1e-15:
            print(abs(1/((2*math.sqrt(2)/9801)*m) - math.pi))
            print(1/((2*math.sqrt(2)/9801)*m))
            return 'Done'
            

def total(k):
    a = factorial(4*k)*(1103+26390*k)
    b = math.pow(factorial(k),4)*math.pow(396,4*k)
    c = a/b
    return c
   
def factorial(k):
    if k==0:
        return 1
    else:
        recurse = factorial(k-1)
        result = k*recurse
        return result
    

    
    
    
    
