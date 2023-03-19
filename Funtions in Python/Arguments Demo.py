#1. Use Of Arguments
print("1. Arguments:-")
def printline(a=10):
    print(a*a)
printline(20)
printline()
print()
print()
# 2. Positional Argument
print("2. Positional Argument:-")
def wish(name,msg):
    print("Hello",name,msg)
wish("Aryan","Good Morning")
print()
print()
#3. Keyword Argument
print("3. Keyword Argument:-")
def wish1(name,msg):
    print("Hello",name,msg)
wish1(name="Aryan",msg="Good Morning")
wish1(msg="Good Morning",name="Aryan")
print()
print()
#4. Hybrid Argument
print("4. Hybrid Argument:-")
def wish2(name,msg):
    print("Hello",name,msg)
wish2("Aryan",msg="Good Morning")
    # wish2(name="Aryan","Good Morning") Positional Error
print()
print()
#5. Variable Length Argumen
print("5. Variable lenght argument:-")
print("(i) * Non Keyword example:-")
def f1(n1,*s):
    print(n1)#first parameter will be stored in n1
    print(s)#tuple data type
f1(10,20,30)
print()
print("(ii) ** Keyword example:-")
def f2(n1,**s):#** is keyword argument and * is non keyword argument
    for key,value in s.items():
        print(key,"=",value)
f2("Geek",mid="for",last="Geeks")