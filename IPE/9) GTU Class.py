class GTU():
    cnt=100
    def __init__(self):
        self.x=None
        self.y=None
    def get_value(self,x,y):
        self.x=x
        self.y=y
    def print_value(self):
        print(self.x,self.y,self.cnt)
gtu=GTU()
gtu.get_value(x=10,y=20)
gtu.print_value()