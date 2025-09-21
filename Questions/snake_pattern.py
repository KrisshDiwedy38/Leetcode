matrix = 	[[1,2,3],
		      [4,5,6],
		      [7,8,9]]

n = len(matrix)

for i in range(n):
	if i % 2 == 0:
		for j in range(n):
			print(matrix[i][j],end = " ")
	else:
		for j in range(n-1, -1, -1):
			print(matrix[i][j], end= " ")


# Output = 1,2,3,6,5,4,7,8,9

