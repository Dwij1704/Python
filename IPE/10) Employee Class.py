class employee:
    def read(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary
    def display(self):
        print(self.name,self.department,self.salary)
a=employee()
a.read("Dwij","A.I Engineer","Infinite xD:)")
a.display()