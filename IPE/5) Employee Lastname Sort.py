f=open("5) Emplyee full Name.txt","r")
l1=f.readlines()
new=""
for i in l1:
    new=new+i.split(" ")[2]
new=new.split("\n")
new.sort()
f.close()
f=open("5) Emloyee Last name.txt","w")
for i in new:
    f.write(i+"\n")