for _ in range(input()):
    totalEnergy, secondConsumption = map(int, raw_input().split())
    leftPoints = 0
    remainEnergy = totalEnergy
    answer = 0
    while remainEnergy >= secondConsumption:
        answer = max(answer, (remainEnergy/secondConsumption)*leftPoints)
        remainEnergy -= 1
        leftPoints += 1
    print answer
