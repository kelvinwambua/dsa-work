initialNumber = 5
total =0
def factorial_using_recursion(num):
    if num == 1 or num == 0:
        return 1
    else:
        return  num * factorial_using_recursion(num-1)
print("The factorial is", factorial_using_recursion(initialNumber))