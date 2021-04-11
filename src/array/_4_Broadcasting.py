import numpy as np


arr_1 = np.array([1,2,3,4])
arr_2 = np.array([10,20,30,40])
result = arr_1 * arr_2
print(result) #[ 10  40  90 160]

a = np.array([[0.0, 0.0, 0.0], [10.0, 10.0, 10.0], [20.0, 20.0, 20.0], [30.0, 30.0, 30.0]])
b = np.array([1.0, 2.0, 3.0])

print('First array:')
print (a)
print('\n')
"""
First array:
[[ 0.  0.  0.]
 [10. 10. 10.]
 [20. 20. 20.]
 [30. 30. 30.]]
"""
print('Second array:')
print(b)
print('\n')
"""
Second array:
[1. 2. 3.]
"""

print('First Array + Second Array')
print(a + b)
"""
First Array + Second Array
[[ 1.  2.  3.]
 [11. 12. 13.]
 [21. 22. 23.]
 [31. 32. 33.]]
"""