from fractions import gcd
t = input()
if(t==1):
	print -1
else:
	if(t==2):
		x1,y1 = map(int, raw_input().split())
		x2,y2 = map(int, raw_input().split())
		if(x1!=x2 and y1!=y2):
			print abs(x2-x1)*abs(y2-y1)
		else:
			print -1
	if(t==3):
		x1,y1 = map(int, raw_input().split())
		x2,y2 = map(int, raw_input().split())
		x3,y3 = map(int, raw_input().split())
		print max(abs(x2-x1)*abs(y2-y1),abs(x3-x1)*abs(y3-y1),abs(x3-x2)*abs(y3-y2))
	if(t==4):
		x1,y1 = map(int, raw_input().split())
		x2,y2 = map(int, raw_input().split())
		x3,y3 = map(int, raw_input().split())
		x4,y4 = map(int, raw_input().split())
		print max(abs(x2-x1)*abs(y2-y1),abs(x3-x1)*abs(y3-y1),abs(x3-x2)*abs(y3-y2))