t=input()
for i in range(t):
    a=raw_input()
    ans=0
    b=[0]*13
    for j in range(1,13):
        if 12%j!=0:
            continue
        for l in range(j):
            done=1
            for k in range(12/j):
                if a[(k*j)+l]=='O':
                    done=0
                    break
            if done==1:
                b[j]=1
                ans+=1
                break
    print ans,
    for j in range(12,0,-1):
        if b[j]==0:
            continue
        temp=str(12/j)+"x"+str(j)
        print temp,
    print ""