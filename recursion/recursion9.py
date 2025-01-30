def geometric_sum(b, q, n):
    '''Write a Python program to calculate the geometric sum up to n terms'''

    if n == 1:
        return b
    
    else:
        return b + geometric_sum(b*q, q, n-1)