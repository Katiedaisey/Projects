# **Tax Calculator** - 
# Asks the user to enter a cost and either a country or state tax. 
# It then returns the tax plus the total cost with tax.


cost = float(raw_input('Cost: '))
tax = float(raw_input('Tax: '))

ttl = cost + (cost * tax)

# check digits
rem = ttl - int(ttl)
string = str(rem)

# more than 2 digits
if len(string) > 4:
	if string[3] == '5':
		# round up
		if string[4] >= '5':
			string = string[0:3] + "6"
		# round down
		if string[4] < '5':
			string = string[0:4]
		
	string = str(int(ttl)) + string[1:4]
	
print 'Cost with Tax: ', string