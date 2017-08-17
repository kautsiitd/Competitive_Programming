import sys
def printIt(s):
    print s
    sys.stdout.flush()

def bestDisk(diskInfo):
    return diskInfo[0]/(diskInfo[3]*1.0)

n,h = map(int,raw_input().split())
hardDisksInfo = sorted([map(int,raw_input().split())+[i] for i in range(h)], key=bestDisk)
penalty = input()

numberOfHardDisk = 0
currentHardDisk = -1
userMap = {}
hardDiskMap = {}
exceed = False
hardDiskUsed = True
for _ in range(n):
    # Buying hardDisk
    currentCapacity = 0
    if numberOfHardDisk < 1050 and hardDiskUsed:
        printIt("p b "+str(hardDisksInfo[0][-1]))
        hardDiskUsed = False
        numberOfHardDisk += 1
        currentHardDisk += 1
        currentCapacity = hardDisksInfo[0][3]
    else:
        exceed = True

    # Asking query
    printIt("g")
    q = map(int,raw_input().split())
    qType = q[0]
    if qType == 0:
        userId = q[1]
        userData = q[2]
        if userData < currentCapacity and not(exceed):
            userMap[userId] = currentHardDisk
            hardDiskUsed = True
            hardDiskMap[currentHardDisk] = userId
            hardDiskMap[currentHardDisk-1] = userId
            printIt("p s "+str(currentHardDisk)+" 0")
        else:
            printIt("p s -1 -1")
    elif qType == 1:
        userId = q[1]
        userData = q[2]
        if userId in userMap:
            printIt("p i "+str(userMap[userId])+" "+str(userData))
        else:
            printIt("p i -1 -1")
    else:
        erasedHardDisk = q[1]
        if erasedHardDisk in hardDiskMap:
            erasedUser = hardDiskMap[erasedHardDisk]
            if erasedUser in userMap:
                del userMap[erasedUser]
print "end"
