def findMax(num):
    ans = 0
    while num != 0:
        ans = max(ans,num%10)
        num /= 10
    return ans

for _ in range(input()):
    num = input()
    moves = 0
    while num != 0:
        num -= findMax(num)
        moves += 1
    print moves
