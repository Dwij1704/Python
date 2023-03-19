f1=open("4) File.txt","r")
f2=open("5) Emplyee full Name.txt","r")
l1=f1.readlines()
l2=f2.readlines()
f3=open("6) File.txt","w")
for i in range(len(l1)):
    f3.write(l1[i]+l2[i])