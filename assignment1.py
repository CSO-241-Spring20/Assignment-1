def read_matrix(filename):
	with open(filename, "r") as f:
		matrix = f.readlines()
		for i,row in enumerate(matrix):
			matrix[i] = list(map(int,matrix[i].split(",")))
	return matrix

def write_matrix(filename, solved_matrix):
	with open(filename, "w") as f:
		f.writelines(','.join(str(j) for j in i) + '\n' for i in solved_matrix)
	print(filename+" for backtracking generated.")

class sudoku():
	def __init__(self, filename):
		self.matrix = read_matrix(filename)

	def solve(self):
		''' WRITE YOUR CODE HERE
			self.matrix contains the 2-D sudoku array.
			Entries having zero need to filled in.
			You can create additional functions that will support this main bactracking function.
		'''

	def solve_without_backtracking(self):
		''' WRITE YOUR CODE HERE
			Fill in this function using any algorithm other than backtracking.
			You can implement CSP or any other algo.
		'''

		'''END YOUR CODE HERE'''
		raise NotImplementedError("You need to fill the non-backtracking function") 

if __name__=="__main__":
	su = sudoku("data.txt")
	su.solve()
	write_matrix("sol.txt", su.matrix)
	try:
		su = sudoku("data.txt")
		su.solve_without_backtracking()
		print("Solved sudoku matrix without backtracking:")
		for i in range(9):
			print(*su.matrix[i], sep=" ")
	except Exception as e:
		print(e)



