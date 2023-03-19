#write a py prog to determine whether the number is an armstrong or not
n = int(input("Enter a number: "))
a=n
sum=0
len=len(str(n))
while n!=0:
    digit=n%10
    sum=sum+(digit**len)
    n=n//10
if sum==a:
    print("""Your 
    number is
     armstrong 
     number""")
else:
    print("Your number is not an armstrong number")