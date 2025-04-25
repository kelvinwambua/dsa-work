testList = [3,5,6,7,8,8,9,4,5,7,7,8,8,9,7,9,10,11,12,13,14,15,16,17,18,19,20]  # Define a list of numbers to sum

def sum_of_all_numbers(list):  # Define a function that takes a list as input
   total = 0  # Initialize the sum to zero
   for num in list:  # Iterate through each number in the list
       total += num  # Add the current number to our running total
   return total  # Return the final sum
 
print("The sum of all numbers in the array is:", sum_of_all_numbers(testList))  # Call the function and print the result