initialNumber = 5  # Define the number for which we want to calculate factorial
def factorial_using_recursion(num):
   if num == 1 or num == 0:  # Base case: factorial of 0 or 1 is 1
       return 1
   else:  # Recursive case: n! = n × (n-1)!
       return num * factorial_using_recursion(num-1)  # Call the function recursively with num-1
print("The factorial is", factorial_using_recursion(initialNumber))  # Calculate and print the factorial