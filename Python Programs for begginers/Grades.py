#write a py prog to calculate Grade
marks = int(input("Enter Marks:"))
if(marks<0) or(marks>100):print("Your Input Is Invalid")
elif (marks>=80)and(marks<=100) :print("Distinction")
elif (marks>=60)and(marks<=79) :print("First Class")
elif (marks>=35)and(marks<=59) :print("Second Class")
elif (marks<=34):print("Failed")