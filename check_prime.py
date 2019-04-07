def prime(i):
	for k in range(2,i):
		if i%k==0:
			return False
	else:
		return True
a=[2,4,5,6,7,8,9,55,87]
print(a)
h=list(map(prime,a))
print(h)
