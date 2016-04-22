# input pdf articles into bibdesk
# pull bibtex info from google scholar

import os
import re

# pdf files in directory are converted to txt files in new subdirectory
command = '/Users/katiedaisey/Desktop/xpdfbin-mac-3.04/bin32/pdftotext'


#dir = raw_input('Enter directory: ')
dir = '/Users/katiedaisey/Documents/to-read'

command = command + ' -l 1 -q ' + dir + '/'
newdir = dir + '/text'
try:
    os.stat(newdir)
except:
    os.mkdir(newdir) 

files = os.listdir(dir)
for f in files:
	f = re.findall('(.*)\.pdf$', f) 
	if len(f) > 0:
		tmp = command + f[0] + '.pdf ' + newdir + '/' + f[0] + '.txt'
		#print tmp
		os.system(tmp)
		
		
files = os.listdir(newdir)
for f in files:
	with open(f) as f:
		content = f.readlines()
    	print content