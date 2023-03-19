#write a py prog to convert Days 
d = int(input("Enter Days:"))
year= d//365
month= (d%365)//30
days=(d%365)%30
print("Year= "+str(year)+"\nMonth= "+str(month)+"\nDays= "+str(days))