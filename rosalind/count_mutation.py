import sys

def count_mutation(filename):
    file = open(filename,'r')
    seq = []
    for line in file:
        line = line.rstrip()
        seq.append(line)

    s1 = seq[0]
    s2 = seq[1]
    different =[ i for i in range(len(s1)) if s1[i] != s2[i]]
    print(len(different))
    return len(different)

if __name__ == '__main__':
	count_mutation(sys.argv[1])