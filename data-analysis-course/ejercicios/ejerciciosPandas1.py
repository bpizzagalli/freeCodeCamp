import sys
import numpy as np
import pandas as pd

print(pd.__version__)

### Create an empty pandas Series
pd.Series()

### Given the X python list convert it to an Y pandas Series
X = ['A','B','C']
print(X, type(X))
Y= pd.Series(X)
print(Y, type(Y))

### Given the X1 pandas Series, name it 'My letters'
X1 = pd.Series(['A','B','C'])
X1.name = 'My letters'
print(X1) 

### Given the X2 pandas Series, show its values
X2 = pd.Series(['A','B','C'])
print(X2.values) 

### Assign index names to the given X3 pandas Series
X3 = pd.Series(['A','B','C'])
index_names = ['first', 'second', 'third']
X3.index = index_names
print(X3) 

### Given the X4 pandas Series, show its first element
X4 = pd.Series(['A','B','C'], index=['first', 'second', 'third'])
print(X4[0])
print(X4.iloc[0])
print(X4['first']) 

### Given the X5 pandas Series, show its last element
X5 = pd.Series(['A','B','C'], index=['first', 'second', 'third'])
print(X5[-1])
print(X5.iloc[-1])
print(X5['third']) 

### Given the X6 pandas Series, show all middle elements
X6 = pd.Series(['A','B','C','D','E'],
              index=['first','second','third','forth','fifth'])

print(X6[1], X6[2], X6[3])
print(X6.iloc[1:-1])
print(X6[1:-1])

### Given the X pandas Series, show the elements in reverse position
X7 = pd.Series(['A','B','C','D','E'],
              index=['first','second','third','forth','fifth'])
print(X7.iloc[::-1])
print(X7[::-1]) 

### Given the X8 pandas Series, show the first and last elements
X8 = pd.Series(['A','B','C','D','E'],
              index=['first','second','third','forth','fifth'])
print(X8[['first','fifth']])
print(X8.iloc[[0, -1]])
print(X8[[0, -1]]) 

### Convert the given integer pandas Series to float
X9 = pd.Series([1,2,3,4,5],
              index=['first','second','third','forth','fifth'])
pd.Series(X9, dtype=float)
print(type(X9))

### Reverse the given pandas Series (first element becomes last)
X10 = pd.Series([1,2,3,4,5],
              index=['first','second','third','forth','fifth'])
print(X10[::-1])
print(X10.iloc[::-1]) 

### Order (sort) the given pandas Series
X11 = pd.Series([4,2,5,1,3],
              index=['forth','second','fifth','first','third'])
print(X11.sort_values())

### Given the X12 pandas Series, set the fifth element equal to 10
X12 = pd.Series([1,2,3,4,5],
              index=['A','B','C','D','E'])
X12[4] = 10
print(X12)

### Given the X13 pandas Series, change all the middle elements to 0
X13 = pd.Series([1,2,3,4,5],
              index=['A','B','C','D','E'])
X13[1:-1]=0
print(X13)  

### Given the X14 pandas Series, add 5 to every element
X14 = pd.Series([1,2,3,4,5])
print(X14+5) 

### Given the X15 pandas Series, make a mask showing negative elements
X15 = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])
mask= X15[X15 <= 0]
print(mask) 

### Given the X16 pandas Series, get the negative elements
X16 = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])
print(X16[X16 <= 0])

### Given the X17 pandas Series, get numbers higher than 5
X17 = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])
print(X17[X17 > 5]) 

### Given the X18 pandas Series, get numbers higher than the elements mean
X18 = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])
print(X18.mean())
print(X18[X18 > X18.mean()]) 

### Given the X19 pandas Series, get numbers equal to 2 or 10
X19 = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])
mask1=(X19 == 2) | (X19 == 10)
print(X19[mask1]) 

### Given the X20 pandas Series, return True if none of its elements is zero
X20 = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])
print(X20.all())

### Given the X21 pandas Series, return True if any of its elements is zero
X21 = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])
print(X21.any()) 

### Given the X pandas Series, show the sum of its elements
X22 = pd.Series([3,5,6,7,2,3,4,9,4])
print(X22.sum())

### Given the X23 pandas Series, show the mean value of its elements
X23 = pd.Series([1,2,0,4,5,6,0,0,9,10])
print(X23.mean())

### Given the X pandas Series, show the max value of its elements
X24 = pd.Series([1,2,0,4,5,6,0,0,9,10])
print(X24.max())