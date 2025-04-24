initialNumber = 5
def factorial_using_loop(num):
    total = num
    for i in range(1,num):   
        total = total * i
    return total
print("The factorial is",factorial_using_loop(initialNumber))
