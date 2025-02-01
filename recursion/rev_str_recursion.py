def reverse_string(str_):
    '''Reverse a string using recursion'''
    # base case 
    if len(str_) == 1:
        return str_
    else:
    # the recursive calls will collect the letters of the string one by one. at the end only one string will remain (the first one) which will be returned by base case
        return str_[-1] + reverse_string(str_[:-1])
    
 
if __name__ == '__main__':
    print(reverse_string('puyfyja'))