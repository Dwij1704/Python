import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
arr3=np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[1,2,3,4,5],[6,7,8,9,10]],[[1,2,3,4,5],[6,7,8,9,10]]])
print(arr1.ndim)
print(arr1.shape)
print(arr2.ndim)
print(arr2.shape)
print(arr3.ndim)
print(arr3.shape)

arr4=np.array([[1,2,3,4,5],[6,7,8,9,10]],ndmin=5)
print(arr4)
print(arr4.ndim)
print(arr4.shape)

arr5=np.array([1,2,3,4,5,6,7,8,9])
print(arr5)
newarr=arr5.reshape(3,3)
print(newarr)
print(newarr.base)

# for i in newarr:
#     # print(i)
#     for j in i:
#         print(j)
print("NEW ARR")
print(newarr)
for i in newarr:
    for j in i:
        print(j)
print("----------------------------------------------------------------")
for x in np.nditer(newarr):
    print(x)
print("----------------------------------------------------------------")
for x in np.nditer(newarr[0:3,::2]):
    print(x)