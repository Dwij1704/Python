# Computation class:
# 1 - Create a Coputation class with a default constructor
# (without parameters) allowing to perform
# various calculations on integers numbers.
# 2 - Create a method called Factorial() which allows to calculate the factorial of
# integer. Test the method by instantiating the class.
# 3 - Create a method called Sum() allowing to calculate the sum of the first n
# integers 1 + 2 + 3 + .. + n. Test this method.
# 4 - Create a method called testPrim() in the Calculation
# class to test the primality of a given integer. Test this method.
# 4 - Create a method called testPrims() allowing to test if
# two numbers are prime between them.
# 5 - Create a tableMult() method which creates and displays
# the multiplication table of a given integer.
# Then create an allTablesMult() method to display all the
# integer multiplication tables 1, 2, 3, ..., 9.
# 6 - Create a static listDiv() method that gets all
# the divisors of a given integer on new list called Ldiv.
# Create another listDivPrim() method that gets all
# the prime divisors of a given integer.
class computation:
    def __init__(self):
        pass
    def factorial(self,n):
        j=1
        for i in range(1,n+1):
            j=j*i
        return j
    def sum(self,n):
        sum=0
        for i in range(1,n+1):
            sum+=i
        return sum
    def testPrim(self,n):
        flag=0
        for i in range(1,n+1):
            if n%i==0:
                flag+=1
        if flag>2:
            return False
        else:
            return True
    def testPrims(self,n,m):
        flag=0
        for i in range(1,n+1):
            if n%i==0 and m%i==0:
                flag+=1
        if flag!=1:
            return False
        else:
            return True
    def mul_table(self,n):
        for i in range(1,10):
            print(i,"x",n,"=",i*n)
    def all_mul_table(self):
        for i in range(1,10):
            for j in range(1,10):
                print(i,"x",j,"=",i*j)
    def list_div(self,n):
        li_div=[]
        for i in range(1,n+1):
            if n%i==0:
                li_div.append(i)
        return li_div
    def list_div_prime(self,n):
        li_div=[]
        for i in range(1,n+1):
            if (n%i==0 and self.testPrim(i)):
                li_div.append(i)
        return li_div
Comput= computation ()
Comput.testPrims (13, 7)
print ("List of divisors of 18:", Comput.list_div (18))
print ("List of prime divisors of 18:", Comput.list_div_prime (18))
Comput.all_mul_table ()