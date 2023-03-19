#write a py prog to see if you are elligible for exam or not
work = int(input("Enter Working Days:"))
abs = int(input("Enter Absence:"))
if(abs<0) or(work<0):print("Your Input Is Invalid")
elif (((work-abs)/work)*100)<75:print("You are not elligible for the exams")
else:print("You are good to go")