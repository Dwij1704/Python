#write a py prog to check if the number is prime or not
number = int(input("Enter a number to check:"))#7
flag=0
for i in range(2,number):
    if number%i==0:
        flag=1
        break
    i+=1
if flag==1:
    print("Number Is Not Prime")
else:
    print("Number is prime")
