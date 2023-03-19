class india:
    def capital(self):
        print("New Delhi")
    def lang(self):
        print("Hindi")
    def type(self):
        print("Developing")
class usa:
    def capital(self):
        print("Washington DC")
    def lang(self):
        print("English")
    def type(self):
        print("Developed")

# Longer Way!
ind=india()
us=usa()
ind.capital()
ind.lang()
ind.type()
print()
us.capital()
us.lang()
us.type()
print("\nEasier Way:")
# Easier Way!!
# It uses tuple and gives output, list,set can be used
for country in (ind,us):
    country.capital()
    country.lang()
    country.type()
    print()
    
# Function method to diplay output
def all(obj):
    obj.capital()
    obj.lang()
    obj.type()
all(ind)
all(us)
print()

# Inheritance:-
# Single
# Multiple
# Multi level
# hybrid
# Hirerchial

# Single:
class parent():
    def func1(self):
        print("parent")
class child(parent):
    def func2(self):
        print("child")
kid=child()
papa=parent()
kid.func1()
kid.func2()
print()

# Concepts:
class animal:
    def penguin(self):
        print("Penguin is animal")
    def bat(slef):
        print("Mamal")
class bird(animal):
    def penguin(self):
        print("It is a bird")
class mamals(animal):
    def bat(self):
        print("Bird")
animals=animal()
birds=bird()
mamal=mamals()
animals.penguin()
animals.bat()
birds.penguin()
mamal.bat()
print()


# Method Overloading:
class A:
    def add(self,a,b,c):
        s=a+b+c
        print(s)
    def add(self,a,b,c=0):
        s=a+b
        print(s)
class B:
    def add(self,a=None,b=None,c=None):
        if (a!=None and b!=None and c!=None):
            print(a+b+c)
        else:
            print(a+b)
    def add2(self,*args):
        sum=0
        for i in args:
            sum+=i
        print(sum)
A().add(10,20)
A().add(10,20)        
B().add(10,20)        
B().add(10,20,30)     
B().add("Hello","3")  
B().add2(10,20,30,40,10,20,30,40)
print()


# Method Overiding:
class mom:
    def cook(self):
        print("Cooking")
    def dance(self):
        # Overriden
        print("Dancing")
class daughter(mom):
    def dance(self):
        print("Daughter Dacin")
d=daughter()
d.dance()
print()

# Better Understanding
class A:
    def func1(self):
        print("Method of A")
    def func2(self):
        # Overriden
        print("Method of A")
class B(A):
    def func2(self):
        print("Method of A overidden by B")
    def func3(self):
        print("Method of B")
d=B()
d.func1()
d.func2()
d.func3()
print()


# Hybrid:
class parent():
    def func1(self):
        print("OK")
class child():
    def func2(self):
        print("No")
class child2(parent,child):
    def func3(self):
        print("Yes")
kid=child()
kid2=child2()
papa=parent()
papa.func1()
kid.func2()
kid2.func1()
kid2.func2()
kid2.func3()
print()



# Hirerchial:
class parent():
    def func1(self):
        print("OK")
class child(parent):
    def func2(self):
        print("No")
class child2(parent):
    def func2(self):
        print("Yes")
class child3(child,child2):
    def func3(self):
        print("Not sure")
kid=child()
kid2=child2()
kid3=child3()
papa=parent()
kid.func1()
kid.func2()
kid2.func1()
kid2.func2()
kid3.func1()
kid3.func2()
kid3.func3()
print()
class A:
    # print(" In class A")
    def __init__(self):
        pass
    def display(self):
        self.a=10
        print("IN A")
        print(self.a)
        
class B(A):
    def rk(self):
        print(" In class B")
    def display(self):
        print("B")
class C(A):
    def rk(self):
        print("In class C")
    # def display(self):
    #     print("C")
# classes ordering
class D(B, C):
    def __init__(self):
        # print(super(C,self).display())
        # super(A,self).display()
        disp=super(C,self)
        print(disp)
        # print(disp.display())
        # disp.display()
        # print(disp.display())
D()