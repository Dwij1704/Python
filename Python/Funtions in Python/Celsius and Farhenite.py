# Write a py program to convert celsius to farhenite or vice-versa
def farhenite(degree):
    print("Farhanite is : %.2f"%((9/5)*degree+32))
def celsius(degree):
    print("Celsius is : %.2f "%((degree-32)+(5/9)))
degree=int(input("Enter Temprature: "))
choice=int(input("Enter You Choice\n1. Enter 1 for celsius\n2. Enter 2 for Farhenite:"))
if choice==1:
    celsius(degree)
elif choice==2:
    farhenite(degree)
else:
    print("Enter Valid Choice")