# **Happy Numbers** - 
# A happy number is defined by the following process. 
# Starting with any positive integer, replace the number by the sum of 
# the squares of its digits, and repeat the process until the number equals 1 
# (where it will stay), or it loops endlessly in a cycle which does not 
# include 1. Those numbers for which this process ends in 1 
# are happy numbers, while those that do not end in 1 are unhappy numbers. 
# Display an example of your output here. Find first 8 happy numbers.


num = int(raw_input('Enter any positive integer: '))




def happy(num):
	num = str(num)
	nothappy = list()
	
	while num != 1 and (num  not in nothappy):
		nothappy.append(num)
		string = str(num)
		total = 0
		for i in string:
			a = int(i)
			total = total + a*a
		num = total
	
	return num;


happy_num = list()

while len(happy_num) < 8:
	new = happy(num)
	if new == 1:
		happy_num.append(num)
	num = num + 1

print happy_num	
	