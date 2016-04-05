# **Count Vowels** - 
# Enter a string and the program counts the number of vowels in the text. 
# For added complexity have it report a sum of each vowel found


mess = raw_input('Enter message: ')
mess = mess.lower()

vowel = list('aeiou')
dict = {}

for i in vowel:
	dict[i] = mess.count(i)
for i in dict:
	print i, dict[i]
	