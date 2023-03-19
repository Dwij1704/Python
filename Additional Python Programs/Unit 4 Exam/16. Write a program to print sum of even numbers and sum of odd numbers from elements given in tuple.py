# 15. Write a program to print even numbers from given tuple.
tup=(1,2,3,4,5,6,7,8,9)
odd=0
even=0
for i in tup:
    if i%2==0:
        even+=i
    else:
        odd+=i
print("Total sum of Odd are",odd,"and Total sum of Even are",even)