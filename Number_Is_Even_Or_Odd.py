number1 = 21  # Define a test number (odd)
number2 = 22  # Define another test number (even)

def number_is_even_or_odd(num):
   if num % 2 == 0:  # Check if the number is divisible by 2 (remainder is 0)
       return "even"  # If divisible by 2, it's even
   else:
       return "odd"  # If not divisible by 2, it's odd

print("The number is", number_is_even_or_odd(number1))  # Test with number1 (21)
print("The number is", number_is_even_or_odd(number2))  # Test with number2 (22)