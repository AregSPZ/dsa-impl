def int_to_str(n, base):
    '''Convert an integer of base from 2 to 16 to a string using recursion (no while and for loops)'''
    digits = '0123456789ABCDEF'
    # base case of recursion
    # we gradually get closer to this with each recursive call
    if n < base:
        # convert to coresponding digit string
        return digits[n]
    else:
        return int_to_str(n // base, base) + digits[n % base]


if __name__ == '__main__':
    print(int_to_str(10, 2))