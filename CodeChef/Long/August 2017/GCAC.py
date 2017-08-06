for _ in range(input()):
    numCandidates,numCompanies = map(int,raw_input().split())
    minSalaries = map(int,raw_input().split())
    maxCandidates = []
    remainOffers = []
    packages = []
    for i in range(numCompanies):
        a,b = map(int,raw_input().split())
        packages.append((a,i))
        maxCandidates.append(b)
        remainOffers.append(b)
    packages = sorted(packages,reverse=True)
    hMatrix = [raw_input() for __ in range(numCandidates)]

    studentSelected = 0
    total = 0
    companyGotNothing = 0

    for i in range(numCandidates):
        for j in range(numCompanies):
            k = packages[j][1]
            if hMatrix[i][k] == '1' and remainOffers[k] > 0 and packages[j][0] >= minSalaries[i]:
                remainOffers[k] -= 1
                studentSelected += 1
                total += packages[j][0]
                break

    for i in range(numCompanies):
        if maxCandidates[i] == remainOffers[i]:
            companyGotNothing += 1

    print studentSelected,total,companyGotNothing
