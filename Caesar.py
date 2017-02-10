# Developer: Aastha Anand
"""A program that can encode decode Caesar ciphers. Given an input string and an offset, 
 program should output an encrypted string. In this assignment we assume that : Input
 and output contain only space,numeric digits,upper case letters and lower case letters.
 In the order of [space][0-9][A-Z][a-z] """

# Store user inputs
plaintext= input("Enter your string:")
key_str = input("Enter the offset:")

#predefined cipher code list
stored_data = ' 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

#perform encryption
ciphertext = ''
for c in plaintext:
	if c in stored_data:
		ciphertext += stored_data[(stored_data.index(c)+key)%len(stored_data)]

print("Encrypted code is:",ciphertext)




	
		




	
