#write a py prog to find area of and volume of a Cylinder
import math
h = int(input("Enter Height:"))
r = int(input("Enter Radius:"))
print("The Area Of A Cylinder With Height "+str(h)+" and Radius "+str(r)+" is "+str(2*math.pi*r*r+2*math.pi*r*h)+" And its Volume is ",math.pi*r*r*h)