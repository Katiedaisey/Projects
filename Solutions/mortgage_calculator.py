# **Mortgage Calculator** - 
# Calculate the monthly payments of a fixed term mortgage over given Nth 
# terms at a given interest rate. Also figure out how long it will take 
# the user to pay back the loan. For added complexity, add an option for 
# users to select the compounding interval (Monthly, Weekly, Daily, 
# Continually).

import math

mort = float(raw_input('Mortgage Amount: '))
rate = float(raw_input('Annual Percentage Rate: '))
term = float(raw_input('Terms (in months): '))
termt = term
comp = ['Monthly', 'Weekly', 'Daily', 'Continually']
compt = None
idx = None
for item in enumerate(comp):
	print '[%d] %s' % item

while compt is None:
	while idx is None:
		try:
			idx = int(raw_input('Compounding Interval: '))
		except ValueError:
			print 'Please Enter Number of Compounding Interval'
			continue
		else:
			break
	
	try:
		compt = comp[idx]
	except:
		print 'Please Enter a Valid Number'
		idx = None
		continue
	else:
		break

# monthly
if idx == 0:
	rate = rate / 12

# weekly
elif idx == 1:
	rate = rate / 52
	term = term * 52 / 12 

# daily
elif idx == 2:
	rate = rate / 365
	term = term  * 365 / 12

# continuous
elif idx == 3:
	term = term / 12
	out = mort * math.exp(rate*term)
	print 'Total Repayment: ', round(out,2)
	outt = out/termt
	print 'Monthly Payment: ', round(outt,2)
	raise SystemExit


out = round(mort * (1 + rate)**term, 2)
print 'Total Repayment: ', out
outt = round(out/termt, 2)
print 'Monthly Payment: ', outt