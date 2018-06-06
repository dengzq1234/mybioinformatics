import sys

def dna_to_rna(filename):
	with open(filename) as f:
		dna = f.readline()[:-1]

	rna = dna.replace('T','U')
	print(rna)
	return rna

if __name__ == '__main__':
	dna_to_rna(sys.argv[1])