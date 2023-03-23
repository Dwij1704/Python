class employee:
    def get_info(self,sal,work):
        self.sal=sal
        self.work=work
    def addSal(self):
        if self.sal<500:
            self.sal+=10
    def addWork(self):
        if self.work>6:
            self.sal+=5
    def display(self):
        self.addSal()
        self.addWork()
        print(self.sal)
emp=employee()
emp.get_info(300,8)
emp.display()