import numpy as np

a  = np.arange(0,60,5)
print(a) #[ 0  5 10 15 20 25 30 35 40 45 50 55]
a = a.reshape(3,4)
print(a)
"""
[[ 0  5 10 15]
 [20 25 30 35]
 [40 45 50 55]]
"""

for x in np.nditer(a):
    print(x, end = " ") #0 5 10 15 20 25 30 35 40 45 50 55


# Modifying Array Values
arr_1 = np.arange(0,60,5)
arr_1 = arr_1.reshape(3,4)
print ('Original array is:')
print ('arr_1 : ', arr_1)
"""
arr_1 :  
[[ 0  5 10 15]
 [20 25 30 35]
 [40 45 50 55]]
"""
print ('\n')
for x in np.nditer(arr_1, op_flags=['readwrite']):
   x[...] = 2*x
print ('Modified arr_1 : ', arr_1)
"""
Modified arr_1 :  
[[  0  10  20  30]
 [ 40  50  60  70]
 [ 80  90 100 110]]
"""