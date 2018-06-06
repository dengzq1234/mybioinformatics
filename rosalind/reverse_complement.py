import sys

def reverse_complement(filename):
    with open(filename) as f:
        seq = f.readline()[:-1]

    match_dict = {'A':'T','T':'A','C':'G','G':'C'}
    reverse_seq = seq[::-1]
    reverse_complement_seq = ''
    for base in reverse_seq:
        reverse_complement_seq += match_dict[base]
    
    print(reverse_complement_seq)
    return reverse_complement_seq

if __name__ == '__main__':
	reverse_complement(sys.argv[1])