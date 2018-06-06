import sys

#Clump Finding Problem
from collections import Counter
import itertools

def FrequenceWords(Text,k):
    words = []
    for i in range(len(Text)):
        word = Text[i:i+k]
        if len(word) == k:
            words.append(word)
    results = Counter(words).most_common() #it's a list of tupple
    return results

def ClumpFinding(genome, k, L, t):
    words = []
    
    for i in range(len(genome) + L):
        string_1 = genome[i:i+L]
        
        for j in string_1:
            words.append(FrequenceWords(string_1,k)) #words is a list with many sublist
    #print(words)
    final_collection = [every_set for every_set in itertools.chain(*words)] #final_collection become one big list
    #print(final_collection)
    
    result_in_window = [pattern[0] for pattern in set(i for i in final_collection if i[1] >= t)] #[0]is pattern,[1]is frequence
    return result_in_window

if __name__ == '__main__':
	f = open(sys.argv[1])
	strings = []
	for line in f:
		line = line.rstrip('\n')
		strings.append(line)
	param = strings[1].split(' ')
	#print(param)
	ClumpFinding(strings[0],int(param[0]),int(param[1]),int(param[2]))
	f.close()
