#write a py prog to print fibonnaci series
n1=0
n2=1
n=int(input("Enter Terms= "))
if (n<=0):
    print("Enter Positive Integer")
elif(n==1):
    print(n1,end="")
else:
    print(n1,n2,end=" ")
for i in range (n-1):
    nth=n1+n2
    print(nth,end=" ")
    n1=n2
    n2=nth