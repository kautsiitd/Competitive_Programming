n=input()
a=[];l=0
for i in range(n):
    old,new=raw_input().split()
    j=0
    while j<l:
        if old==a[j][1]:
            a[j][1]=new
            break
        j+=1
    if j==l:
        a.append([old,new])
        l+=1
print l
for i in range(l):
    print a[i][0],a[i][1]