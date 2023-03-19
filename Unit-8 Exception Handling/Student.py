class data:
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def enter_inputs(self):
        for i in range(3):
            self.marks.append(int(input("Enter Marks for %s for Subject %d: "%(self.name,i+1))))
    def display(self):
        print("Data of",self.name,":")
        count=1
        for i in self.marks:
            print("Subject",count,"Marks:",i)
            count+=1
d1=data("Dwij")
d1.enter_inputs()
d1.display()