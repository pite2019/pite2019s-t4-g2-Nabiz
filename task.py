#Write a library that contains a class that can represent any 2𝑥2 real matrice. 
#Include two functions to calculate the sum and product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
#Examples:
#
# matrix_1 = Matrix(4,5,6,7)
# matrix_2 = Matrix(2,2,2,1)
#
# matrix_3 = matrix_2.add(matrix_1)
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#(If you want you can expand implementation to NxN matrix.)
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

#!/usr/bin/python3

from matrix import Matrix2x2


def main():
	
	m1 = Matrix2x2(1,2,3,4)
	m2 = Matrix2x2(4,3,2,1)
	m3 = m1.matrixSum(m2)
	print(m3)
	m4 = m1.matrixProduct(m2)
	print(m4)
	print(m1.getDeterminant())
	print(m1.matrixMuliplayScalar(3))

if __name__ == '__main__':
	main()

