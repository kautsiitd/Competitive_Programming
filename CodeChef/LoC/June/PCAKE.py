primeNumbers = [2,3,5,7,11,13,17,19,23,29,31]
primeFactors = [[[]], [[]], [[2,1]], [[3,1]], [[2,2]], [[5,1]], [[2,1],[3,1]]]

for i in range(7,1001):
    factors = []
    number = i
    for prime in primeNumbers:
        if number == 1:
            break
        else:
            power = 0
            while number%prime == 0:
                number/=prime
                power += 1
            if power != 0:
                factors.append([prime,power])
    if number != 1:
        factors.append([number,1])
    primeFactors.append(factors)

for i in range(32, 1000):
    isPrime = True
    for j in range(11):
        if i%primeNumbers[j] == 0:
            isPrime = False
            break
    if isPrime:
        primeNumbers.append(i)
numberOfPrimes = len(primeNumbers)

shouldVisit = [False,True]
for i in range(2,1001):
    visit = True
    for factor in primeFactors[i]:
        if factor[1] > 1:
            visit = False
            break
    shouldVisit.append(visit)

for _ in range(input()):
    n = input()
    a = map(int,raw_input().split())
    answer = 0
    start = 0
    end = 0
    primeCount = {}
    for prime in primeNumbers:
        primeCount[prime] = 0
    while end < n:
        number = a[end]
        if number == 1:
            answer += end - start + 1
            end += 1
        elif shouldVisit[number]:
            repetedPrimes = []
            for factor in primeFactors[number]:
                primeCount[factor[0]] += 1
                if primeCount[factor[0]] > 1:
                    repetedPrimes.append(factor[0])
            while(len(repetedPrimes) != 0):
                startNumber = a[start]
                if startNumber == 1:
                    start += 1
                    continue
                for factor in primeFactors[startNumber]:
                    primeCount[factor[0]] -= 1
                start += 1
                copyOfRepetedPrimes = []
                for prime in repetedPrimes:
                    if primeCount[prime] > 1:
                        copyOfRepetedPrimes.append(prime)
                repetedPrimes = copyOfRepetedPrimes
            answer += end - start + 1
            end += 1
        else:
            end += 1
            start = end
            primeCount = {}
            for prime in primeNumbers:
                primeCount[prime] = 0

    print answer
