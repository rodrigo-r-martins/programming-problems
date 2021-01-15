# Return the fibonacci number at the position given by user
def fib_number_at(pos):
    list_numbers = []
    for i in range(pos+1):
        if i == 0 or i == 1:
            list_numbers.append(i)
        else:
            list_numbers.append(list_numbers[i-2]+list_numbers[i-1])
    return list_numbers[pos]


# It returns a list of n fibonacci numbers
def fib_num_list(n):
    list_numbers = []
    for i in range(n):
        if i == 0 or i == 1:
            list_numbers.append(i)
        else:
            list_numbers.append(list_numbers[i-2]+list_numbers[i-1])
    return list_numbers


# It creates a fibonacci numbers generator
def fib_sequence(n):
    n1 = 0
    n2 = 1
    for i in range(n):
        yield n1
        temp = n1
        n1 = n2
        n2 = temp + n2


print(fib_number_at(10))
print(fib_num_list(10))
for x in fib_sequence(20):
    print(x)
