f=open("4) File.txt","r")
l1=f.readlines()
print("Number Of Lines are",len(l1))
new=""
for i in l1:
    new=new+" "+i.rstrip("\n")
l1=new.upper().split(" ")
each=dict()
print("Unique Occurence are:",end="")
for i in range(len(l1)):
    flag=0
    for j in range(i+1,len(l1)):
        if l1[i]==l1[j]:
            flag=1
    if flag!=1:
        print(l1[i],end=" ")
    each[i+1]=l1[i]
print("\nDictionary of Every Word:",each)