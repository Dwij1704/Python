def log(user,password):
    f=open("User_Pass.txt","r")
    u=f.readlines()
    for i in u:
        if i[i.find(user):i.find(user)+len(user)]==user and i[i.find(password):i.find(password)+len(password)]==password:
            print("Logged in")
            break
    else:
        print("Invalid Username Password")
log(input("Enter a Username: "),input("Enter a Password: "))