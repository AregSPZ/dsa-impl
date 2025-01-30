from stack import Stack

def rev_string(my_str):
    stack = Stack()
    # push strings into stack
    for s in my_str: 
        stack.push(s)
    output = ''
    # output the pushed strings in reverse order with pop()
    while not stack.is_empty():
        output += stack.pop()

    return output


print(rev_string('Areg'))

