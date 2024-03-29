from typing import List

class Solution:
	def setZeroes(self, matrix: List[List[int]]) -> None:
		R, C = len(matrix), len(matrix[0])
		rowZero = False

		
		for r in range(R):
			for c in range(C):
				if matrix[r][c] == 0:
					matrix[0][c] = 0
					if r > 0:
						matrix[r][0] = 0
					else:
						rowZero = True	

		for r in range(1, R):
			for c in range(1, C):
				if matrix[0][c] == 0 or matrix[r][0] == 0:
					matrix[r][c] = 0

		if matrix[0][0] == 0:
			for r in range(R):
				matrix[r][0] = 0
		if rowZero:
			for c in range(C):
				matrix[0][c] = 0
