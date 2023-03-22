class student:
    def read(self,roll,name,age,total_marks):
        self.roll=roll
        self.name=name
        self.age=age
        self.marks=total_marks
    def display(self):
        return self.roll,self.name,self.age,self.marks
    def __eq__(self,other_obj):
        if self.marks==other_obj.marks:
            return other_obj.display(),self.display()
a=student()
b=student()
a.read(1,"Dwij",18,98)
b.read(2,"Shubham",18,98)
print(a==b)