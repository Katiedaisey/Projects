# **Check if Palindrome** - 
# Checks if the string entered by the user is a palindrome. 
# That it reads the same forwards as backwards like racecar

new = raw_input('Enter a string:')
space = raw_input('Consider spaces? (y/n) ')
space = space.lower()


if space == 'n':
	new.split()
	new = ''.join(new)

compare = list(new)
compare.reverse()
compare = ''.join(compare)

if compare == new:
	print 'Palindrome!'
else:
	print ' Not a Palindrome :('