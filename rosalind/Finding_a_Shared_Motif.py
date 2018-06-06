import sys

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

	
	#print(len(a)) 
	fhand.close()
	return seq_list

def longest_common_substr(strings):
    
    short_string = strings[0]
    other_strings = strings[1:]

    l = len(short_string)
    m = ''
    for i in range(0, l):
        for j in range(l, i + len(m), -1):
            s1 = short_string[i:j]

            matched_all = True
            for s2 in other_strings:
                if s1 not in s2:
                    matched_all = False
                    break

            if matched_all:
                m = s1
                break
    print(m)
    return m

if __name__ == '__main__':
	seq_list = get_file(sys.argv[1])
	longest_common_substr(seq_list)