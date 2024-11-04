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

