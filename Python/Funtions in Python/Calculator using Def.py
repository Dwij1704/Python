#Write a py program to make a calculator
def calc(a,b,choice):
        """**Calculator**"""
        if choice=="+":
            print("Ans",a+b)
        elif choice=="-":
            print("Ans",a-b)
        elif choice=="*":
            print("Ans",a*b)
        elif choice=="/":
            print("Ans",a/b)
        elif choice=="//":
            print("Ans",a//b)
        elif choice=="**":
            print("Ans",a**b)
        elif choice=="%":
            print("Ans",a%b)
print(calc.__doc__)
a=int(input("Enter A: "))
b=int(input("Enter B: "))
choice=input("""Enter + For Sum
Enter - For Subtraction
Enter * For Multiplication
Enter / For Division
Enter // For Flow Division
Enter ** For Power
Enter % For Modulo: """)
calc(a,b,choice)