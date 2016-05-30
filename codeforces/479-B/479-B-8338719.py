'''f=open('input.txt')
g=open('output.txt', 'w')
nooftest=int(f.readline().strip())'''
#import cmath
import math
nooftest=1
for i in range(nooftest):
    n,k=map(int,raw_input().split())
    array=map(int,raw_input().split())
    s=0
    for j in range(n):
        s+=array[j]
    new=[]
    lol=[]
    avg=s/n
    for j in range(n):
        lol.append([array[j],j])
    lol.sort(key=lambda x:x[0])
    for j in range(n):
        new.append(s/n)
    remain=s%n
    j=n-1
    while remain!=0:
        new[j]+=1
        remain-=1
        j-=1
    '''noofmove=0
    j=n-1
    contri=[]
    while array[j]>new[j]:
        noofmove+=array[j]-new[j]
        contri.append(array[j]-new[j])
        j-=1'''
    ans=[]
    diff=lol[n-1][0]-lol[0][0]
    noofmove=0
    while k!=0 and (lol[n-1][0]!=new[n-1] or lol[0][0]!=new[0]):
        lol[0][0]+=1
        lol[n-1][0]-=1
        ans.append([lol[n-1][1],lol[0][1]])
        #print "lolb",lol
        lol.sort(key=lambda x:x[0])
        #print "lola",lol
        diff=lol[n-1][0]-lol[0][0]
        k-=1
        noofmove+=1
    print diff,noofmove
    j=0
    for j in range(len(ans)):
        print ans[j][0]+1,ans[j][1]+1
#g.close()