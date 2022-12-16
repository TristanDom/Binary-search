import random
import time

# Binary search algoritm.
# Code make by Orta Domínguez Tristán Eduardo.

# .:****** Native search ******:. 
"""Naitive search:
scan entire list and ask if its equal to the target 
if yes, return the index.
if not, return -1."""

def native_search(l, target):
    l = [2, 5, 6]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# .:****** Binary search ******:. 
# Binary search uses divide and conquer.
# We will leverage the fact that our list is SORTED.

def binary_search(l, target, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if high < low:
        return -1 
    mindpoint = (low + high) // 2
    if l[mindpoint] == target:
        return mindpoint
    elif target < l[mindpoint]:
        return binary_search(l, target, low, mindpoint - 1)
    else:
        return binary_search(l, target, mindpoint + 1, high)


if __name__== '__main__':
    # Test between native search and binary search.
    # l = [1, 3, 5, 10, 12]
    # target = 10
    # print(native_search(l, target))
    # print(binary_search(l, target))

# .:****** Make list of 10000 random elements ******:. 
    lenght = 10000
    sorted_list = set()
    while len(sorted_list) < lenght:
        sorted_list.add(random.randint(-3*lenght, 3*lenght))
    sorted_list = sorted(list(sorted_list))

# .:****** Time of native search ******:. 
    start = time.time()
    for target in sorted_list:
        native_search(sorted_list, target)
    end = time.time()
    print("Native search time: ", (end - start) / lenght, "seconds")

# .:****** Time of binary search ******:. 
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start) / lenght, "seconds")