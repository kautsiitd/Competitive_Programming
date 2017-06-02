for _ in range(input()):
    x,y = map(int, raw_input().split())
    print (((x+y)*(x+y+1))/2) + x + 1
