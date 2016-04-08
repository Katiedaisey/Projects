# **Next Prime Number** - 
# Have the program find prime numbers until the 
# user chooses to stop asking for the next one.


cont = str(raw_input('Next Prime Number (y/n)? '))
cont = cont.lower()

if cont == 'y':
	prime = 1
	primes = [1]
	print prime
	cont = str(raw_input('Next Prime Number (y/n)? '))
	cont = cont.lower()
	if cont == 'y':
		prime = 2
		primes = [1,2]
		print prime
	else:
		raise SystemExit
else:
	raise SystemExit

cont = str(raw_input('Next Prime Number (y/n)? '))
cont = cont.lower()


while cont == 'y':
	num = prime + 1
	print prime
	yes = 0
	
	
	while yes == 0:
		for i in primes[1:]:
			if num % i != 0: 
				# not divisible by a found prime
				# prime
				yes = yes + 1
		# increment num and try again
		if yes == len(primes)-1:
			primes.append(num)
			prime = num
		else:
			yes = 0
			num = num + 1
	cont = str(raw_input('Next Prime Number (y/n)? '))
	cont = cont.lower()
	

print len(primes)-1,' primes found: '
print primes[:-1]
