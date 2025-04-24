number = 2323232323
def sum_of_digits(num):
    total =0
    while num> 0:
        total += num % 10
        num = num//10
    return total
print("The sum of the digits is", sum_of_digits(number))
        