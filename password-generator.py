import random

# Character lists
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # Convert numbers to strings
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', ',', '<', '>', '.', '?', '/', '|', 'º', 'ª', '«', '»']

# Define desired password length
desired_length = 90
password = [] # could've instead done passworrd = []*90 but then wouldn't have desired_length to handle non-multiples of 4

# Main loop to fill password with groups of 4 until nearing the end
for i in range(0, desired_length - 3, 4):
    password.append(random.choice(special_characters))
    password.append(random.choice(uppercase))
    password.append(random.choice(numbers))
    password.append(random.choice(lowercase))

# Handle remaining characters if desired_length doesn't go high enough to be a multiple of 4
remaining = desired_length - len(password)
if remaining > 0:
    # Add the exact number of remaining characters
    all_characters = [random.choice(special_characters), random.choice(uppercase), random.choice(numbers), random.choice(uppercase)]
    password.extend(all_characters[:remaining])

# Join the password list into a single string
password_string = ''.join(password)
print(password_string)

