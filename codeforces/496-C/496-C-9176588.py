row,column=map(int,raw_input().split())
a=[]
ans=0
remain=[1]*column
for i in range(row):
    a.append(raw_input())
i=0
while i<row-1:
    for j in range(column):
        if ord(a[i][j])<ord(a[i+1][j]) and remain[j]==1:
            break
        if ord(a[i][j])>ord(a[i+1][j]) and remain[j]==1:
            ans+=1
            remain[j]=0
            i=-1
            break
    i+=1
print ans