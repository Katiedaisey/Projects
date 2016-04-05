# **Pig Latin** - 
# Pig Latin is a game of alterations played on the English language game. 
# To create the Pig Latin form of an English word the initial consonant 
# sound is transposed to the end of the word and an ay is affixed 
# (Ex.: "banana" would yield anana-bay). 
# Read Wikipedia for more information on rules.


string = raw_input('Enter message: ')
string = string.lower()
string = string.split()

vowels = ['a','e','i','o','u']

for i, word in enumerate(string):
	tmp = word[0]
	# check length a and i
	if len(word) == 1:
		if word is 'a':
			string[i] = 'ay'
		else:
			string[i] = word + 'ay'
	
	
	# check vowel
	elif tmp in vowels:
		string[i] = word + 'ay'
		
		
	
	# else constant
	else:
		tmp = tmp + 'ay'
		string[i] = word[1:len(word)] + tmp
	
string = ' '.join(string)
print string	

# does not handle punctuation