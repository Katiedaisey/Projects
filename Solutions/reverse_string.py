# **Reverse a String** - Enter a string and the program will reverse it and print it out.

forward = raw_input("Enter a string: ")

#forward = forward.split('')

a = range(len(forward)-1,-1,-1)


backward = range(len(forward))
count = 0
for i in a:
	backward[count] = forward[i]
	count = count + 1

print ''.join(backward)