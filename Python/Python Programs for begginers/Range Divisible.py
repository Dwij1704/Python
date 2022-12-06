#write a py prog to enter a range and a divisible number
a=int(input("Enter Start= "))
b=int(input("Enter Stop= "))
n=int(input("Enter number to be divisible= "))
count=0
for i in range(a+1,b):
    if(i%n==0):
        print(i,end=" ")
        count+=1
    
print("Total Numbers=",count)