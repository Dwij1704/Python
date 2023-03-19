# 6. Write a Python program to swap first and last element of the list.
l1=[x for x in range(0,11)]
l1[0]=l1[-1]
l1[-1]=l1[0]-l1[-1]
print(l1)