#write a py prog to calculate all operations
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
print("""1. To Add Press 1
2. To Subtract Press 2
3. To Divide Press 3
4. To Multipy Press 4
5. To F Division Press 5
6. To Modulo Press 6
7. To Power Press 7""")
choice=int(input("Enter Choice: "))
if choice==1:print("Your Sum of "+str(a)+" and "+str(b)+" is",a+b)
elif choice==2:print("Your Subtraction of "+str(a)+" and "+str(b)+" is",a-b)
elif choice==3:print("Your Division of "+str(a)+" and "+str(b)+" is",a/b)
elif choice==4:print("Your Multiplication of "+str(a)+" and "+str(b)+" is",a*b)
elif choice==5:print("Your F Division of "+str(a)+" and "+str(b)+" is",a//b)
elif choice==6:print("Your Modulo of "+str(a)+" and "+str(b)+" is",a%b)
elif choice==7:print("Your Power of "+str(a)+" and "+str(b)+" is",a**b)
else:print("Your Input Is Invalid")