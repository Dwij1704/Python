#write a py prog to determine wage
age=int(input("Enter Age:"))
gender=input("Enter Gender:")
days=int(input("Enter Days:"))
if (age<18) or (age>40):print("Enter Valid Age")
if gender!="M" and gender!="F":print("Enter Valid Gender")
elif age>=18 and age<30:
    if gender=="M":print("Your Wage is ",days*700)
    else:print("Your Wage is ",days*750)
elif age>=30 and age<40:
    if gender=="M":print("Your Wage is ",days*800)
    else:print("Your Wage is ",days*850)