initialString = "IloveDSA"  # Define the string we want to reverse

def reverse_a_string(string):
   newString = []  # Create an empty list to store characters
   for i in range((len(string)-1), -1, -1):  # Loop from last index to first (decreasing by 1)
        newString.append(string[i])  # Add each character to our list in reverse order
   return "".join(newString)  # Convert list back to a string and return it

print(reverse_a_string(initialString))  # Call the function and print the reversed string