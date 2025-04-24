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
testArr = [3,5,6,7,8,8,9,4,5,7,7,8,8,9,7,9,10,11,12,13,14,15,16,17,18,19,20]

def sum_of_all_numbers(arr):
    total = 0
    for num in arr:
        total += num
    return total
print("The sum of all numbers in the array is:", sum_of_all_numbers(testArr))
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
number1 = 21
number2 = 22
def number_is_even_or_odd(num):
    if num %2 == 0:
        return "even"
    else:
        return "odd"
print("The number is",number_is_even_or_odd(number1))
print("The number is",number_is_even_or_odd(number2))
```

<h3>Explantation </h3>

- We define to numbers 21 which we know is odd and 22 which we know it even
- We then define a function passing num as an argument
- In the function we have an if statement, the if statement checks that if you divide the number given is the reminder 0 . This is the divisibility test for 2.
- If true then the number is divisible by 2 and is thus even
- Otherwise it is not divisible by 2 and is thus odd

## Question 3: Factorial Using a Loop

```python
initialNumber = 5
def factorial_using_loop(num):
    total = num
    for i in range(1,num):  
        total = total * i
    return total
print("The factorial is",factorial_using_loop(initialNumber))
```


<h3>Explanation</h3>

- We set the initial number to 5 which we will use to test if the function works
- We define a function with an argument num
- we set the total to num since factorials are <strong> n*(n-1)*(n-2)..... *1</strong> this the inital number is the total
- We loop from all numbers from 1  to the num while adding the multiplication of it and the total

## Question 4:  Reverse a String 
```python
initialString = "IloveDSA"
def reverse_a_string(string):
    newString = []
    for i in range((len(string)-1),-1,-1):
         newString.append(string[i])
    return "".join(newString)
print(reverse_a_string(initialString))
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
initialNumber = 5
total =0
def factorial_using_recursion(num):
    if num == 1 or num ==0:
        return 1
    else:
        return  num * factorial_using_recursion(num-1)
print("The factorial is", factorial_using_recursion(initialNumber))
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
number = 2323232323
def sum_of_digits(num):
    total =0
    while num> 0:
        total += num % 10
        num = num//10
    return total
print("The sum of the digits is", sum_of_digits(number))
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

