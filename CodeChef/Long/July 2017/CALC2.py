for _ in range(input()):
    totalEnergy, secondConsumption = map(int, raw_input().split())
    if secondConsumption >= totalEnergy:
        print 0
        continue
    else:
        factor = (totalEnergy/2)/secondConsumption
        cPoint1 = secondConsumption*factor
        cPoint2 = secondConsumption*(factor + 1)
        cPoint3 = secondConsumption*(factor + 2)

        answer = 0
        if cPoint1 < totalEnergy:
            answer = max(answer, factor*(totalEnergy - cPoint1))
        if cPoint2 < totalEnergy:
            answer = max(answer, (factor + 1)*(totalEnergy - cPoint2))
        if cPoint3 < totalEnergy:
            answer = max(answer, (factor + 2)*(totalEnergy - cPoint3))

        print answer
