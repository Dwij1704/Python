#write a py prog to Add N numbers
n=int(input("Enter Total Number= "))
sum=0
for i in range(1,n+1):
    print("Enter",i,"Number= ",end="")
    x=int(input())
    sum+=x
print("Sum=",sum)
print("Average=",sum/n)