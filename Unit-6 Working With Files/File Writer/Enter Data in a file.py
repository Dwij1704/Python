file=open("data.txt","w")
# file.write("Hello\n")
# file.write("How are you")
for i in range(3):
    name=input("Enter A Name: ")
    file.write(name+"\n")
file.close