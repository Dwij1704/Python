f1=open("replace.txt","r+")
s=f1.read()
f1.close
f1=open("replace.txt","w")
f1.write(s.replace("Python","Java"))