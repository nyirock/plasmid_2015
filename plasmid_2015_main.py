#!/usr/bin/python

import sys, getopt, os
from count_fn import count_fn
from frequent_patterns import frequent_patterns


def main(argv):
	inputfile = ''
	file_name = ''
	k_mer_arg=''
	default_file_name='input_DNA.txt'
	k_mer_ln=10 #default value for the length of the pattern
	try:
		opts, args = getopt.getopt(argv,"hi:k:")
	except getopt.GetoptError:
	    print 'Usage: '+os.path.basename(__file__)+ ' -i <inputfile> -k <k-mer length>'
	    sys.exit(2)
	for opt, arg in opts:
	  if opt == '-h':
		 print 'Usage: '+os.path.basename(__file__)+ ' -i <inputfile> -k <k-mer length>'
		 sys.exit()
	  elif opt in ("-i"):
		inputfile = arg
	  elif opt in ("-k"):
		k_mer_arg = arg

	if (len(inputfile))>0:
		file_name=inputfile
		print 'Using DNA inputfile: '+inputfile
	else:
		file_name=default_file_name
		print 'Using default inputfile: '+file_name
	
	try:
		int(k_mer_arg)>0
		k_mer_ln=int(k_mer_arg)
		print 'Length of k-mer is '+ str(k_mer_ln)+' bp'
	except:
		print 'Using default k-mer length of '+str(k_mer_ln) + ' bp'



	#print type(os.path.basename(__file__))

	
	#file_name='input_DNA.txt'
	try:
		hand=open(file_name)
	except:
		print "Error! The specified file could not be opened. Using the defile input file option: "+default_file_name
		hand=open(default_file_name)
	dataset=hand.read()
	hand.close()

	#Cleaning the data
	dataset_cln=dataset

	dataset_cln=dataset_cln.strip().upper()
	dataset_lst=dataset_cln.split('\n')
	dataset_cln=''.join(dataset_lst)
	
	#print len(dataset)
	print 'We are working with the dataset of '+ str(len(dataset_cln))+' characters....'
	#print k_mer_ln
	if len(dataset_cln) > k_mer_ln:
		results=frequent_patterns(dataset_cln,k_mer_ln)
	else:
		print "\nError! k-mer length should be less than number of characters in the DNA dataset"
		print "Please try changing the input parameters"		
		return
		
		
#	print results
	if max(results.values())==1:
		print "No motif occurs more than once. Please try changing the input parameters"
	elif len(results)==1:
		print '\n'+'Single most frequent pattern found'+'\n'
		print str(k_mer_ln)+" bp motif "+results.keys()[0]+" occurs "+str(results.values()[0])+" times in the input DNA sequence"
	elif len(results)>1:
		print '\n'+'No single most frequent pattern found'+'\n'
		for item in results:
			print str(k_mer_ln)+" bp motif "+item+" occurs "+str(results[item])+" times in the input DNA sequence"
	else:
		print "No results found. Please try changing the input parameters"
		


if __name__ == "__main__":
   main(sys.argv[1:])