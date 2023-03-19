a=10
# b=0
b=5
try:
    d=a/b
except:
    print("Exception")
else:
    print(d)
finally:
    print("Program Complete")



try:
    l=[1,2,3]
    l[100]=20
except Exception as e:
    print(e)

try:
    f=open("abc.txt","r+")
except FileNotFoundError as b:
    print("File not found")
    print(b)

try:    
    print(m)
except NameError as a:
    print("Invalid name")
    print(a)
    
try:    
    print(m)
except (NameError,IndexError,SyntaxError,FileNotFoundError,ZeroDivisionError) as e:
    print(e)

# Syntax Error occurs directly it does not catch the error:-
# try:
#     if{
#         print("Hi")
#     }
# except:
    # print("Error")
   



# List of errors:--
# (ArithmeticError,
# AttributeError,
# Exception,
# EOFError,
# ImportError,
# IndentationError,
# IndexError,
# KeyError,
# NameError,
# SyntaxError,
# TypeError,
# ValueError,
# ZeroDivisionError)



# Name Error:
# a=5
# if a<4:
#     b=0
# print(b)


# Unbound Local Error: Parent is Name Error:--
# def fun(a):
#     if a<5:
#         b=a
#     print(b)
# fun(5)
class jodd(Exception):
    def __init__(self,arg):
        self.msg=arg
money=10000
withdraw=9000
try:
    balance=money-withdraw
    if balance<=2000:
        raise jodd("Insufficient Balance")
    print(balance)
except jodd as e:
    print(e)


money=10000
withdraw=9000
try:
    balance=money-withdraw
    if balance<=2000:
        raise NameError("Insufficient Balance")
    print(balance)
except NameError as e:
    print(e)



money=10000
withdraw=9000
balance=money-withdraw
if balance<=2000:
    raise jodd("Insufficient Balance")
    print(balance)