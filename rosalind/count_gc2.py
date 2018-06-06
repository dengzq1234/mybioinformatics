import sys

def gc_count(filename):
	file = open(filename,'r')
	gene_dict = {}

	for line in file:
	    line = line.rstrip('\n')
	    if line.startswith('>'):
	        gene = line[1:]
	        gene_dict[gene] = ''
	        seq = ''
	        #print(line)
	    else:
	        seq = seq + line
	        gene_dict[gene] = seq
	file.close()
	#print(gene_dict)
	gc_count = 0
	for gene_name,seq in gene_dict.items():
		gc_count = seq.count('C') + seq.count('G')
		gc_percent = str(float(gc_count) / float(len(seq)) * 100) +'%'
		answer = gene_name + ' ' + gc_percent
		print(answer)

if __name__ == '__main__':
	
	gc_count(sys.argv[1])