#write a py prog to tax on bike
price = int(input("Enter Price the bike: "))
if(price<0):
    print("Invalid Input")
elif (price>100000):
    tax=(((price)*15)/100)
    print("Tax on Your Bike is: ",tax)
elif(price>50000):
    tax=(((price)*10)/100)
    print("Tax on Your Bike is: ",tax)
elif(price<50000):
    tax=(((price)*5)/100)
    print("Tax on Your Bike is: ",tax)