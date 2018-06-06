import sys

def make_file(filename):
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
	return gene_dict

def gc_count(gene_dict):
    gc_count = 0
    for gene_name,seq in gene_dict.items():
        gc_count = seq.count('C') + seq.count('G')
        gc_percent = str(float(gc_count) / float(len(seq)) * 100) +'%'
        answer = gene_name + ' ' + gc_percent
        print(answer)
        #print(gc_count)
    return answer

if __name__ == '__main__':
	
	gc_count(make_file(sys.argv[1]))