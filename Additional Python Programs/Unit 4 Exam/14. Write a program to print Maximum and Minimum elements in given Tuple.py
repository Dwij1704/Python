# 14. Write a program to print Maximum and Minimum elements in given Tuple
tup=(1,2,3,4,5,6,7,8,9)
max=tup[0]
min=tup[0]
for i in tup:
    if max<i:
        max=i
    if min>i:
        min=i
print("Minimun is",min,"Maximun is",max)