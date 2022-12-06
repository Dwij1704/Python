#write a py prog to find Greater number out of 3
a=int(input("Enter Value of A: "));
b=int(input("Enter Value of B: "));
c=int(input("Enter Value of C: "));
if(a>b):
    if(a>c):print("A is Greater")
    else:print("C is Greater")
elif(b>c):print("B is Greater")
else:print("C is Greater")