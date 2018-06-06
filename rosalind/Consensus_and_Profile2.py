import numpy as np
import sys,os
from collections import Counter

def get_file(filename):
	fhand = open(filename,'r')
	seq_dict = {}
	for line in fhand:
	    line = line.rstrip()
	    if line.startswith('>'):
	        gene = line
	        seq_dict[gene] = ''
	        continue
	    seq_dict[gene] +=line
	seq_list = list(seq_dict.values())

	a = np.array(seq_list)#创建一个二维数组
	#print(len(a)) 
	fhand.close()
	return a

def get_profile(seq_array):
	L1,L2,L3,L4 = [], [], [], []
	comsquence=''
	for i in range(len(seq_array[0])):
	    l = [x[i] for x in seq_array] #调出二维数组的每一列
	    L1.append(l.count('A'))
	    L2.append(l.count('C'))
	    L3.append(l.count('G'))
	    L4.append(l.count('T'))
	    comsquence=comsquence+Counter(l).most_common()[0][0]


	L1 = " ".join(str(x) for x in L1)
	L2 = " ".join(str(x) for x in L2)
	L3 = " ".join(str(x) for x in L3)
	L4 = " ".join(str(x) for x in L4)

	output = open('Consensus_test.txt','wt')
	
	output.write(comsquence+'\n')
	#print(comsquence)

	content = 'A: '+L1+'\n'+'C: '+L2+'\n'+'G: '+L3+'\n'+'T: '+L4
	output.write(content)
	#print('A:',L1,'\n','C:',L2,'\n','G:',L3,'\n','T:',L4)
	output.close()
	return comsquence

if __name__ == '__main__':
	seq_array = get_file(sys.argv[1])
	get_profile(seq_array)


