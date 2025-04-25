initialNumber = 5  # Define the number for which we want to calculate factorial

def factorial_using_loop(num):
   total = 1  # Initialize total to 1 
   for i in range(1, num + 1):  # Loop through numbers 1 to num inclusive
       total = total * i  # Multiply the running total by the current number
   return total

print("The factorial of", initialNumber, "is", factorial_using_loop(initialNumber))  # Calculate and print 5!