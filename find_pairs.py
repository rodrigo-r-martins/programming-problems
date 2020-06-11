'''
- FIND PAIRS WITH PYTHON

Define a function that finds pair values of a list that when we sum those values result in the given target value

Example: 
list = [1, 3, 5, 6, 8, 20, 11]
target = 8
It should return (3, 5)
'''


def find_pairs(values, target):
    pairs = []
    while values:
        number = values.pop()
        # Subtraction between target and number popped from list
        difference = target - number
        if difference in values:          # If the result is in the list we have a pair
            pairs.append((difference, number))
    return pairs


print(find_pairs([14, 3, 5, 7, 8, 10, 1, 2], 12))
print(find_pairs([14, 13, 6, 7, 8, 10, 1, 2], 3))


# *** If we know there's only one pair that correspond to target, we can use the following function.
'''
def find_pairs(values, target):
   for value in values:
      for val in values:
         if value+val == target:
            return f'{value} and {val}'  
   return 'no valid pairs' 
'''
