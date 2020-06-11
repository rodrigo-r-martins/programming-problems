'''
Write a function: equilibrium(arr, n), that given a sequence arr[] of size n, returns an equilibrium index (if any) OR -1 if no equilibrium indexes exist.

*** Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
'''


def equilibrium(arr):
    n = len(arr)

    for i in range(n):
        lower_sum = 0
        higher_sum = 0

        for j in range(i):
            lower_sum += arr[j]

        for j in range(i+1, n):
            higher_sum += arr[j]

        if lower_sum == higher_sum:
            return i
    return -1


arr = [5, 6, 3, 8, 1, 2]
print(equilibrium(arr))
