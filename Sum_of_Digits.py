number = 2323232323  # The number whose digits we want to sum

def sum_of_digits(num):
   total = 0  # Initialize the sum to zero
   while num > 0:  # Continue until no digits remain
       total += num % 10  # Get the last digit and add it to total
       num = num // 10  # Remove the last digit from the number
   return total

print("The sum of the digits is", sum_of_digits(number))  # Display the result