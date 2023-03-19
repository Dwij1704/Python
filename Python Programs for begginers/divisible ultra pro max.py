#write a py prog to check if the last number is divisible by 3 or not
number = int(input("Enter a number to check: "))
if (number%10)==0: print("Its Not Divisible by 3")
elif (number%10)%3==0: print("Divisible")
else:print("Its Not Divisible by 3")