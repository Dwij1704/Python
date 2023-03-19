import os
from tkinter import *
def clearui():
    for widgets in frame.winfo_children():
        widgets.destroy()
def ui(username):
    clearui()
    view_task_button = Button(frame,text="View Tasks", command=lambda: view_tasks(username))
    view_task_button.grid(row = 1, column = 2, pady = 10,padx = 10)
    add_task_button = Button(frame,text="Add Task", command=lambda: add_task(username))   
    add_task_button.grid(row = 1, column = 3, pady = 3,padx = 10)
    modify_task_button = Button(frame,text="Modify Task", command=lambda: modify_task(username))      
    modify_task_button.grid(row = 1, column = 4, pady = 3,padx = 10)
    delete_task_button = Button(frame,text="Delete Task", command=lambda: delete_task(username))    
    delete_task_button.grid(row = 1, column = 5, pady = 3,padx = 10)
    logout_button = Button(frame,text="Logout", command=lambda: main_screen(),fg="red")      
    logout_button.grid(row = 1, column = 6, pady = 3,padx = 10)
    user_label=Label(frame,text="Hello "+username,font=("Poppins", 15))
    user_label.grid(row=5,column=4,pady=80)   
def main_screen():
    clearui()
    username_label = Label(frame,text="Username:",font=("Poppins",10))
    username_entry = Entry(frame)
    password_label = Label(frame,text="Password:")
    password_entry = Entry(frame,show="*",)
    login_button = Button(frame,text="Login", command=lambda: login(username_entry.get(),password_entry.get()))
    register_button = Button(frame,text="Register", command=lambda: create_account(username_entry.get(),password_entry.get()))
    username_label.grid(row=0,column=0,padx=(100,0),pady=(75,0))
    username_entry.grid(row=0,column=1,pady=(75,0),padx=(1,100))
    password_label.grid(row=1,column=0,padx=(100,0),pady=(20,0))
    password_entry.grid(row=1,column=1,pady=(20,0),padx=(1,100))
    register_button.grid(row=3,column=1,pady=(5,200),padx=(35,150))
    login_button.grid(row=2,column=1,pady=(20,0),sticky='W',padx=(40,100))
def login(user,passw):
    # username=user
    username = "Dwij"
    password = passw
    clearui()
    # if check_credentials(username, password):
    if True:        
        ui(username)

def create_account(user,passw):
    username =user
    #username="Dwij"
    password = passw 
    if os.path.exists(str(username)+".txt"):
       error_label.config(text="Username already taken.\nPlease choose a different name.")
       error_label.place(x=140,y=240)
    else:
        if len(password) < 8:
            error_label.config(text="Password must be at least 8 characters long.")
            error_label.place(x=100,y=240)
            return
        elif not any(c in "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~" for c in password):
            error_label.config(text="Password must contain at least one special character.\n (!#$%&'()*+,-./:;<=>?@[\]^_`{|}~)")
            error_label.place(x=70,y=235)
            return
        elif not any(c.isupper() for c in password):
            error_label.config(text="Password must contain at least one uppercase letter")
            error_label.place(x=70,y=240)
            return
        elif not any(c.isdecimal() for c in password):
            error_label.config(text="Password must contain at least one decimal number.")
            error_label.place(x=75,y=240)
            return
        f=open("users.txt", "a")
        f.write(str(username)+":"+str(password)+"\n")
        f.close()
        open(str(username)+".txt", "w").close()
        error_label.config(text="Account created.")
        error_label.place(x=180,y=240)
    

def check_credentials(username, password):
    if os.path.exists("users.txt"):
        f=open("users.txt", "r")
        users = f.readlines()
        for user in users:
            if user.strip() == str(username)+":"+str(password):
                f.close()
                return True
    f.close()
    return False

def view_tasks(username):
    if os.path.exists(str(username)+".txt"):
        f=open(str(username)+".txt", "r")
        tasks = f.readlines()
        f.close()
        print("Task List:-")
        print("-----------------------")
        for i, task in enumerate(tasks):
            print(i+1,".",task.strip())
        print("-----------------------")
        print()
    else:
        print("No tasks found.")

def add_task(username):
    task = input("Enter a task: ")
    f=open(str(username)+".txt", "a")
    f.write(str(task)+"\n")
    f.close()
    print("Task added.")
    
def modify_task(username):
    view_tasks(username)
    task_index = int(input("Enter the task number you want to modify: "))
    f=open(str(username)+".txt", "r")
    tasks = f.readlines()
    f.close()
    if task_index > len(tasks):
        print("Invalid task number.")
        return
    new_task = input("Enter the new task: ")
    tasks[task_index - 1] = str(new_task)+"\n"
    f=open(str(username)+".txt", "w")
    f.writelines(tasks)
    f.close()
    print("Task modified.")
    
def delete_task(username):
    task_index = int(input("Enter the task number you want to delete: "))
    if os.path.exists(str(username)+".txt"):
        f=open(str(username)+".txt", "r")
        tasks = f.readlines()
        f.close()
        if task_index > len(tasks) or task_index < 1:
            print("Invalid task number.")
            return
        tasks.pop(task_index - 1)
        f=open(str(username)+".txt", "w")
        f.writelines(tasks)
        f.close()
        print("Task deleted.")
    else:
        print("No tasks found.")

r = Tk()
frame=Frame(r)
frame.pack()
frame.grid()
r.title('To-Do List')
r.geometry("425x300")
username_label = Label(frame,text="Username:",font=("Poppins",10))
username_entry = Entry(frame)
password_label = Label(frame,text="Password:")
password_entry = Entry(frame,show="*",)
login_button = Button(frame,text="Login", command=lambda: login(username_entry.get(),password_entry.get()))
register_button = Button(frame,text="Register", command=lambda: create_account(username_entry.get(),password_entry.get()))
username_label.grid(row=0,column=0,padx=(100,0),pady=(75,0))
username_entry.grid(row=0,column=1,pady=(75,0),padx=(1,100))
password_label.grid(row=1,column=0,padx=(100,0),pady=(20,0))
password_entry.grid(row=1,column=1,pady=(20,0),padx=(1,100))
register_button.grid(row=3,column=1,pady=(5,200),padx=(35,150))
login_button.grid(row=2,column=1,pady=(20,0),sticky='W',padx=(40,100))
error_label = Label(frame,text="",font=("Poppins",10))
error_label.place(x=140,y=240)
r.mainloop()