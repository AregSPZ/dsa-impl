def a_power_b(a, b):
    '''Write a Python program to calculate the value of 'a' to the power of 'b' using recursion'''

    if b == 1:
        return a 
    
    else:
        return a * a_power_b(a, b-1)
    

if __name__ == '__main__':
    print(a_power_b(3,4))