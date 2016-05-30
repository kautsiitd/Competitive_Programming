'''f=open('input.txt')
g=open('output.txt', 'w')
nooftest=int(f.readline().strip())'''
#import cmath
#import math
nooftest=1
for i in range(nooftest):
    a=input()
    b=input()
    c=input()
    print max(a+b+c,a*(b+c),c*(a+b),a*b*c,a*b+c,c*b+a)
#g.close()