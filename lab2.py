# Name: Edgar Martinez 
# Course: EE 355
# Date: 01/19/19

import time

# open the input file in read mode 
file1 = open('input.txt', 'r')

# initialize the list that will store the elements of our matricies
a = [ [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0] ]
b = [ [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0] ]
c = [ [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0] ]

# y is used to seperate the first matrix from the second matrix 
y = 0
matrix_size = 8

for x in range(matrix_size + 1):
	
	if (y < matrix_size):
 
		# read a single line from the file
		# extract the needed elements 
		file_line = file1.readline()
		hold = file_line.split()

		# store the elements of the matrix in the first 2D list
		
		for z in range(matrix_size):
			a[x][z] = int(hold[z])			

		y = y + 1

	else:
	
		for z in range(matrix_size):
			
			file_line = file1.readline()
			hold = file_line.split()

			# store the elements in the second 2D list
			
			for m in range(matrix_size):
				b[z][m] = int(hold[m])

# close the input file and open the output file 
file1.close()
file2 = open('output.txt', 'w')
file3 = open('output_time.txt', 'w')

# perform the matrix multiplication 

start = time.time()

for i in range(matrix_size): 
	
	for j in range(matrix_size):
		
		for k in range(matrix_size):
			
			c[i][j] +=  a[i][k] * b[k][j]

end = time.time()
total_time = str(end - start)

file3.write(total_time)
file3.close()

# convert all the elements in c from int to string 

for i in range(matrix_size):
	
	for j in range(matrix_size):
		
		c[i][j] = str(c[i][j])

# write the contents of c to the output file 
index = 0 

for items in c: 
	
	for x in items: 

		if(index < 7):
			file2.write(x)
			file2.write(" ")
			index = index + 1

		else:
			file2.write(x)
			file2.write(" ")
			file2.write("\n")
			index = 0

file2.close()
