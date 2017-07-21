import Queue

for _ in range(input()):
    n,m = map(int,raw_input().split())
    s = raw_input()
    tempCount = 1
    pq = Queue.PriorityQueue()
    for i in range(1,n):
        if s[i] != s[i-1]:
            if pq.empty():
                pq.put((-tempCount,"Left"))
            else:
                pq.put((-tempCount,"Middle"))
            tempCount = 1
        else:
            tempCount += 1
    if pq.empty():
        pq.put((-tempCount,"LeftRight"))
    else:
        pq.put((-tempCount,"Right"))

    for i in range(m):
        if pq.empty():
            break
        top = pq.get()
        print top
        if top[0] == -1:
            break
        elif top[0] == -2:
            if top[1] == "Middle":
                pq.put(top)
                break
            else:
                continue
        else:
            leftPartValue = -(((-top[0])/2) - 1 + ((-top[0])%2))
            rightPartValue = -((-top[0])/2)
            if top[1] == "Middle":
                pq.put((leftPartValue,"Middle"))
                pq.put((rightPartValue,"Middle"))
            elif top[1] == " Left":
                pq.put((leftPartValue,"Left"))
                pq.put((rightPartValue,"Middle"))
            elif top[1] == "Right":
                pq.put((leftPartValue,"Middle"))
                pq.put((rightPartValue,"Right"))
            else:
                pq.put((leftPartValue,"Left"))
                pq.put((rightPartValue,"Right"))

    if pq.empty():
        print 1
    else:
        print -pq.get()[0]
