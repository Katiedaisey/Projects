# searches for doi's


import os
import re
import subprocess



dir = '/Users/katiedaisey/Documents/to-read'
newdir = dir + '/text'

files = os.listdir(newdir)
#print files
#print files[0]
count = 0
for f in files[0:1]:
	print f
	count = count + 1
	doi = list()
	print 'file: ',count
	with open(newdir + '/' + f) as f:
		content = f.readlines()
		#print content	
		for line in content:
			line = line.lower()
			#print line
			if len(re.findall('doi:\s+(.*?)\s', line)) > 0:
				doi.append(re.findall('doi:\s+(.*?)\s', line))
			elif len(re.findall('identifier:\s+(.*?)\s', line)) > 0:
				doi.append(re.findall('identifier:\s+(.*?)\s', line))
			elif len(re.findall('doi\s+(.*?)\s', line)) > 0:
				doi.append(re.findall('doi\s+(.*?)\s', line))
			elif len(re.findall('identifier\s+(.*?)\s', line)) > 0:
				doi.append(re.findall('identifier\s+(.*?)\s', line))
			elif len(re.findall('(http://dx\.doi\.org.*?)\s', line)) > 0:
				doi.append(re.findall('(http://dx\.doi\.org.*?)\s', line))
			#elif len(re.findall('vol', line)) > 0:
			#	doi.append(re.findall('.*vol.*', line))
		if len(doi) > 0:
			print doi[0][0]
			scholar = 'python scholar.py -c 1 -p ' + doi[0][0] + ' --citation bt | tee {}.format(path_to_cache, b, tmp_log_file )'
    		os.system(scholar)
    		output = open(tmp_log_file, 'r' ).read()
    		for l in output:
    			print l
			
		

