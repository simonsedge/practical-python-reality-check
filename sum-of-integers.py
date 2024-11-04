first_number = int(input("Please enter the first number: "))
final_number = int(input("Please enter the final number: "))

if first_number > final_number:
    first_number, final_number = final_number, first_number #this is how you swap variables in python

sum_of_integers = first_number
for i in range(first_number, final_number):
    sum_of_integers += i+1
print(sum_of_integers)