'''
Given an array, write a program to count pairs in the array such that one element of pair divides other.
'''


def divide_pair(arr):
    n = len(arr)
    pairs = []

    for i in range(n):
        for j in range(i+1, n):
            if arr[j] % arr[i] == 0:
                pairs.append((arr[i], arr[j]))
    print(pairs)
    return len(pairs)


arr_1 = [1, 2, 3]
arr_2 = [2, 3, 7, 11, 4, 6, 9]

print(divide_pair(arr_1))
print(divide_pair(arr_2))
