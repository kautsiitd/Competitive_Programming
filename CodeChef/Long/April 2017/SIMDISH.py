for i in range(0,input()):
	a = raw_input().split()
	b = raw_input().split()
	count = 0
	for j in a:
		if count > 1:
			break
		for k in b:
			if j == k:
				count +=1
			if count > 1:
				print "similar"
				break
	if count < 2:
		print "dissimilar"
