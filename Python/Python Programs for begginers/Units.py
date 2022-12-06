#write a py prog to check units/
unit = int(input("Enter Total Units: "))
if(unit<0):
    print("Invalid Input")
elif (unit>200):
    bill=((unit-200)*10)+(100*5)
    print(bill)
elif(unit>100):
    bill=((unit-100)*5)
    print(bill)
elif(unit<100):
    bill=0
    print(bill)

