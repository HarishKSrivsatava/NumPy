import numpy as np


# Basic Indexing
# Slice Object : A Python slice object is constructed by giving start, stop, and step parameters to
# the built-in slice function. This slice object is passed to the array to extract a part of array.
# slice(start: Optional[int], stop: Optional[int], step: Optional[int]=...)

a  = np.arange(10)
print(a) #[0 1 2 3 4 5 6 7 8 9]
slice = slice(0, 11, 2)
print(a[slice]) #[0 2 4 6 8]
