import sys

def get_dna(filename):
    file = open(filename,'r')
    seq = []
    for line in file:
        line = line.rstrip()
        seq.append(line)

    dna = seq[0]
    k_mer = seq[1]
    print(dna)
    print(k_mer)
    return dna,k_mer

def dna_motif(dna,k_mer):
    location = ''
    count = 0
    for i in range(0,len(dna)-len(k_mer)+1):
        count +=1
        if dna[i:i+len(k_mer)] == k_mer:
            location = location + str(count) + ' '
    print(location)
    return location

if __name__ == '__main__':
	dna,k_mer = get_dna(sys.argv[1])
	dna_motif(dna,k_mer)

