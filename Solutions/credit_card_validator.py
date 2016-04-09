# **Credit Card Validator** - 
# Takes in a credit card number from a common credit card vendor 
# (Visa, MasterCard, American Express, Discoverer) and validates 
# it to make sure that it is a valid number 
# (look into how credit cards use a checksum).




valid = 0
while valid == 0:
	num = raw_input('Enter a card number: ')
	
	try:
		num = num.split('-')
		num = ''.join(num)
	except:
		pass

	
	if len(num) == 15 and (num[0:2] == '34' or num[0:2] == '37'):
		type_card = "American Express"
		valid = 1
	elif len(num) == 13 and num[0] == '4':
		type_card = 'Visa'
		valid = 1
	elif len(num) == 15 and int(num[0:2]) > 50 and int(num[0:2]) < 56:
		type_card = 'Master Card'
		valid = 1
	elif len(num) == 15 and num[0] == '4':
		type_card = 'Visa'
		valid = 1
	else:
		print 'Invalid card.'
		valid = 0


# reverse digits
new = list(num)
new.reverse()

# double evo digit
for n in range(0,len(new)): 
	if n % 2 != 0:
		a = int(new[n])
		a = a * 2
		new[n] = str(a)
	

# split digits
new = ''.join(new)
new = list(new)

# add digits
check = 0
for i in new:
	i = int(i)
	check = check + 0

# if divides by 0 - valid
if check % 10 == 0:
	print num, ' is a valid ', type_card, ' card.'

