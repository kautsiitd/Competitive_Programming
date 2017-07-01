import math
for _ in range(input()):
	b,ls = map(int,raw_input().split())
	print round(math.sqrt(ls*ls - b*b), 5), round(math.sqrt(b*b + ls*ls), 5)
