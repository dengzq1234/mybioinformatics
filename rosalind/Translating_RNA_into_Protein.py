import sys

f = open('rna_protein_code','r')
rna_protein_code = {}
for line in f:
    line = line.rstrip()
    rna_code = line.split(' ')[0]
    aa = line.split(' ')[1]
    rna_protein_code[rna_code] = aa
f.close()

def get_rna(filename):
    file = open(filename,'r')
    seq = ''
    for line in file:
        line = line.rstrip()
        seq += seq + line
    file.close()
    return seq

def rna_protein(rna_seq):
    if len(rna_seq) %3 != 0:
        raise ValueError("this sequence cannot be translated")
    else:
        pre_aa_list = [rna_seq[i:i+3] for i in range(0,len(rna_seq),3)]
        
    aa = ''
    for rna in pre_aa_list:
        if rna_protein_code[rna] != 'Stop':
            aa = aa + rna_protein_code[rna]
        else:
            break
    print(aa)
    return aa

if __name__ == '__main__':
    rna_protein(get_rna(sys.argv[1]))