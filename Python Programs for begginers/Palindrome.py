#write a py prog to check if number is palindrome
n = int(input("Enter a number: "))
rev=0
a=n
while n!=0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if(rev==a):
    print("Number Is Palindrome")
else:
    print("Number Is Not Palindrome")