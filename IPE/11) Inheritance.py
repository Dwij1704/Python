class A:
    def dispA(self):
        print("I am in A")
class B:
    def dispB(self):
        print("I am in B")
class C(A,B):
    def dispC(self):
        print("I am in c")
c=C()
c.dispA()
c.dispB()
c.dispC()