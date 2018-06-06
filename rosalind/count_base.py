import sys

def count_base(filename):
    
    with open(filename) as f:
        text = f.readline()[:-1]
    
    count_dict = {}
    for base in text:
        if base in count_dict:
            count_dict[base] += 1
        else:
            count_dict[base] = 1
    print(count_dict)
    return count_dict

if __name__ == '__main__':
    count_base(sys.argv[1])
