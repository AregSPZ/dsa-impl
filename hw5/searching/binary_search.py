def binary_search(data, item):
    '''Assume the data is sorted'''
    
    left, right = 0, len(data) - 1
    
    while left <= right:
        middle = (left + right) // 2
        
        if data[middle] == item:
            return True
        elif data[middle] < item:
            left = middle + 1
        else:
            right = middle - 1
    
    return False


def binary_search_rec(data, item, l, r):

    middle = (l + r) // 2

    # base cases 
    if l > r:
        return False
    if data[middle] == item:
        return True
    
    elif data[middle] > item:
        return binary_search_rec(data, item, l, middle-1)
    
    else:
        return binary_search_rec(data, item, middle+1, r)



if __name__ == '__main__':  

    data_even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    data_odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    item_to_find = 10

    print(f"Iterative binary search for {item_to_find} in even data: {binary_search(data_even, item_to_find)}")
    print(f"Iterative binary search for {item_to_find} in odd data: {binary_search(data_odd, item_to_find)}")
    
    print(f"Recursive binary search for {item_to_find} in even data: {binary_search_rec(data_even, item_to_find, 0, len(data_even) - 1)}")
    print(f"Recursive binary search for {item_to_find} in odd data: {binary_search_rec(data_odd, item_to_find, 0, len(data_odd) - 1)}")