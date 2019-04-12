#!/usr/bin/python3

class Matrix2x2():
	def __init__(self,a=0,b=0,c=0,d=0):
		if isinstance(a,(int,float)) and isinstance(b,(int,float))\
		and isinstance(c,(int,float)) and isinstance(d,(int,float)): 
			self.a=a
			self.b=b
			self.c=c
			self.d=d
		else:
			raise Exception()
	def __str__(self):
		return str(((self.a,self.b),(self.c,self.d)))
	def setMatrix(self,a=None,b=None,c=None,d=None):
		if a!=None:
			self.a=a
		if b!=None:
			self.b=b
		if c!=None:
			self.c=c
		if d!=None:
			self.d=d
	def matrixSum(self,matrix):
		r_a = self.a+matrix.a
		r_b = self.b+matrix.b
		r_c = self.c+matrix.c
		r_d = self.d+matrix.d
		return Matrix2x2(r_a,r_b,r_c,r_d)
	def matrixMuliplayScalar(self,scalar):
		if isinstance(scalar,(int,float)):
			r_a = self.a*scalar
			r_b = self.b*scalar
			r_c = self.c*scalar
			r_d = self.d*scalar
		else:
			raise Exception()
		return Matrix2x2(r_a,r_b,r_c,r_d)
	def matrixProduct(self,matrix):
		r_a = self.a*matrix.a + self.b*matrix.c
		r_b = self.a*matrix.b + self.b*matrix.d
		r_c = self.c*matrix.a + self.d*matrix.c
		r_d = self.c+matrix.b + self.d*matrix.d
		return Matrix2x2(r_a,r_b,r_c,r_d)
	def getDeterminant(self):
		return self.a*self.d-self.b*self.c
		