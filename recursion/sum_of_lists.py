def sum_lists(L):
    '''Write a Python program to sum recursion lists using recursion'''

    r = 0
    
    # iterate through the list
    for a in L:
        # if its a number, add to result
        if isinstance(a, (int, float)):
            r += a
        # if its a sublist, call the function on that sublist
        else:
            r += sum_lists(a)

    return r


if __name__ == "__main__":
    L = [1, 2, [3, 4], [5, [6, 7]], 8]
    result = sum_lists(L)
    print(f"The sum of the list is: {result}")
