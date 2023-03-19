file=open("sum.txt","r+")
li=file.readlines()
file.close
file=open("sum.txt","w")
print(li)
for i in li:
    if i[0]=="#":
        continue
    if "#" in i:
        ind=i.index("#")
        file.write(i[0:ind])
        continue
    file.write(i)