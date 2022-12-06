#write a py prog to calculate Grade
att = int(input("Enter Attendance:"))
if(att<0) or(att>100):print("Your Input Is Invalid")
elif (att>=70)and(att<=100) :print("Bonus Marks are ",(15*att)/100)
elif (att>=50)and(att<70) :print("Bonus Marks are ",(10*att)/100)
elif (att>=35)and(att<50) :print("Bonus Marks are ",(5*att)/100)
elif (att>=0)and(att<35) :print("You Are Not Elligible For Bonus Marks")