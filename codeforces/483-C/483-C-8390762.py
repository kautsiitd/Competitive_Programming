'''f=open('input.txt')
g=open('output.txt', 'w')
nooftest=int(f.readline().strip())'''
#import cmath
import math
import time
n,k=map(int,raw_input().split())
diff=k
print 1,
a=1
m=0
while diff!=0:
    print a+(diff*(pow(-1,m))),
    a=a+(diff*(pow(-1,m)))
    diff-=1
    m+=1
i=k+2
while i<n+1:
    print i,
    i+=1