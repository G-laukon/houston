def gcd(a,b):
'''最大公约数'''
    if abs(a)<abs(b) :
        a_b = a
        b_a = b
        a = b_a
        b = a_b
        return gcd(abs(a),abs(b))
    else:
        if b == 1:
            return 'No GCD'
        if b == 0:
            return a
        else:
            return gcd(abs(a%b),abs(b))
