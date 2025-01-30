def gcd_rec(a, b):
    '''Write a Python program to find the greatest common divisor (GCD) of two integers using recursion'''
    
    if b == 0:
        return a
    
    else:
        return gcd_rec(b, a % b)