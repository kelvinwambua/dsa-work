testArr = [3,5,6,7,8,8,9,4,5,7,7,8,8,9,7,9,10,11,12,13,14,15,16,17,18,19,20]

def sum_of_all_numbers(arr):
    total = 0
    for num in arr:
        total += num
    return total


print("The sum of all numbers in the array is:", sum_of_all_numbers(testArr))
