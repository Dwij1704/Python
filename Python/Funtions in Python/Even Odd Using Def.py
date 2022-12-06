#Write a py program to identify whether the number is even or odd
def check(num):
    if num%2==0:
        # print("Number is Even")
        return 1
    else:
        # print("Number is Odd")
        return 0
num=int(input("Enter number: "))
result=check(num)
if result==1:
    print("Even")
else:
    print("Odd")