class stackqueue:
    def __init__(self,li):
        self.stackque=li
    def shift(self):
        print(self.stackque.pop(0))
    def unshift(self,num):
        self.stackque.append(0)
        self.stackque=[num]+self.stackque[0:-1]
    def push(self,num):
        self.stackque.append(0)
    def pop(self):
        print(self.stackque.pop())
    def display(self):
        print(self.stackque)
st=stackqueue([0,1,2,3,4])
st.shift()
st.unshift(10)
st.push(10)
st.pop()
st.display()