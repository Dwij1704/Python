#write a py prog to determine and add Odd And Even Numbers
n=int(input("Enter Total Number= "))
evensum=0
oddsum=0
even=0
odd=0
for i in range(1,n+1):
    print("Enter",i,"Number= ",end="")
    x=int(input())
    if x%2==0:
        evensum+=x
        even+=1
    else:
        oddsum+=x
        odd+=1
print("Total even number are",even,"and the sum is",evensum)
print("Total odd number are",odd,"and the sum is",oddsum)