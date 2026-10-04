def sum(k):
	if k>0:
		return sum(k-1)+k
	return 0

print(sum(5))