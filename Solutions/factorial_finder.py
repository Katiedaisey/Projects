# **Factorial Finder** - 
# The Factorial of a positive integer, n, is defined as 
# the product of the sequence n, n-1, n-2, ...1 and the 
# factorial of zero, 0, is defined as being 1. 
# Solve this using both loops and recursion.

def factorial(num):
	if num < 2:
		fact = 1
	else:
		fact = num * factorial(num - 1)
	return fact;



num = int(raw_input('Enter a number: '))
typ = raw_input('loops or recursion (l/r)? ')
fact = 1


if typ == 'l':
	if num < 2:
		fact = 1
	else:
		n = 1
		while n < num:
			n = n + 1
			fact = fact * n
	print fact			


elif typ == 'r':
	if num < 2:
		fact = 1
	else:
		fact = factorial(num)
	
	print fact



