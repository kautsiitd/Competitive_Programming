h=raw_input()
a=raw_input()
t=input()
aa=[]
ha=[]
for i in range(100):
    aa.append(0)
    ha.append(0)
for i in range(t):
    time,team,number,card=raw_input().split()
    if team=='a':
        if (aa[int(number)]==1 or card=='r')and(aa[int(number)]!=-1):
            aa[int(number)]=-1
            print a,int(number),int(time)
        else:
            if(aa[int(number)]!=-1):
                aa[int(number)]=1
    else:
        if (ha[int(number)]==1 or card=='r')and(ha[int(number)]!=-1):
            ha[int(number)]=-1
            print h,int(number),int(time)
        else:
            if(ha[int(number)]!=-1):
                ha[int(number)]=1