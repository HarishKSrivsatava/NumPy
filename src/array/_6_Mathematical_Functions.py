import numpy as np

# Trigonometric Functions
a = np.array([0,30,45,60,90])
print('Sine of different angles')
# Convert degree into radians by multiple with pi/180
a = a*np.pi/180
print('Sine values : ', np.sin(a))
# Sine values :  [0.         0.5        0.70710678 0.8660254  1.        ]
print('Cosine values : ', np.cos(a))
# Cosine values :  [1.00000000e+00 8.66025404e-01 7.07106781e-01 5.00000000e-01   6.12323400e-17]
print('Tangent values : ', np.tan(a))
# Tangent values :  [0.00000000e+00 5.77350269e-01 1.00000000e+00 1.73205081e+00   1.63312394e+16]


# Rounding Function
arr_test = np.array([1.0,5.55, 123, 0.567, 25.532])
print('arr_test : ',arr_test)
# arr_test :  [  1.      5.55  123.      0.567  25.532]
arr_tes_2 = np.around(arr_test, decimals=1)
print('Array after rounding off : ', arr_tes_2)
# Array after rounding off :  [  1.    5.6 123.    0.6  25.5]
