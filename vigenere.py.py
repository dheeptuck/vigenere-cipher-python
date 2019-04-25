# This is sample program to emulate vigenere cipher encryption and decryption. 
# This program consists of four steps.
# Step 1 : Convert the string(plain text and key) to equivalent number list for 
# 	     computation.
# Step 2 : Encrypt the number list.
# Step 3 : Decrypt the cipher list.
# step 4 : Convert the deciphered list to string.(i.e 0->a, 1->b and so on)
# Note: This only works for strings with lower case alphabets.


# Plain text to be encrypted
plain_text_str = "weareunited"
# Key
key_text_str   = "bcasdhr"


#Step 1- Convert input strings into corresponding number lists(i.e A-Z -> 0-25)
# Used to store the string to number mapping a->0, b->1 and so on
plain_text_num = []
key_test_num   = []

# Convert to number equivalent by substracting ASCII value of 'a' 
for character in plain_text_str:
	plain_text_num.append(ord(character) - 97)

for character in key_text_str:
	key_test_num.append(ord(character) - 97)

print(plain_text_num)
print(key_test_num)

#Step 2: Encryption
# Ci - The ith cipher text character
# Pi - The ith plain text character 
# Ki - The ith key text character 
# Ci = (Pi + Ki)mod 26
idx = 0
# Length of the key
LK = len(key_test_num)
cipher_char_list = []
for element in plain_text_num:
	cipher_char_list.append(element + key_test_num[idx%LK])
	idx = idx + 1
print(cipher_char_list)

#Step 3: Decryption
# Ci - The ith cipher text character
# Pi - The ith plain text character 
# Ki - The ith key text character 
# Ci = (Ci - Ki)mod 26
idx = 0
LK = len(key_test_num)
decrypt_char_list = []
for element in cipher_char_list:
	decrypt_char_list.append(element - key_test_num[idx%LK])
	idx = idx + 1
print(decrypt_char_list)

#Step 4: Convert to string
# Convert to number equivalent by adding ASCII value of 'a' 
deciphered_string = ""
for element in decrypt_char_list:
	deciphered_string += (chr(element+97))

print(deciphered_string)