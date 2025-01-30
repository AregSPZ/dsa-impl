import random

L = [random.randint(1, 101) for _ in range(20)]

print(L)

L_sorted = sorted(L)

def find_kth_smallest(list, k):
    print(f'\n{k}-th smallest: {list[k-1]}')

find_kth_smallest(L_sorted, 17)