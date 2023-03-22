from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def display(self):
        pass

class Maruti(Car):
    def display(self):
        print("Maruti display()")

class Santro(Car):
    def display(self):
        print("Santro display()")

m = Maruti()
m.display()
s = Santro()
s.display()