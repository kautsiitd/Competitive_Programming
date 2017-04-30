for i in range(input()):
    n, k = map(int, raw_input().split())
    islands = []
    ingredients = [0 for j in range(k)]
    for j in range(n):
        island = map(int, raw_input().split())[1:]
        islands.append(island)
        for ingredient in islands[j]:
            ingredients[ingredient - 1] += 1
    # doing calculation to find answer
    foundAnswer = False
    for ingredientCount in ingredients:
        if ingredientCount == 0:
            print "sad"
            foundAnswer = True
            break
    if foundAnswer:
        continue
    for island in islands:
        canSkipThisIsland = True
        for ingradient in island:
            if ingredients[ingradient - 1] < 2:
                canSkipThisIsland = False
                break
        if canSkipThisIsland:
            print "some"
            foundAnswer = True
            break
    if not foundAnswer:
        print "all"
