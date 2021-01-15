def highest_even(li):
    evens = []
    for number in li:
        if number % 2 == 0:
            evens.append(number)
    return max(evens)


print(highest_even([11, 2, 3, 4, 8, 10]))
