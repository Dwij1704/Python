# 5. Write a Python Program to print the largest even and largest odd number in a list.
li=[x for x in range(0,11)]
maxeven=0
maxodd=0
for i in li:
    if i%2==0:
        if i>maxeven:
            maxeven=i
    else:
        if i>maxodd:
            maxodd=i
print(maxodd,maxeven)