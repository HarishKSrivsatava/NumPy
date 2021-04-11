import numpy as np

arr = np.array([('test'),('test2')],ndmin=2)
print(arr) # [['test' 'test2']]
print('shape : ',arr.shape) # shape :  (1, 2)
print('size : ', arr.size) # size :  2

# reshape an array
b = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(b)
""" 
[[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]]
"""
print(b.shape) # (2, 6)
c = b.reshape(6,2)
print(c.shape) # (6, 2)
print(c)

# arange : Return an array with evenly spaced values within a given interval.
print(np.arange(3)) # [0 1 2]
print(np.arange(2,7)) #[2 3 4 5 6]
print(np.arange(12,step=2)) #[ 0  2  4  6  8 10]


# zeros
print(np.zeros(5)) #[0. 0. 0. 0. 0.]
print('------------------')
print(np.zeros((5,2)))
"""
[[0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]]
"""

# asarray : To create an array from existing data.
x =[1,2,3]
print(x) #[1, 2, 3]
t = np.asarray(x)
print(t) #[1 2 3]

#ndarray from list of tuples
list_of_tuples = [(1,2,3),('1','abc',3)]
print('list_of_tuples : ',list_of_tuples) #list_of_tuples :  [(1, 2, 3), ('1', 'abc', 3)]
ndarray = np.asarray(list_of_tuples)
print('ndarray_from_list_of_tuples',ndarray) #ndarray_from_list_of_tuples [['1' '2' '3']['1' 'abc' '3']]