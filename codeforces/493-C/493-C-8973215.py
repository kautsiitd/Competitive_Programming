a=input()
aa=map(int,raw_input().split())
b=input()
ba=map(int,raw_input().split())
aa.sort()
ba.sort()
pa=0
pb=0
cd=0
md=0
na=a
nb=b
while pa<a or pb<b:
    if pa<a and (pb>=b or aa[pa]<ba[pb]):
        pa+=1
        cd-=1
    elif pb<b and (pa>=a or aa[pa]>ba[pb]):
        pb+=1
        cd+=1
        if cd>md:
            md=cd
            na=a-pa
            nb=b-pb
    else:
        pa+=1
        pb+=1
ans=str((na*3)+((a-na)*2))+":"+str((nb*3)+((b-nb)*2))
print ans