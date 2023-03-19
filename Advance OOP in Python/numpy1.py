import numpy as np
import sys
s=range(1000)
print("Size of each element of list in bytes",sys.getsizeof(s))
print("Size of whole list in bytes",sys.getsizeof(s)*len(s))
d=np.array([[["hehehehe1","hehehehe2","hehehehe3"]]])
print(d[0,0,2:][-1][-1])
print(d.ndim)
n1=np.array([1,2,3,4,5,6,7,8,9,10])
n2=np.where(n1%2==0)
print(type(n2))
print(n2)
print(n2[0])
for x in n2[0]:
    print(x)