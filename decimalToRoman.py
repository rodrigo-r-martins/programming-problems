

def intToRoman(number):
    num_in_roman = ''
    numbers = [1, 4, 5, 9, 10, 40, 50, 90,
               100, 400, 500, 900, 1000]
    symbols = ["I", "IV", "V", "IX", "X", "XL",
               "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    while number:
        div = number // numbers[i]
        number %= numbers[i]

        while div:
            num_in_roman += symbols[i]
            div -= 1
        i -= 1

    return num_in_roman


print(intToRoman(3549))
