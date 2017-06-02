for _ in range(input()):
    n = input()
    rowA = raw_input()
    rowB = raw_input()
    answer = 0

    if rowA != "."*n and rowB != "."*n:
        answer += 1
    
