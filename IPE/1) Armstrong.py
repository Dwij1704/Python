#Write a py program to identify whether the number is Armstrong or not
def check(num):
    a=num
    sum=0
    l=len(str(a))
    while a>0:
        digit=a%10
        sum=sum+(digit**l)
        a=a//10
    if sum==num:
        print("Number is Armstrong")
    else:
        print("Number is not armstrong")
num=int(input("Enter number: "))
check(num)