#Write a py program to use def
def wish(name):
    print("Hello",name,"Good Morning")
# name=input("Enter Your name: ")
# wish(name)
wish("Dwij")


#1. No Parameter and no return type
def printline():
    s="1. No Parameter and no return type"
    print(s)
printline()


#2. Parameter and no return type
def printline1(s1):
    print(s1)
printline1("2. Parameter And No Return Type")


#3. Parameter with return type
def printline2(s2):
    return s2
print(printline2("3. Using Print:- Parameter with Return Type"))
t=printline2("\tUsing Varialbe:- Parameter with Return Type")
print(t)


#4. No Parameter with return type
def printline2():
    s3=("4. Using Print:- No Parameter with Return Type")
    return s3
print(printline2())