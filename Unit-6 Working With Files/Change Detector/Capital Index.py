f1=open("capital.txt","r+")
f2=open("capital2.txt","r+")
l1=f1.readlines()
l2=f2.readlines()
for i in range(len(l1)):
    if l1[i]==l2[i]:
        continue
    for j in range(len(l1[i])):
        if l1[i][j]!=l2[i][j]:
            print(str(l1[i][j])+" and "+str(l2[i][j])+" are different at line "+str(i+1)+" and index "+str(j)+"\n")