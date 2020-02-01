The python file lab2.py reads two arrays from an input file an performs a simple matrix multiplication on the matricies. The results of the multiplication are printed to an output file. 

input file information: 
The input file has all the values for each of the matricies, the values for each of the matricies are seperated by a space. The contenets of the first matrix are at the begining of the file followed by the contents of the second matrix. 

reading the matrix values from the file: (lines 15-46)
The way I chose to read the values from the file is line by line with the .readline() function. I then extracted the elements that I needed with the .split() function, spliting at a space. I used a variable "y" (line 16) to seperate the first matrix from the second matrix. The contents were stored in two seperate 2D list's "a" and "b". When I stored the values I had to cast the type from string to integer so that I could later perform the matrix multiplication. 

writing to a file: (lines 70-96)
When writing the product of the matrix multiplication to the output file I needed to convert the values stored in the 2D list from integer back to string. I used the .write() function to write the contents to the output file.    
