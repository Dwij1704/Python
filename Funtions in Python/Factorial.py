# Write a py program to print factorial
def factorial(num):
    mul=1
    for i in range(num,0,-1):
        mul=mul*i
    print("Factorial of",num,"is",mul)
num=int(input("Enter a Number: "))
if(num<0):
    print("Please Enter Positive Number")
else:
    factorial(num) 