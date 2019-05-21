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

from matrix import Matrix


def main():
	
	m2x2 = Matrix(-2,1,0,-2)
	print(m2x2)
	print(m2x2[0,0])
	m2x2[1,0] = 3
	print(m2x2)

	m1 = Matrix(1,2,3,4,5,6,7,8,9)
	m2 = Matrix(9,8,7,6,5,4,3,2,1)
	print(m1)

	m5x5 = Matrix(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
	print(m5x5)

	print(m1.matrixSum(m2))
	print(m1.matrixAddScalar(10))
	print(m1.matrixMuliplayScalar(3))

	print(m1.matrixMultiplayCorrespondingElements(m2))
	print(m1.matrixProduct(m2))

	print(m2x2.getDeterminant())
	print(m1.getDeterminant())
	print(m5x5.getDeterminant())

if __name__ == '__main__':
	main()

