class student:
    def __init__(self):
        pass
    def display(self):
        return "IN"
    def calc(self):
        return self.display()
obj=student()
print(obj.calc())