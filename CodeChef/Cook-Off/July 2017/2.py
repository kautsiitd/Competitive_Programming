import bisect

squares = [i*i for i in range(1,1000005)]

a,b = map(int,raw_input().split())

answer = 0
for x in range(1,a+1):
    answer += bisect.bisect(squares,x*x + b) - bisect.bisect(squares,x*x)

print answer
