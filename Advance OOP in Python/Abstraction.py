from abc import ABC,abstractmethod
# print(dir())
class shapes(ABC):
    def __init__(self,shapename):
        self.name=shapename
    @abstractmethod
    def drawcircl(self):
        pass
    def circle1(self):
        pass
class circle(shapes):
    def __init__(self,shape_name):
        super().__init__(shape_name)
    # def drawcircle(self):
    #     print("Drawing circle")
    def drawcircl(self):
        print("Drawing circle2")
a=circle("Circle")
a.drawcircl()
class Mammal():

	def __init__(self, name):
		print(name, "Is a mammal")

class canFly(Mammal):

	def __init__(self, canFly_name):
		print(canFly_name, "cannot fly")

		# Calling Parent class
		# Constructor
		super().__init__(canFly_name)
	def display(self, canFly_name):
		print(canFly_name, "cannot fly")

		# Calling Parent class
		# Constructor
		super().__init__(canFly_name)

class canSwim(Mammal):

	def __init__(self, canSwim_name):

		print(canSwim_name, "cannot swim")

		super().__init__(canSwim_name)

class Animal(canFly, canSwim):

	def __init__(self, name):
		super(canFly,self).display(name)

# Driver Code
Carol = Animal("Dog")
