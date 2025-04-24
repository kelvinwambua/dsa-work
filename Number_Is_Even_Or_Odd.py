number1 = 21
number2 = 22
def number_is_even_or_odd(num):
    if num %2 == 0:
        return "even"
    else:
        return "odd"

print("The number is",number_is_even_or_odd(number1))
print("The number is",number_is_even_or_odd(number2))