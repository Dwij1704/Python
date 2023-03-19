#Write a py program to identify whether the number is odd in a range
def check(num):
    count=0
    for i in range(1,num+1):
        if i%2!=0:
            print(i,"Is an odd number")
            count+=1
    print("Total Odd Numbers are",count)
num=int(input("Enter number: "))
check(num)