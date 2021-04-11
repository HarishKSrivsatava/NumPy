import numpy as np

arr_1 = np.arange(9, dtype=np.float).reshape(3,3)
print('First array : ', arr_1)
"""
First array :  
[[0. 1. 2.]
 [3. 4. 5.]
 [6. 7. 8.]]
"""
arr_2 = np.array([10,10,10])
print('Second Array : ',arr_2)
"""
Second Array :  [10 10 10]
"""
result = arr_1 +arr_2
print(result)
"""
[[10. 11. 12.]
 [13. 14. 15.]
 [16. 17. 18.]]
"""
result_2 = np.add(arr_1,arr_2)
print(result_2)
"""
[[10. 11. 12.]
 [13. 14. 15.]
 [16. 17. 18.]]
"""


a = np.array([0.25, 1.33, 1, 0, 100])
print ('Our array is:', a)
# Our array is: [  0.25   1.33   1.     0.   100.  ]
print ('After applying reciprocal function:')
print (np.reciprocal(a))
# [4.        0.7518797 1.              inf 0.01     ]
b = np.array([100], dtype = int)
print('The second array is:',b) # The second array is: [100]
print('After applying reciprocal function:')
print(np.reciprocal(b)) # [0]
"""
C:/Harish/Learning/NumPy/src/array/_7_Arithmetic_Operations.py:35: 
RuntimeWarning: divide by zero encountered in reciprocal
  print (np.reciprocal(a))
"""
