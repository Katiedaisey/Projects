# Coin Flip Simulation - 
# Write some code that simulates flipping a single coin 
# however many times the user decides. 
# The code should record the outcomes and count the number of tails and heads.

import random

count = int(raw_input('Flips?: '))
tails = 0
heads = 0

cou = 0
while cou < count:
	num = random.randint(1,2)
	if num == 1:
		tails = tails + 1
	elif num == 2:
		heads = heads + 1
	cou = cou + 1
	
print "Tails: ", tails, "\n Heads: ", heads