def sum_digits(n):
    '''Write a Python program to get the sum of a non-negative integer using recursion'''
    str_n = str(n)
    if len(str_n) == 1:
        return n
    else:
        return int(str_n[0]) + sum_digits(int(str_n[1:]))
    
if __name__ == "__main__":
    print(sum_digits(45))  # Example usage