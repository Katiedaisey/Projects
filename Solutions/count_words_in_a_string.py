# **Count Words in a String** - 
# Counts the number of individual words in a string. 
# For added complexity read these strings in from a 
# text file and generate a summary.


file_name = raw_input('Enter a file: ')
try:
	fh = open(file_name, 'r')
except:
	print 'Not a valid file'
	raise SystemExit

count = 0
for line in fh:
	line.split()
	count = len(line) + count


print count, 'words'