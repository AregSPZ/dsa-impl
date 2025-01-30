def harmonic_series_sum(n):
    '''Write a Python program to calculate the sum of harmonic series upto n terms'''

    if n == 1:
        return 1
    
    else:
        return (1/n) + harmonic_series_sum(n-1)
    

