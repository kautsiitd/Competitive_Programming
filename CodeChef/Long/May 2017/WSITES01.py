def find_match(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    if len1 == 1 and string1[0] != string2[0]:
        return string1
    minLen = min(len1, len2)
    answer = ""
    i = 0
    while i < minLen:
        if string1[i] == string2[i]:
            answer += string1[i]
        else:
            break
        i += 1
    if answer == string1:
        return None
    elif answer == string2:
        answer += string1[i]
        return answer
    else:
        answer += string1[i]
        return answer

unblockedSites = []
blockedSites = []
for i in range(input()):
    sign, word = raw_input().split()
    if sign == '+':
        unblockedSites.append(word)
    else:
        blockedSites.append(word)
unblockedSites.sort()
blockedSites.sort()

answers = []
if len(unblockedSites) == 0:
    for i in range(len(blockedSites) - 1):
        if blockedSites[i][0] != blockedSites[i+1][0]:
            answers.append(blockedSites[i][0])
    answers.append(blockedSites[-1][0])
    print len(answers)
    for answer in answers:
        print answer
elif len(blockedSites) == 0:
    print 0
else:
    blockedMaxIndex = len(blockedSites)
    unblockedWordIndex = 0
    unblockedMaxIndex = len(unblockedSites)

    answerExist = True
    bigUnblockedWordIndex = 0
    for blockedWord in blockedSites:
        while answerExist and bigUnblockedWordIndex < unblockedMaxIndex and unblockedSites[bigUnblockedWordIndex] < blockedWord:
            bigUnblockedWordIndex += 1
        if bigUnblockedWordIndex != 0:
            match = find_match(blockedWord, unblockedSites[bigUnblockedWordIndex - 1])
            if match == None:
                answerNotExist = False
                break
            else:
                answers.append(match)
        if bigUnblockedWordIndex != unblockedMaxIndex:
            match = find_match(blockedWord, unblockedSites[bigUnblockedWordIndex])
            if match == None:
                answerNotExist = False
                break
            else:
                answers.append(match)


    if answerExist:
        answers.sort()
        l = len(answers)
        finalAnswer = []
        for i in range(l-1):
            if find_match(answers[i], answers[i+1]) != None:
                finalAnswer.append(answers[i])
        finalAnswer.append(answers[-1])
        print len(finalAnswer)
        for i in finalAnswer:
            print i
    else:
        print -1
