'''
Given an array A[] containing N elements, create a new array that will store at index i the number of elements that are smaller than A[i] and coming after index i in A[] array.

Example:
Input = 6 4 2 1 5
Output = 4 2 1 0 0
'''

array = list(map(int, input('> ').split(' ')))
new_array = []

for i in range(len(array)):
    counter = 0
    for j in range(i+1, len(array)):
        if array[i] > array[j]:
            counter += 1
    new_array.append(counter)

for x in new_array:
   print(x, end=' ')
