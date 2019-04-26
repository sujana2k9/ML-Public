import numpy as np
'''a=np.array([2,3,6,7,8], dtype=int)
print(a)
b=np.array((2,3,4,5), dtype=int)
print(b)
print(a[0])
print(b[0])
b[0]=8
print(b)
b=np.array((2,3,4,5), dtype=int)
c=np.exp(b)
print(c)
print(b[1])'''
d= np.array([[1,2,3,4,5,6,7], [4,5,6,7,8,9,2], [1,2,3,4,5,6,7], [4,5,6,7,8,9,2]], dtype=int)
print(d)
print(d[1,2])
print(d[[[0],[1]],[1,3,4]])
print (d[[[0], [1], [3]], [0, 2]])
print(d[3][1]) #same as below
print(d[3,1]) # same as above line
print(d[1:3],)
print(d[1:3,1:3])
