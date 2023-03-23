class points:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __add__(self,other):
        return (self.x+other.x,self.y+other.y)
    def slope(self,other):
        return(other.y-self.y)/(other.x-self.x)
p1=points(2)
p2=points(4,5)
print(p1.slope(p2))
print(p1+p2)