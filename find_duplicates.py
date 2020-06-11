some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []
for char in some_list:
    if some_list.count(char) > 1:
        if char not in duplicates:
            duplicates.append(char)

print(duplicates)