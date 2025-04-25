<h2>SYENGO KELVIN WAMBUA - 189989</h2>


## PROJECT SECTIONS
- [Question 1: Sum of All Numbers](#question-1--sum-of-all-numbers)
- [Question 2: Number is Even or Odd](#question-2--number-is-even-or-odd)
- [Question 3: Factorial Using a Loop](#question-3-factorial-using-a-loop)
- [Question 4: Reverse a String](#question-4--reverse-a-string)
- [Question 5: Factorial Recursive](#question-5-factorial-recursive)
- [Question 6: Sum of Digits](#question-6-sum-of-digits)

## Question 1 : Sum of All Numbers

```python
testList = [3,5,6,7,8,8,9,4,5,7,7,8,8,9,7,9,10,11,12,13,14,15,16,17,18,19,20]  # Define a list of numbers to sum

def sum_of_all_numbers(list):  # Define a function that takes a list as input
   total = 0  # Initialize the sum to zero
   for num in list:  # Iterate through each number in the list
       total += num  # Add the current number to our running total
   return total  # Return the final sum
 
print("The sum of all numbers in the array is:", sum_of_all_numbers(testList))  # Call the function and print the result
```
<h3>Explanation</h3>

- We define an list of numbers
- Define the function with the argument passing the list
- Set our total to 0 which we will update as we go on
- We have a loop which select each number in the list
-  the <strong> total += num </strong> is equivalent to <strong>total = total + num</strong> . It sets the new total to the previous one plus the current number in the array
- We then return the total
- We have a print statement to return the data to the user

## Question 2 : Number is Even or Odd

A number is even if divisible by 2 
```python
number1 = 21  # Define a test number (odd)
number2 = 22  # Define another test number (even)

def number_is_even_or_odd(num):
   if num % 2 == 0:  # Check if the number is divisible by 2 (remainder is 0)
       return "even"  # If divisible by 2, it's even
   else:
       return "odd"  # If not divisible by 2, it's odd

print("The number is", number_is_even_or_odd(number1))  # Test with number1 (21)
print("The number is", number_is_even_or_odd(number2))  # Test with number2 (22)
```

<h3>Explantation </h3>

- We define to numbers 21 which we know is odd and 22 which we know it even
- We then define a function passing num as an argument
- In the function we have an if statement, the if statement checks that if you divide the number given is the reminder 0 . This is the divisibility test for 2.
- If true then the number is divisible by 2 and is thus even
- Otherwise it is not divisible by 2 and is thus odd

## Question 3: Factorial Using a Loop

```python
initialNumber = 5  # Define the number for which we want to calculate factorial

def factorial_using_loop(num):
   total = 1  # Initialize total to 1 
   for i in range(1, num + 1):  # Loop through numbers 1 to num inclusive
       total = total * i  # Multiply the current total by the current number
   return total

print("The factorial of", initialNumber, "is", factorial_using_loop(initialNumber))  # Calculate and print 5!
```


<h3>Explanation</h3>

- We set the initial number to 5 which we will use to test if the function works
- We define a function with an argument num
- we set the total to 1 since factorials are <strong> n*(n-1)*(n-2)..... *1</strong> t
- We loop from all numbers from 1  to num while multiplying the current total by the number

## Question 4:  Reverse a String 
```python
initialString = "IloveDSA"  # Define the string we want to reverse

def reverse_a_string(string):
   newString = []  # Create an empty list to store characters
   for i in range((len(string)-1), -1, -1):  # Loop from last index to first (decreasing by 1)
        newString.append(string[i])  # Add each character to our list in reverse order
   return "".join(newString)  # Convert list back to a string and return it

print(reverse_a_string(initialString))  # Call the function and print the reversed string
```

<h3>Explanation</h3>

- So we declare a string
- We define a function that takes string as an argument
- A string is basically a listof characters so we define an empty array which we will later add the list of characters
- We loop through the string provided 
- In Python the first arguement is the start point of the loop and since we have 0 based indexing we have to minus 1 to get the last element of the list , the next argument it takes is the stop and since we want it to go all the way to 0 we set the stop value to -1 to ensure we access all the elements. After that we have the steps we want the loop to move through so we will -1 to go through each index of the list
- We then convert and join the array to the string and we print out the result

## Question 5: Factorial Recursive

```python
initialNumber = 5  # Define the number for which we want to calculate factorial
def factorial_using_recursion(num):
   if num == 1 or num == 0:  # Base case: factorial of 0 or 1 is 1
       return 1
   else:  # Recursive case: n! = n × (n-1)!
       return num * factorial_using_recursion(num-1)  # Call the function recursively with num-1
print("The factorial is", factorial_using_recursion(initialNumber))  # Calculate and print 5!
```

<h3>Explantation</h3>

- We start by defining an initial number: <strong>initialNumber = 5 </strong>. This is the number whose factorial we want to calculate.
- We then define a **recursive function** called factorial_using_recursion(num) that calculates the factorial of a given number num.
- Inside the function:
	- **Base case**: If num is 0 or 1, we return 1. This is because the factorial of 0 and 1 is always 1.  
    - **Recursive case**: For any other value of num, we return <strong>num * factorial_using_recursion(num - 1)</strong>. This means the function keeps calling itself with smaller and smaller values of num until it reaches the base case.
- We print the result 


## Question 6: Sum of Digits 

```python
number = 2323232323  # The number whose digits we want to sum

def sum_of_digits(num):
   total = 0  # Initialize the sum to zero
   while num > 0:  # Continue until no digits remain
       total += num % 10  # Get the last digit and add it to total
       num = num // 10  # Remove the last digit from the number
   return total

print("The sum of the digits is", sum_of_digits(number))  # Display the result
```

<h3>Explanation</h3>

- We define a  number
- We define a function taking the argument  num
- We set the total to 0 and we will add to it as we loop
- We then do the modulus of of the number with 10 this will give use the digits other than the last one which in this case is 3
- We add this 3 to the total 
- We then do floor division to remove the decimal point leaving us with the all the digits other than the last one
- This continues until we have 0 digits
- We print the statement 

