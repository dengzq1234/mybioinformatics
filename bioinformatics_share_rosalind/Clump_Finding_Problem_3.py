import sys
#The Frequency Array
def SymbolToNumber(Symbol):
    if 'A' in Symbol:
        return 0
    elif 'C' in Symbol:
        return 1
    elif 'G' in Symbol:
        return 2
    elif 'T' in Symbol:
        return 3

def PatternToNumber(Pattern):
    if len(Pattern)==1:
        return SymbolToNumber(Pattern)
    else:
        symbol = Pattern[-1]
        Prefix = Pattern[:-1]
        return 4 * PatternToNumber(Prefix) + SymbolToNumber(symbol)

def NumberToSymbol(index):
    index = int(index)
    if index == 0:
        return 'A'
    elif index == 1:
        return 'C'
    elif index == 2:
        return 'G'
    elif index == 3:
        return 'T'

def NumberToPattern(index, k):
    index = int(index)
    k = int(k)
    if k == 1:
        return NumberToSymbol(index)
    else:
        prefixIndex = index//4
        r = index%4
        symbol = NumberToSymbol(r)
        return NumberToPattern(prefixIndex,k-1)+symbol

def ComputingFrequencies(Text,k):
    k = int(k)
    FrequencyArray = [0 for _ in range(4**k)]
    for i in range(len(Text)-k+1):
        fragment = Text[i:i+k]
        digital_fragment = PatternToNumber(fragment)
        FrequencyArray[digital_fragment] += 1
    return FrequencyArray

def ClumpFinding(Genome, k, L, t):
    FrequentPatterns = []
    Clump = [0 for _ in range(4**k)]
    for i in range(len(Genome)-L+1):
        Text = Genome[i:i+L]
        FrequencyArray = ComputingFrequencies(Text, k)
        for index in range(4**k):
            if FrequencyArray[index] >= t:
                Clump[index] = 1
    for i in range(4**k):
        if Clump[i] == 1:
            Pattern = NumberToPattern(i,k)
            FrequentPatterns.append(Pattern)
    print(FrequentPatterns)
    return FrequentPatterns


if __name__ == '__main__':
	f = open(sys.argv[1])
	strings = [line.rstrip('\n') for line in f]
	param = strings[1].split(' ')
	#print(param)
	ClumpFinding(strings[0],int(param[0]),int(param[1]),int(param[2]))
	f.close()
