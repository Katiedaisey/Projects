# **Change Return Program** - 
# The user enters a cost and then the amount of money given. 
# The program will figure out the change and the number of 
# quarters, dimes, nickels, pennies needed for the change.


cost = float(raw_input('Total Price: '))
cash = float(raw_input('Cash Given: '))

change = cash - cost
if change == 0:
	print "Exact Amount - No change given."
elif change < 0:
	print "Insufficient Funds."

dol = int(change)
print dol
coin = change - float(dol)
print coin
quarter = int(coin / .25)
coin = coin - (quarter * .25)
dime = int(coin / .1)
coin = coin - (dime * .1)
nickel = int(coin / .05)
coin = coin - (nickel * .05)
penny = int(coin / .01)

print "Please return: ", dol, " Dollars, ", quarter, "Quarters, ", dime, "dimes, ", nickel, "Nickels, and ", penny, "pennies."