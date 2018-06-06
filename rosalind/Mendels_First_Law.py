import sys

k = float(input('How many individuals are homozygous dominant:'))
m = float(input('How many individuals are heterozygous:'))
n = float(input('How many individuals are homozygous recessive:'))


def p(k,m,n):
    total = k+m+n
    pro = (4*n*(n-1) + 2*n*m + 2*n*m + m*(m-1))/(4*total*(total-1))
    return 1-pro

probability = p(k,m,n)
print(' The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele is '+str(probability))