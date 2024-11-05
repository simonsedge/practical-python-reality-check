# XOR with Shifted Key Cipher with Hexadecimal Encoding

key = "key"  # Shared secret key
original_text = input("Enter the text to be encoded or decoded: ")

def shift_key(key):
    """Shift the key by moving the first character to the end."""
    return key[1:] + key[0]
    '''
    slice notation | key[1:] means "take all characters of key starting from the second character up to the end."
    example | if key = "securekey", then key[1:] would be "ecurekey" (everything except the first character)
    then key[0] accesses the first character of key and when adding them moves the first character to the end of the string
    '''

def xor_shifted_key_encode(plaintext, key): # even though the data used will have its root in original_text, plain_text is just the name of the argument/placeholder to the function that passes any string to xor_shifted_key_encode()
    """Encrypts plaintext using XOR with shifted key and converts to hex."""
    encoded_chars = [None] * len(plaintext)  # Initialize a list of None with the length of the plaintext (better for memory with bigger inputs and accessing specific indexes and other benefits but an overkill here)
    for i, char in enumerate(plaintext): # i is index of char in plaintext and char is the value of each character in the plaintext string. enumerate() returns an iterator that produces pairs of index and value for each element in the plaintext string. This is useful when we need to modify or access elements based on their position in the string like when want to store each encoded character in encoded_chars at the exact same index (encoded_chars[i]).
        # XOR each character with the first character of the key
        encoded_char = ord(char) ^ ord(key[0]) # ord() returns the ASCII numerical code of the character. ^ is the bitwise XOR operator. It compares each bit of the first operand (char) to the corresponding bit of the second operand (key[0]) and returns a 1 if the bits are different and 0 if they are the same. This is how XOR encryption works. The result is then stored in encoded_char.
        encoded_chars[i] = format(encoded_char, '02x')  # format() converts the integer value of encoded_char into a string (hexadecimal). The '02x' format specifier: x converts the integer to lowercase hexadecimal. 02 means the string should be padded with zeros (0s first) to achieve a minimum width of 2 characters. This is necessary because each hexadecimal character represents 4 bits of data, and a single byte (8 bits) can be represented by 2 hexadecimal characters. So, if the result of the XOR operation is a single-digit hexadecimal number, it needs to be padded with a leading zero to maintain the correct length of the encoded string. Without padding, the decryption process would not be able to correctly interpret the encoded data because it expects each character to be 2 hexadecimal digits long.
        # Shift the key after each XOR operation
        key = shift_key(key)
    return ''.join(encoded_chars)  # Join the list into a single hex string

def xor_shifted_key_decode(ciphertext, key):
    """Decrypts ciphertext in hex format using XOR with shifted key."""
    decoded_chars = [None] * (len(ciphertext) // 2)  # Initialize list with half the length (since each hex is 2 chars)
    for i in range(0, len(ciphertext), 2): # Iterate over the hex string two characters at a time (since each hex is 2 chars)
        # Convert hex back to integer, then XOR with the first character of the key
        encoded_char = int(ciphertext[i:i+2], 16) # ciphertext[i:i+2] extracts a substring of 2 characters from the ciphertext string. The slice notation [i:i+2] means "take all characters of ciphertext starting from the i-th character up to the (i+2)-th character." int() converts the hexadecimal string into an integer. The second argument to int() is the base of the number system to use for conversion. In this case, 16 is used because the string is in hexadecimal format. The result is then stored in encoded_char. example: if ciphertext[i:i+2] is "61", int("61", 16) would be 97 (the ASCII numerical code for 'a') and this value is stored in encoded_char.
        decoded_char = chr(encoded_char ^ ord(key[0])) # chr(...) converts the resulting integer value into a character. inside brackets it XORs the ASCII integer value in ord(key[0]) with encoded_char, reversing the XOR operation
        decoded_chars[i // 2] = decoded_char  # [i // 2] calculates the correct index for decoded_charts since i is iterating by 2. decoded_chars[i // 2] = decoded_char stores the decoded character in the correct position in the decoded_chars list.

        # Shift the key after each XOR operation
        key = shift_key(key)
        
    return ''.join(decoded_chars)  # Join the list into a single decoded string

# Ask the user whether they want to encrypt or decrypt
decrypt_or_encrypt = input("Do you want to encrypt or decrypt? press 'd' or 'e': ")
while decrypt_or_encrypt != "d" and decrypt_or_encrypt != "e":
    print("Invalid input. Please enter 'd' or 'e'.")
    decrypt_or_encrypt = input("Do you want to encrypt or decrypt? press 'd' or 'e': ")

# Encrypt or decrypt based on user input
if decrypt_or_encrypt == "e":
    encrypted_text = xor_shifted_key_encode(original_text, key)
    print("Encrypted text (hex):", encrypted_text)
else:
    # Directly decrypt the input text, assuming it's in hex format
    decrypted_text = xor_shifted_key_decode(original_text, key)
    print("Decrypted text:", decrypted_text)