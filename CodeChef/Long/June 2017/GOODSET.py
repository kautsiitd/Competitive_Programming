answer = [1,2,4]
for i in range(1,100):
    answer.append(4 + (3*i))
for _ in range(input()):
    n = input()
    for i in range(n):
        print answer[i],
    print ""
