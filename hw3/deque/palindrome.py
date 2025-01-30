from deque import Deque

def palindrome_check(str_):
    # handling palindromes with spaces
    str_ = str_.replace(' ', '')
    if len(str_) == 1:
        return True
    else:
        deque = Deque()
        for s in str_:
            deque.add_front(s)
        while deque.size() > 1:
            rear = deque.remove_rear()
            front = deque.remove_front()
            if rear != front:
                return False
        return True
    

for _ in [palindrome_check('radar'),
palindrome_check('madam'),
palindrome_check('r'),
palindrome_check('rgb'),
palindrome_check('Areg'),
palindrome_check('I PREFER PI')]:
    
    print(_)
    