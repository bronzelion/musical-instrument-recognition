#!/usr/bin/python

#expecting label as the last column
import sys
import os

from ..settings import BASE_DIR

def csvtolibsvm(instrument_label):
	ifile = os.path.join(BASE_DIR, 'testinput.csv')
	out= os.path.join(BASE_DIR, 'testinput.libsvm')
	instru = instrument_label

	fin = open(ifile,'r')
	fout =open(out,'w+')
	line = fin.readline()
	while(line != ''):
		vals=line.strip().split(',')	
		fout.write(str(vals[-1])+' ')
		#print vals

	#	if(instru == str(vals[-1])):
	#		fout.write('+1'+' ')
	#	else:
	#		fout.write('-1'+' ')
		#for i in range(2,len(vals)-1):
		#	fout.write(str(i+1-2)+':'+str(vals[i])+' ')
		#fout.write('\n')
		#line = fin.readline()

		for i in range(len(vals)-1):
			fout.write(str(i+1)+':'+str(vals[i])+' ')
		fout.write('\n')
		line = fin.readline()
