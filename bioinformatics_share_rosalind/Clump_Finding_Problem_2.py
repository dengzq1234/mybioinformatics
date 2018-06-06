import sys

def ClumpFinding(genome,k,L,t):
    results = set()
    for i in range(len(genome)-L+1):
        window = genome[i:i+L]
        counts = {}
        for j in range(len(window)-k+1):
            kmer = window[j:j+k]
            
            if kmer in counts:
                counts[kmer]+=1
            else:
                counts[kmer] = 1
        for kmer_candidate in counts:
            if counts[kmer_candidate] >= t:
                results.add(kmer_candidate)
    print(list(results))
    #print(kmer)
    return results

if __name__ == '__main__':
	f = open(sys.argv[1])
	strings = [line.rstrip('\n') for line in f]
	param = strings[1].split(' ')
	#print(param)
	ClumpFinding(strings[0],int(param[0]),int(param[1]),int(param[2]))
	f.close()
