#!/usr/bin/python3
import numpy
import os

r=int(input("Enter the row of 1st & 2nd matrix :"))
c=int(input("Enter the column of 1st & 2nd matrix :"))
ui = int(input("Enter the element of 1st matrix :"))
ar1 = numpy.full((r,c),ui)
ui1 = int(input("Enter the element of 2nd matrix :"))
ar2 = numpy.full((r,c),ui1)

print ("The sum of matrices are :")
Darray = ar1+ar2
print(Darray)

store = input ("Will you want to store the output .....Ans:yes or no")
if store == 'yes' :
	file_path ="/home/"+os.getlogin()+"/"+input("Enter where you want to store eg.Desktop): ")
	if file_path:
		numpy.savetxt(file_path+"/Addition_of_matrix.txt",Darray,fmt="%i",delimiter=" ")
		print ("file successfully saved")
	else:
		numpy.savetxt("/Addition_of_matrix.txt",Darray,fmt="%i", delimeter=" ")
else :
	print ("Thanks for using")
