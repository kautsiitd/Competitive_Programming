n = input()
funcF = [map(int,raw_input().split()) for _ in range(n)]
numberOfMoves = input()
moves = [map(int,raw_input().split()) for _ in range(numberOfMoves)]
tapeUpperLimit = 100
tape = [i for i in range(n)] + [0 for i in range(n,tapeUpperLimit)]
testCases = [i for i in range(9)]

def resetTape():
    tape = [i for i in range(n)] + [0 for i in range(n,tapeUpperLimit)]

# validating Results
upperLimit = n*n
for i in testCases:
    for j in testCases:
        tape[n] = i/n
        tape[n+1] = i%n
        tape[n+2] = j/n
        tape[n+3] = j%n
        for move in moves:
            tape[move[2]] = funcF[tape[move[0]]][tape[move[1]]]
        answer = tape[n+4]*pow(n,3) + tape[n+5]*pow(n,2) + tape[n+6]*n + tape[n+7]
        if answer != i*j:
            print "Failing for: ",i,j,answer
        resetTape()
