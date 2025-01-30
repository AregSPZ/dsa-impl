def sum_series1(n):
    '''Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0) using recursion '''

    if n <= 0:
        return 0
    
    else:
        return n + sum_series1(n-2)
    
if __name__ == "__main__":
    n = 10
    print("The sum of the series is:", sum_series1(n))