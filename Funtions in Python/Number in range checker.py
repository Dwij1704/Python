# Write a py program to check a number in a range
def check(start,end,num):
    flag=0
    if start>end:
        for i in range(start,end,-1):
            if i==num:
                flag=1
                break
    else:  
        for i in range(start,end):
            if i==num:
                flag=1
                break
    if flag==1:
        print("Number is present")
    else:
        print("Number is not present")
num=int(input("Enter a Number: "))
start=int(input("Enter Start: "))
end=int(input("Enter End: "))
check(start,end,num) 