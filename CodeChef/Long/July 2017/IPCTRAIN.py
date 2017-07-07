import Queue
import heapq

for _ in range(input()):
    n,d = map(int, raw_input().split())
    daywisePeople = sorted([map(int, raw_input().split()) for i in range(n)])
    peopleIndex = 0
    sadnessQueue = []
    for dayIndex in range(1,d+1):
        while peopleIndex < n and daywisePeople[peopleIndex][0] <= dayIndex:
            heapq.heappush(sadnessQueue, (-daywisePeople[peopleIndex][2],daywisePeople[peopleIndex]))
            peopleIndex += 1

        if not sadnessQueue:
            continue

        topPriorPerson = heapq.heappop(sadnessQueue)[1]
        if topPriorPerson[1] != 1:
            topPriorPerson[1] -= 1
            heapq.heappush(sadnessQueue,(-topPriorPerson[2],topPriorPerson))

    answer = 0
    while sadnessQueue:
        person = heapq.heappop(sadnessQueue)[1]
        answer += person[1]*person[2]

    print answer
