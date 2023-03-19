f=open("remove_new_line.txt","r+")
lines=f.readlines()
new=""
for i in lines:
    new=new+" "+i.rstrip("\n")
f.close()
f=open("remove_new_line.txt","w")
f.write(new)