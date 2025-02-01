def preprocess_string(str_):
    '''Remove spaces, caps and notation to also be able to evaluate phrases'''
    chars_to_remove = [' ', ',', ';', '.', '!', '?', '"', "'"]
    for char in chars_to_remove:
        str_ = str_.replace(char, '')
    return str_.lower()

def palindrome_check(str_):
    '''  
    Check if the string is palindrome using recursion
    The function has limitations and will work unexpectedly with unusual strings instead of human expressions
    e.g. ',....,'  
    '''
    
    str_ = preprocess_string(str_)

    # edge case: empty string
    if len(str_) == 0:
        return True
    
    # base case. if the length of the string is 1 or 2, make the trivial check
    elif len(str_) <= 2:
        return str_[0] == str_[-1]
    
    # like in deque, we remove the front and the rear of the string until there's only 1 or 2 letters left and the base case activates
    else:
        # making sure that the front and the rear match before making the recursive call
        return palindrome_check(str_[1:-1]) if str_[0] == str_[-1] else False 

if __name__ == '__main__':
    for str_ in ['kayak', 'aibohphobia', 'Live not on evil', 'Go hang a salami; I"m a lasagna hog', 'Reviled did I live, said I, as evil I did deliver', 'Able was I ere I saw Elba', 'vorrr', 'x', 'radar', 'hello', '', 'hannah', 'madam i"m adam']:
        print(palindrome_check(str_))