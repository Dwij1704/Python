# 2. Write a Python program to add two given lists using map and lambda.
num1=[1,2,3,4,5]
num2=[1,2,3,4,5]
result=list(map(lambda x,y:x+y,num1,num2))
print(result)