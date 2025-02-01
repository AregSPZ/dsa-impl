def integer_converter(n, base):
    '''Write a Python program to convert an integer to a string in any base using recursion'''
    digits = '0123456789ABCDEF'
    if base > n:
        return digits[n]
    else:
        return integer_converter(n // base, base) + digits[n % base]

if __name__ == "__main__":
    print(integer_converter(10, 2))  # Output should be '1010'
    print(integer_converter(255, 16))  # Output should be 'FF'
    print(integer_converter(100, 8))  # Output should be '144'