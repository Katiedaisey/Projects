# **Prime Factorization** - 
# Have the user enter a number and find all Prime Factors 
# (if there are any) and display them.

try:
	target2 = int(raw_input('Enter a number: '))
except:
	print 'Enter an integer!'
	raise SystemExit

def factor(target):
	if target == 1:
		primes = [1]

	elif target == 2:
		primes = [1,2]
	
	else:
		num = 2 # start at 2
		primes = [1,2]
		yes = 0
		
		while num < target:
			num = num + 1
			yes = 0
			# start at 3
			# check if num is prime
			for i in primes[1:]:
				if num % i != 0:
					# not divisible by a found prime
					# possibly prime
					yes = yes + 1
			# if not divisible by all primes
			if yes == (len(primes) - 1):
				# add num to primes
				primes.append(num)

	
	return primes;

primes2 = factor(target2)

primes = list()
for prime in primes2:
	if target2 % prime == 0:
		primes.append(prime)

if len(primes) == 2:
	print 'Only 2 prime factors!'
	print 'This is a prime number!'

else:
	print len(primes), ' found!'
	print primes
	
