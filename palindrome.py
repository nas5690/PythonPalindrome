#Python program to see if a string is a palindrome or not

#declare string
str = 'Level'

#to check regardless of upper/lowercase letters
str = str.casefold()

#declare function to reverse string
rev_str = reversed(str)

#if/else function to see if the string is same as reverse of the string
if list(str) == list(rev_str): 
	print("Is a palindrome")
else: 
	print("Is not a palindrome")
