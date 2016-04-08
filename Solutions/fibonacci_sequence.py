# **Fibonacci Sequence** - 
# Enter a number and have the program generate the 
# Fibonacci sequence to that number or to the Nth number.

num = int(raw_input('Enter a number: '))
count = 2
fib = [1,1]

if num == 1:
	fib [1]
if num == 2:
	fib = [1,1]
	count = count + 1
elif num > 2:
	while count < num:
		fib.append(int(fib[-1]) + int(fib[-2]))
		count = count + 1

print 'Fibonacci Sequence with ',num,' terms:'
print fib