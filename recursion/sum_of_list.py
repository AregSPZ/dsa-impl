def rec_sum(L):
    '''Write a Python program to calculate the sum of a list of numbers using recursion'''
    if len(L) == 1:
        return L[0]
    else:
        return L[0] + rec_sum(L[1:])
    

if __name__ == "__main__":
    L = [1, 2, 3, 4, 5]
    print(f"The sum of the list {L} is: {rec_sum(L)}")