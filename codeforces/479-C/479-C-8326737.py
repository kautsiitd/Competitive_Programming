'''f=open('input.txt')
g=open('output.txt', 'w')
nooftest=int(f.readline().strip())'''
#import cmath
import math
nooftest=1
for i in range(nooftest):
    n=input()
    array=[]
    for j in range(n):
        array.append(map(int,raw_input().split()))
    array.sort(key=lambda x:x[0])
    last=min(array[0])
    for j in range(1,n):
        if array[j-1][0]==array[j][0]:
            last=max(array[j][1],last)
        elif last<=array[j][1]:
            last=array[j][1]
        else:
            last=array[j][0]
    print last
#g.close()