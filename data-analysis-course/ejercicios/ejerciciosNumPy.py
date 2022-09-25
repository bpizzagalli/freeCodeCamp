import sys
import numpy as np
print(np.__version__)

""" #Create a numpy array of size 10, filled with zeros.
zeros=np.zeros(10)
print(zeros)

#Create a numpy array with values ranging from 10 to 49
rang10to49=np.arange(10, 50)
print(rang10to49)

#Create a numpy matrix of 2*2 integers, filled with ones.
mat22=np.ones([2,2], dtype=int)
print(mat22)

#Create a numpy matrix of 3*2 float numbers, filled with ones.
mat32=np.ones([3,2], dtype=float)
print(mat32) 



X= np.arange(5, dtype=int)

#Given the X numpy array, create a new numpy array with the same shape and type as X, filled with ones.
np.ones_like(X)
print(np.ones_like(X))

#Given the X numpy matrix, create a new numpy matrix with the same shape and type as X, filled with zeros.
np.zeros_like(X)
print(np.zeros_like(X))

#Create a numpy matrix of 4*4 integers, filled with fives.
mat44=np.ones([4,4], dtype=int) * 5
print(mat44)

#Given the X numpy matrix, create a new numpy matrix with the same shape and type as X, filled with sevens.
print(np.ones_like(X) * 7)

#Create a 3*3 identity numpy matrix with ones on the diagonal and zeros elsewhere.
matident=np.identity(3, dtype=int)
print(matident) 

#Create a numpy array, filled with 3 random integer values between 1 and 10.
matrandint=np.random.randint(1, 10, size=3, dtype=int)
print(matrandint) 

#Create a 3*3*3 numpy matrix, filled with random float values.
matrandfloat=np.random.randn(3,3,3)
print(matrandfloat) 

#Given the X1 python list convert it to an Y numpy array
X1= [1,2,3,4,5,6,7,8,9]
print(X1, type(X1))
X1=np.array(X1)
print(X1, type(X1)) 

# Given the X2 numpy array, make a copy and store it on Y2.
X2=np.random.randint(1,10, size=6)
print(X2, id(X2))

Y2=np.copy(X2)
print(Y2, id(Y2)) 

#Create a numpy array with numbers from 1 to 10
to10=np.arange(1,11)
print(to10)

#Create a numpy array with the odd numbers between 1 to 10
oddnumbers=np.arange(1,11,2)
print(oddnumbers)

#Create a numpy array with numbers from 1 to 10, in descending order.
descorder=np.arange(1,11)[::-1]
print(descorder) 

#Create a 3*3 numpy matrix, filled with values ranging from 0 to 8
ranging0to8=np.arange(9).reshape(3,3)
print(ranging0to8) 

#Show the memory size of the given Z numpy matrix
Z=np.zeros((5,4))
print(Z.size * Z.itemsize, "bytes") 

#Given the X3 numpy array, show it's first element
X3=np.arange(10)
print(X3[0])

#Given the X3 numpy array, show it's last element
print(X3[-1])

#Given the X3 numpy array, show it's first three elements
print(X3[0:3])

#Given the X3 numpy array, show all middle elements
print(X3[1:-1])

#Given the X numpy array, show the elements in reverse position
print(X3[::-1])

#Given the X numpy array, show the elements in an odd position
print(X3[::2]) 

#Given the X4 numpy matrix, show the first row elements
X4=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])


print(X4[0])

#Given the X4 numpy matrix, show the last row elements
print(X4[-1])

#Given the X4 numpy matrix, show the first element on first row
print(X4[0,0])

#Given the X numpy matrix, show the last element on last row
print(X4[-1,-1])

#Given the X numpy matrix, show the middle row elements
print(X4[1:-1, 1:-1])

#Given the X4 numpy matrix, show the first two elements on the first two rows
print(X4[:2, :2]) 

#Given the X4 numpy matrix, show the last two elements on the last two rows
print(X4[1:, 1:])

#Convert the given integer numpy array to float
X5 = [-5, -3, 0, 10, 40]
X5 = np.array(X5, dtype=float)
print(type(X5))


#Reverse the given numpy array (first element becomes last)
print(X5[::-1])

#Order (sort) the given numpy array
X5.sort()
print(X5)

#Given the X7 numpy array, set the fifth element equal to 1
X6 = np.arange(0,10)
X6[4]=1
print(X6)

#Given the X7 numpy array, change the 50 with a 40
X7 = np.array([10, 20, 30, 50])
X7[3]=40

#Given the X8 numpy matrix, change the last row with all 1
X8 = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

print(X8[-1])
X8[-1] = np.array([1,1,1,1]) 

#Given the X9 numpy matrix, change the last item on the last row with a 0
X9 = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

X9[-1,-1] = 0

#Given the X10 numpy matrix, add 5 to every element
X10 = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

print(X10+5) 

prob=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(prob>=2)
print(prob[prob>=2])
print(prob.mean())
print(prob[prob < prob.mean()])
print(prob == 0)

#Given the X11 numpy array, make a mask showing negative elements
X11 = np.array([-1,2,0,-4,5,6,0,0,-9,10])
mask = X11 < 0

#Given the X12 numpy array, get the negative elements
X12 = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
print(X12[X12<0])

#Given the X13 numpy array, get numbers higher than 5
X13 = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
print(X13[X13>5])

#Given the X14 numpy array, get numbers higher than the elements mean
X14 = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
print(X14.mean())
print(X14[X14>X14.mean()]) 

#Given the X15 numpy array, get numbers equal to 2 or 10
X15 = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
mask15 = ((X15 == 2) | (X15 == 10))
print(X15[mask15])

 """

#LOGIC FUNCTIONS

#Given the X16 numpy array, return True if none of its elements is zero
X16 = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
print(X16.all())

#Given the X17 numpy array, return True if any of its elements is zero
X17 = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
print(X17.any())

#Given the X18 numpy array, show the sum of its elements
X18 = np.array([3, 5, 6, 7, 2, 3, 4, 9, 4])
print(X18.sum())

#Given the X19 numpy array, show the mean value of its elements
X19 = np.array([1, 2, 0, 4, 5, 6, 0, 0, 9, 10])
print(X19.mean())

#Given the X20 numpy matrix, show the sum of its columns
X20 = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
print(X20.sum(axis=0)) #axis=0 suma por COLUMNAS, axis=1 suma por FILAS

#Given the X21 numpy matrix, show the mean value of its rows
X21 = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
print(X21.mean(axis=1))

#Given the X22 numpy array, show the max value of its elements
X22 = np.array([1, 2, 0, 4, 5, 6, 0, 0, 9, 10])
print(X22.max())


