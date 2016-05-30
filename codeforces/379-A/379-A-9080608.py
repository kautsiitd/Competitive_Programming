a,b=map(int,raw_input().split())
ans=a
wasteold=a%b
aold=a/b
while aold>0:
    ans+=aold
    wastenew=(aold+wasteold)%b
    anew=(aold+wasteold)/b
    aold=anew
    wasteold=wastenew
print ans