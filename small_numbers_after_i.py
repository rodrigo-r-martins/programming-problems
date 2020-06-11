'''
Given an array A[] containing N elements, create a new array that will store at index i the number of elements that are smaller than A[i] and coming after index i in A[] array.

Example:
Input = 6 4 2 1 5
Output = 4 2 1 0 0
'''

array = list(map(int, input('> ').split(' ')))
new_array = []

for i in range(len(array)):
    nums = []
    for j in range(i+1, len(array)):
        if array[i] > array[j]:
            nums.append(array[j])
    new_array.append(nums)

for x in new_array:
    print(len(x), end=' ')
