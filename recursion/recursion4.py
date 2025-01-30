def factorial_rec(n):
    '''Write a Python program to get the factorial of a non-negative integer using recursion'''
    if n == 1:
        return 1
    else:
        return n * factorial_rec(n-1)
    
if __name__ == "__main__":
    num = 6
    print(f"The factorial of {num} is {factorial_rec(num)}")