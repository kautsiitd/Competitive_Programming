def main(k):
	l = len(k)

	left = k[: l / 2]
	center = k[l / 2] if l % 2 else ''
	right = left[: : -1]
	palin = left + center + right
	if palin > k:
		return palin
	if center:
		if center != '9':
			center = str(int(center) + 1)
			palin = left + center + right
			return palin
		else:
			center = '0'
	if left == '9' * (l / 2):
		palin = '1' + '0' * (l - 1) + '1'
		return palin
	t = list(left)
	p = l / 2 - 1
	while t[p] == '9':
		t[p] = '0'
		p -= 1
	t[p] = str(int(t[p]) + 1)
	left = ''.join(t)
	right = left[: : -1]
	palin = left + center + right
	return palin

if __name__ == "__main__":
	for _ in xrange(int(raw_input())):
		k = raw_input()
		print main(k)
