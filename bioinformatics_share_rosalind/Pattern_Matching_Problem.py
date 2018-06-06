import sys

def PatternMatch(pattern,genome):
    start_point = []
    l = len(pattern)
    
    for i in range(len(genome)-l+1):
        if genome[i:i+l] == pattern:
            start_point.append(i)
    start_point = [str(i) for i in start_point]
    answer = " ".join(start_point)
    print(answer)
    return start_point



if __name__ == '__main__':
	file = open(sys.argv[1],'r')
	genome = file.read().rstrip('\n')
	PatternMatch(sys.argv[2],genome)

