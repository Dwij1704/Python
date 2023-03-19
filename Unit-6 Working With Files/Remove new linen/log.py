def create(user,password):
    f=open("log.txt","a+")
    f.write(user+":"+password+"\n")
    f.close()
def check(user,password):
    f=open("log.txt","r")
    data=f.readlines()
    flag=0
    for i in data:
        check1=i.rstrip("\n")
        if check1==user+":"+password:
            flag=1
    if flag==1:
        print("Sucess")
    else:
        print("Invalid")
create("helly","dwij1704")
check(input("Enter user"),input("Enter Pass"))