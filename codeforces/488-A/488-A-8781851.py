x=input()
done=0
for i in range(1,100):
    if done==0:
        g=x+i
        y=str(g)
        for j in range(len(y)):
            if y[j]=='8':
                print i
                done=1
                break