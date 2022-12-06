#write a py prog to see if the triangle is equilateral triangle or scalene or isosceleces
x = int(input("Enter 1st side:"))
y = int(input("Enter 2nd side:"))
z = int(input("Enter 3rd side:"))
if (x==y==z): print("Your Triangle Is Equilateral")
elif (x!=y) and (x!=z) and (y!=z): print("Your Triangle Is Scalene")
else:print("Your Triangle is Isosceleces")