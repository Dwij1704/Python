class employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def get_all(self):
        return self.name,self.age,self.salary
    def set_name(self,a):
        self.name=a
        
        
class car:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
    def display(self):
        print("Car is",self.name,"colour is",self.colour)

class sum:
    def __init__(self,a,b):
        self.sum=a+b
    def display(self):
        print(self.sum)
        
        
        
        
class prac:
    var=10
    print(var)
    def pra(self,var):
        self.var=var
        print(var)
a1=prac()
print(a1.var)
a1.var=5
print(a1.var)




print(car("BMX","Green"))
c1=car("Mercedes","Black")
c1.display()
del c1 #Destructor


s1=employee("Dwij",18,100000)
print(s1.get_all())
s1.set_name("Shubham")
print(s1.get_all())
del s1

d1=sum(45,55)
d1.display()