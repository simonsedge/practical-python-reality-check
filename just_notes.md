- Decomposition tip: assume every little part of a subproblem can be seen as a variable

---

characteristics_1 = ...
characteristics_2 = ...
characteristics_3 = ...

var_1 = characteristics_1 and not characteristics_2 or characteristics_3

---

list_1 = []
list_2 = []

nested_list = [list_1, list_2] (sometimes new_list = list_1 + list_2 is more practical)

var_1 = ...
var_2 = ...

nested_list[var_1 - 1][var_2 - 1] = "X" is how you can change the value of a nested list and make it human friendly with base10 counting system

---

var_1 = input("Where do u want to put the treasure: ")
var_2 = int(position[0]) is storing the first value of the input

---

range(0, len(list) - 3, 4):
    Start at 0: Begin from the first position in the password list.
    End at len(password) - 3: Preventing going out of the list when getting to the end of it.
    Step of 4: This increments i by 4 each time, so each new loop iteration starts at the next group of four characters.

---

list = [None] * 95 defines 95 empty slots in the list.

---

whats the difference between the 2 highest_score initializations in these blocks of code? initializing it to 0 will fuck it up if list contains negative numbers

```python
{
    student_scores = input("strings separated by commas supposed to form a list")
for n in range(0, len(student_scores)): #you tend to call it n when its position, i when its an iterating thing. but the main point is you're using the actual integers in that range so defining the range depends on the problem. if it was a sum of constant integers from 1-100 you'd use range(1, 100 + 1) to get to 100. if it's a matter of position you'd prob use like range(0, len(student_scores))
    student_scores[n] = int(student_scores[n])
highest_score = 0 # vs highest_score = student_scores[0]
for score in student_scores:
    if score > highest_score:
        highest_score = score
        print(f"Maximum element is: {highest_score}")
}
```

---

this is how you swap variables in python:
first_number, final_number = final_number, first_number

---

