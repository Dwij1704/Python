#write a py prog to Find Factorial numbers
a=int(input("Enter the number= "))
mul=1
if(a<0):
    print("Please Enter Positive Number")
else:
    for i in range(a,0,-1):
        mul=mul*i
        print(i,end="*")
    print("=",mul)
    