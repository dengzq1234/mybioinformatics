import sys

def get_seq(filename):
    seq_dict = {}
    f = open(filename,'r')
    for line in f:
        line = line.rstrip()
        if line.startswith('>'):
            gene = line[1:]
            seq_dict[gene] = ''
            seq = ''
        else:
            seq = seq + line
            seq_dict[gene] = seq
    f.close()
    seq_list = list(seq_dict.values()) 
    return seq_list

def seq_profile(seqlist):
    n = len(seqlist[0])
    profile = {'A':[0]*n,'C':[0]*n,'T':[0]*n,'G':[0]*n}
    for seq in seqlist:
        for index,base in enumerate(seq):
            profile[base][index] +=1
    

    bestseqs = [[]]
    for i in range(n):
        d = {N:profile[N][i] for N in "ACGT"}
        m = max(d.values())
        l = [N for N in ['T','G','C','A'] if d[N] == m]
        bestseqs = [ s+[N] for N in l for s in bestseqs ]
    
    for s in bestseqs:
        print(''.join(s))
        
    for key, value in profile.items():
        print(key,':', " ".join([str(x) for x in value] ))
    
    return


if __name__ == '__main__':
    seqlist = get_seq(sys.argv[1])
    seq_profile(seqlist)

	