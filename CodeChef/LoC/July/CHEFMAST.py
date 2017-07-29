numbers = '0123456789'
dict = {}
dict['00'] = ('0',0)
for a in range(1,10):
    for b in range(10):
        if a>b:
            dict[numbers[a]+numbers[b]] = (numbers[10-a+b],1)
        else:
            dict[numbers[a]+numbers[b]] = (numbers[10-a],2)
for b in range(1, 10):
    dict['0'+numbers[b]] = ('0',1)

def minMoves(num):
    if num in dict:
        return dict[num]
    first,second,remaining,ans = int(num[0]),int(num[1]),num[2:],0
    for i in range(second,first,-1):
        remaining,tempAns = minMoves(numbers[i]+remaining)
        ans+=tempAns
    for i in range(min(first,second)+1):
        remaining,tempAns = minMoves(num[0]+remaining)
        ans+=tempAns
    dict[num] = ('9'+remaining,ans)
    return dict[num]

for _ in range(input()):
    print minMoves('0'+raw_input())[1]
