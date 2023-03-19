def check():
    username_password_data = {
    "user1": "pass1",
    "user2": "pass2",
    "user3": "pass3",
    "user4": "pass4",
    "user5": "pass5",
    "user6": "pass6",
    "user7": "pass7",
    "user8": "pass8",
    "user9": "pass9",
    "user10": "pass10"
    }
    flag=0
    user=input("Enter a Username: ")
    org_pass=input("Enter a password: ")
    for k,v in username_password_data.items():
        if k==user:
            if v==org_pass:
                flag=1
                break
    if flag==0:
        print("Enter Valid Username or password")
    i=4
    while flag==1:
        password=input("Enter a new password: ")
        if not any(c.isdigit() for c in password):
            print("Enter valid password",i,"tries left")
            if i==0:
                print("Try again after 24hrs")
                break
            i-=1           
            continue
        if not any(c.isupper() for c in password):
            print("Enter valid password",i,"tries left")
            if i==0:
                print("Try again after 24hrs")
                break
            i-=1
            continue
        if not any(c.islower() for c in password):
            print("Enter valid password",i,"tries left")
            if i==0:
                print("Try again after 24hrs")
                break
            i-=1
            continue
        if not any(c in "@][_!#$%^&*()<>?/\\|}{~:" for c in password):
            print("Enter valid password",i,"tries left")
            if i==0:
                print("Try again after 24hrs")
                break
            i-=1
            continue
        if len(password) < 8 or len(password) > 15:
            print("Enter valid password",i,"tries left")
            if i==0:
                print("Try again after 24hrs")
                break
            i-=1
            continue
        else:
            print("Great! you successfully updated password")
            username_password_data[user]=password
            print(username_password_data)
            break        
check()