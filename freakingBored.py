matrix=[
[11,21,31],
[12,22,32],
[13,23,33]
]
matrix2=[
[11,21,31],
[12,22,32]
]
class Matrix:
	def __init__(self, val): #set
		if(type(val)==list):
			self.val = val
		else:
			self.val=-1

	def __eq__(self, other): #comper
		return self.val == other.val

	def __repr__(self): #get
		return self.val

	def __mul__(self, other):#multiplication self * other
		if(type(self)==type(other)):
			if(len(self.val)==len(other.val[0])):
				new_matrix=[]
				for y in range(len(self.val)):
					new_matrix.append([])
					for x in range(len(other.val[0])):
						new_matrix[y].append(0)				
				for y in range(len(self.val)):
					for x in range(len(other.val[0])):
						for i in range(len(self.val[y])):
							new_matrix[y][x]+=self.val[y][i]*other.val[i][x]
				return Matrix(new_matrix)
			else:
				return Matrix([])
		else:
			return self

	def __invert__(self):
		print("kekules")

first = Matrix(matrix)
second = Matrix(matrix)
empty = first*second
~empty