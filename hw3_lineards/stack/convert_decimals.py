from stack import Stack

def convert(n, base):
    '''Convert decimal number to different base (returns a string)'''

    digits = '0123456789ABCDEF'
    stack = Stack()
    output = ''

    while n > 0:
        # get the remainder of the current number
        rem = n % base
        # push the corresponding digit of the remainder into stack (if rem is from 0 to 9 then just it, if 10-16 then A-F)
        stack.push(digits[rem])
        n = n // base
    print(stack._items)
    # reverse the stack's contents (the thing is that the first remainder is at the end and so on)
    while not stack.is_empty():
        output += stack.pop()

    return output

print(convert(42, 16))
print(convert(233, 8))
print(convert(25, 8))
print(convert(256, 16))
print(convert(26, 26))