w=open("prac.txt","w")
w.write("Hello")
w.close()

r=open("prac.txt","r") #Default is Read mode
# r.seek(0)
print(r.read())
r.close()

r1=open("prac.txt","r+")
# print(r1.read())
# r1.seek(0)
r1.write("dw")
r1.seek(0)
print(r1.read())
r1.seek(0)
r1.write("He")
r1.close()

w1=open("prac.txt","a+")
# print(w1.read())
w1.write("\nI am Dwij")
w1.seek(0)
print(w1.read())
w1.close()

read=open("prac.txt","r")
print(read.read(5))
read.seek(0)
print(read.readline())
print(read.readline())
read.seek(0)
print(read.readlines()) #List
read.seek(0)
l=read.readlines()
print(l[0])
print(l[1])
l[1]="I am Shubham Jain"
# l=read.writelines("Hello")
# print(l)
read.close()

write=open("prac.txt","w+")
write.writelines(l)
write.seek(0)
print(write.read())