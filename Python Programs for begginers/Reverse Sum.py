#write a py prog to sum the reverse number
n = int(input("Enter a number: "))
sum=0
while n!=0:
    digit=n%10
    sum=sum+digit
    n=n//10
print(sum)