# Sum of Consecutive Integers
'''
first_number = int(input("Please enter the first number: "))
final_number = int(input("Please enter the final number: "))
if first_number > final_number:
    first_number, final_number = final_number, first_number #this is how you swap variables in python

sum_of_consecutive_integers = first_number
for i in range(first_number, final_number, 1):
    sum_of_consecutive_integers += i+1
print(sum_of_consecutive_integers)
'''

'''
The way gauss did it however:

first_number = int(input("Please enter the first number: "))
final_number = int(input("Please enter the final number: "))

# Ensure first_number is less than or equal to final_number
if first_number > final_number:
    first_number, final_number = final_number, first_number

# Calculate the number of terms
n = final_number - first_number + 1

# Initialize the sum to 0 and not first_number because i'll be using first_number and final_number as a group
sum_of_consecutive_integers = 0
if n % 2 == 0:
    while first_number < final_number:
        sum_of_consecutive_integers += (first_number + final_number)
        first_number += 1 #now this is super interesting, i stop using first_number and final_number as constants and start updating their variables to match the consecutive integers like pointers in c. now of course this works only if consecutive +1 integers are being added
        final_number -= 1
else:
    # Odd number of terms: Pair terms symmetrically, and add the middle term separately
    while first_number < final_number:
        sum_of_consecutive_integers += (first_number + final_number)
        first_number += 1
        final_number -= 1
    # Add the middle term
    sum_of_consecutive_integers += first_number

print(sum_of_consecutive_integers)

'''

# Sum of Sequential Integers
'''
first_number = int(input("Please enter the first number: "))
final_number = int(input("Please enter the final number: "))
if first_number > final_number:
    first_number, final_number = final_number, first_number #this is how you swap variables in python

sum_of_sequential_integers = 0
if first_number % 2 != 0: #is odd
    first_number += 1 #go to the +1 even number
for number in range(first_number, final_number + 1, 2):
    sum_of_sequential_integers += number
print(sum_of_sequential_integers)
'''

# Conditional Sum of Integers
'''
first_number = int(input("Please enter the first number: "))
final_number = int(input("Please enter the final number: "))
if first_number > final_number:
    first_number, final_number = final_number, first_number #this is how you swap variables in python

numbers = []
sum_of_even_numbers = 0
for number in numbers:
    if number % 2 == 0:
        sum_of_even_numbers += number
print(sum_of_even_numbers)
'''