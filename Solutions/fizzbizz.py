# Fizz Buzz - 
# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print Fizz instead of the number 
# and for the multiples of five print Buzz. 
# For numbers which are multiples of both three and five print FizzBuzz.

nums = range(1, 100, 1)
print nums

for num in nums:
	if num % 15 == 0:
		wrd = "FizzBuzz"
	elif num % 5 == 0:
		wrd = "Buzz"
	elif num % 3 == 0:
		wrd = "Fizz"
	else:
		wrd = str(num)
		print wrd
	
	print wrd 	