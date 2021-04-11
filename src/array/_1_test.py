import numpy as np
a = np.array([1,2,3])
print (a)

# student data type
# Creating a structured data type Student with string field 'name',
# integer field 'age' and float field 'marks'
student_data_type = np.dtype([('name','S20'),('age','i4'),('marks','f4')])
print(student_data_type)
#Now apply this structured data type Student on ndarray
_1d_student_array = np.array([('abc',20,90)],dtype=student_data_type)
print(_1d_student_array)
_2d_student_array = np.array([('name_1',20,91),('name_2',21,92)],dtype=student_data_type,ndmin=2)
print(_2d_student_array)