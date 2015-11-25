#!/usr/bin/python

import sys, getopt
from count_fn import count_fn
from frequent_patterns import frequent_patterns


def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:k:")
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -k <k-mer length>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -k <k-mer length>'
         sys.exit()
      elif opt in ("-i"):
         inputfile = arg
      elif opt in ("-k"):
         k_mer_ln = arg


   try:
      int(k_mer_ln)>0
      print 'Length of k-mer is '+ k_mer_ln+' bp'
   except:
      print 'Using default k-mer length 10 bp'

   if (len(inputfile))>0:
      print 'Using DNA inputfile: '+inputfile
   else:
      print 'Using default inputfile: input_DNA.txt'

   print 'hehe'

   file_name='input_DNA.txt'
   hand=open(file_name)
   p=hand.read()
   hand.close()

   print len(p)


if __name__ == "__main__":
   main(sys.argv[1:])
