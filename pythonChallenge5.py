"""
pythonChallenge5.py

Instructions:
The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization. Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even".
"""

def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = input_string.replace(" ","")
	new_string = new_string.lower()

	reverse_string = new_string[::-1]
	# Traverse through each letter of the input string
	
	# Compare the strings
	if new_string == reverse_string:
		return True
	else:
		return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True