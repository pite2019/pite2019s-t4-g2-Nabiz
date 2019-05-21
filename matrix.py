#!/usr/bin/python3
from math import sqrt
import copy

class Matrix():
	
	def __init__(self,*args):
		self.dimension = int(sqrt(len(args)))	
		self.matrix = [[args[j] for j in range(i*self.dimension,i*self.dimension+self.dimension) ]\
					  for i in range(self.dimension)]
		
	def __str__(self):
		string = ''
		for line in self.matrix:
			string += str(line) + '\n'
		return string

	def __setitem__(self,tup,item):
		i,j = tup
		self.matrix[i][j] = item

	def __getitem__(self,tup):
		i,j = tup
		return self.matrix[i][j]
	
	def matrixSum(self,matrix):
		if self.dimension != matrix.dimension:
			raise Exception()
		else:
			result = copy.deepcopy(self)
			for i in range(self.dimension):
				for j in range(self.dimension):
					result[i,j] += matrix[i,j]
			return result
	
	def matrixAddScalar(self,scalar):
		result = copy.deepcopy(self)
		for i in range(self.dimension):
			for j in range(self.dimension):
				result[i,j] += scalar
		return result
	
	def matrixMuliplayScalar(self,scalar):
		result = copy.deepcopy(self)
		for i in range(self.dimension):
			for j in range(self.dimension):
				result[i,j] *= scalar
		return result
	
	def matrixMultiplayCorrespondingElements(self,matrix):
		if self.dimension != matrix.dimension:
			raise Exception()
		else:
			result = copy.deepcopy(self)
			for i in range(self.dimension):
				for j in range(self.dimension):
					result[i,j] *= matrix[i,j]
			return result

	def matrixProduct(self,matrix):
		if self.dimension != matrix.dimension:
			raise Exception()
		else:
			result = Matrix(*[0 for _ in range(self.dimension*self.dimension)])
			for i in range(self.dimension):
				for j in range(self.dimension):
					for k in range(self.dimension):
						result[i,j] += self[i,k] * matrix[k,j]
			return result
	
	def getDeterminant(self):
		if self.dimension == 2:
			return self[0,0]*self[1,1] - self[0,1]*self[1,0]
		elif self.dimension == 3:
			result = self[0,0]*self[1,1]*self[2,2]
			result += self[0,1]*self[1,2]*self[2,0]
			result += self[0,2]*self[1,0]*self[2,1]
			result -= self[0,2]*self[1,1]*self[2,0]
			result -= self[0,1]*self[1,0]*self[2,2]
			result -= self[0,0]*self[1,2]*self[2,1]
			return result
		else:
			return 'I am too week to do calculate determinant for dimension greater than 3'
		