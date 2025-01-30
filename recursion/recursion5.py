def fib_rec(n):
    '''Compute nth number of Fibonacci Sequence recursively'''
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)
    
if __name__ == "__main__":
    n = 100
    print('This will take forever.')
    print(f"The {n}th Fibonacci number is: {fib_rec(n)}")