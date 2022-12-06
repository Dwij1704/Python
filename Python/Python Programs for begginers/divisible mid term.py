#write a py prog to check if the mid number is divisible by 3 or not
number = int(input("Enter a number to check if mid term is divisible or not: "))
len=len(str(number))
if len==3:
    if ((number%100)//10)%3==0: print("Divisible")
    else:print("Its Not Divisible by 3")
else:
    print("Invalid Input")