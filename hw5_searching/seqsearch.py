def sequential_search(data, item):
    '''Check if the item exists in sequential data'''
    i = 0
    while i < len(data):
        ith_item = data[i]
        if ith_item == item:
            return True
        i += 1
    return False


if __name__ == '__main__':
    # Example function executions
    data_list = [10, 20, 30, 40, 50]

    print(sequential_search(data_list, 30))  # Output: True
    print(sequential_search(data_list, 60))  # Output: False
    print(sequential_search([], 10))         # Output: False
    print(sequential_search(data_list, 10))  # Output: True
    print(sequential_search(data_list, 50))  # Output: True