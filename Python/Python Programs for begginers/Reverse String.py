#write a py prog to reverse a string
b=input("Enter a String= ")
a=[""]
count=0
for i in b:
    a.append(str(i))
    count=count+1
while count>=0:
    print(a[count],end="")
    count=count-1