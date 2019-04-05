def mult(H):
	return len(H),len(H(0))  
A=[[2,4,3],
   [3,4,5],
   [7,6,5]]
B=[[2,3],
   [4,5],
   [6,7]]
r1,c1 = mult(A)
r1,c2 = mult(B)
if c1==r2:
	result [[0,0],
		[0,0],
		[0,0]]
	for i in range(r1):
		for j in range(c2):
			for k in range(r2):
				result[i][j] += A[i][k]*B[k][j]

else:
	print('dimension not match')
for p in result:	
	print(p)
