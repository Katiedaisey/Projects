# not yet working
# **Number Names** - 
# Show how to spell out a number in English. 
# You can use a preexisting implementation or roll your own, 
# but you should support inputs up to at least one million 
# (or the maximum value of your language's default bounded integer type,
#  if that's less). *Optional: Support for inputs other than positive 
# integers (like zero, negative integers, and floating-point numbers).*


num = int(raw_input('Enter a number: '))


def spell():
	dict = {'0': 'zero'}
	dict['1'] = 'one'
	dict['2'] = 'two'
	dict['3'] = 'three'
	dict['4'] = 'four'
	dict['5'] = 'five'
	dict['6'] = 'six'
	dict['7'] = 'seven'
	dict['8'] = 'eight'
	dict['9'] = 'nine'
	dict['11'] = 'eleven'
	dict['12'] = 'twelve'
	dict['13'] = 'thirteen'
	dict['14'] = 'fourteen'
	dict['15'] = 'fifteen'
	dict['16'] = 'sixteen'
	dict['17'] = 'seventeen'
	dict['18'] = 'eighteen'
	dict['19'] = 'nineteen'
	dict['2s'] = 'twenty'
	dict['3s'] = 'thirty'
	dict['4s'] = 'forty'
	dict['5s'] = 'fifty'
	dict['6s'] = 'sixty'
	dict['7s'] = 'seventy'
	dict['8s'] = 'eighty'
	dict['9s'] = 'ninety'
	dict['0s'] = ''
	return dict;


def huns(num):
	if num < 20:
		num = str(num)
		ans = dict[num]
	
	elif num > 19:
		string = str(num)
			
		if len(string) > 2:
			hun = string[-3]
			if hun != '0':
				ans = dict[hun] + ' hundred '
		if len(string) > 1:
			tens = string[-2]
			if tens != '0':
				if string[-1] != '0':
					ans = ans + dict[(tens + 's')] + ' '
				else:
					ans = ans + dict[(tens + 's')]	
			ones = string[-1]
			if ones != '0':
				ans = ans + dict[ones]
	return ans
	

ans = 'begin'
dict = spell()
string = str(num)
count = 0

while len(string) > 3:
	count = count + 1
	last = string[-3:]
	last = int(last)
	last = huns(last)
	if ans == 'begin':
		ans = last
	else:
		ans = last + ans
	if count == 1 and last != ' ':
		ans = ' thousand ' + ans
	if count == 2:
		ans = ' million ' + ans
	if count == 3:
		ans = ' billion ' + ans
	string = string[:-3]

if len(string) < 4:
	num = int(string)
	if ans == 'begin':
		ans = huns(num)
	else:
		ans = huns(num) + ans
	
	
print ans

