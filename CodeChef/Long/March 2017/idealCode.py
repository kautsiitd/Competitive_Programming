t = int(raw_input())
for i in range(t):
	n,k = map(int,raw_input().split())
	a, k1, k2 = raw_input(), 0, 0
	b, c, d = a[0], 1, []
	for e in a[1:]:
		if b == e: c += 1
		else: d.append(c); b, c = e, 1
	d.append(c)
	if k == 0: print max(d); continue

	for b in a: k1, k2 = k2 + int(b != '0'), k1 + int(b == '0')
	if min(k1, k2) <= k: print 1; continue

	lo, hi= 2, max(d)
	while lo < hi:
		mid = (lo+hi)//2
		if sum([y//(mid+1) for y in d]) > k : lo = mid + 1
		else: hi = mid
	print lo
