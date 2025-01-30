from stack import Stack

def matches(peek, s):
    '''Checks if opening string (at the top of stack) matches the closing string met throughout the loop'''
    open_ = '([{'
    close_ = ')]}'
    return open_.index(peek) == close_.index(s)

def test_balance(str_):
    '''Checks if the string is balanced (parentheses)'''
    stack = Stack()
    matches_dict = {
        '(':')',
        '[':']',
        '{':'}'
    }


    for s in str_:
        # push the opening parentheses into stack
        if s in matches_dict.keys():
            stack.push(s)
        # if met a closing one and the stack isnt empty (otherwise false immediately), then make sure that the last pushed into stack matches that closing one we see one else false
        elif s in matches_dict.values() and not stack.is_empty():
            if matches(stack.peek(), s):
                stack.pop()
            else:
                return False
        # if its neither opener nor closer just false 
        else:
            return False
        
    return stack.is_empty()


# all tests have passed
print(test_balance("((()))"))  # expected True
print(test_balance("((()()))"))  # expected True
print(test_balance("(()"))  # expected False
print(test_balance("[]"))  # expected True
print(test_balance("[[]]"))  # expected True
print(test_balance("[[[]]]"))  # expected True
print(test_balance("[[[]]]]"))  # expected False
print(test_balance("["))  # expected False
print(test_balance("]"))  # expected False
print(test_balance("{}"))  # expected True
print(test_balance("{{}}"))  # expected True
print(test_balance("{{{}}}"))  # expected True
print(test_balance("{{{}}}}"))  # expected False
print(test_balance("{"))  # expected False
print(test_balance("{[()]}"))  # expected True
print(test_balance("{[(])}"))  # expected False
print(test_balance("{[()()]}"))  # expected True
print(test_balance("{[(()])}"))  # expected False
print(test_balance("{[()]}[]"))  # expected True
print(test_balance("{[()]}[{}]"))  # expected True
print(test_balance("{[()]}[{}]("))  # expected False
print(test_balance("{[()]}[{}])"))  # expected False      