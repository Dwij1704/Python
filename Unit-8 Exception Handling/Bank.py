class bank:
    def __init__(self,ac_name):
        self.ac_name=ac_name
        self.balance=10000
        print("Good Morning",self.ac_name)
        self.pin=int(input("Your Default Pin is 0000, Create a new Pin: "))
        self.choose()
    def set_pin(self):
        old_pin=int(input("Enter Your Old Pin: "))
        if self.pin==old_pin:
            self.pin=int(input("Your Current Pin is "+str(self.pin)+", Create a new Pin: "))
        else:
            print("Enter Valid Pin")
    def withdraw(self,withdraw_amount):
        pin=int(input("Enter pin to withdraw: "))
        if pin==self.pin:
            if withdraw_amount>self.balance:
                print("Insufficient Balance")
            else:
                self.balance-=withdraw_amount
                print("Withdrawn Sucessfully")
        else:
            print("Enter Valid Pin")
    def deposit(self,deposit_money):
        pin=int(input("Enter pin to withdraw: "))
        if pin==self.pin:
            self.balance+=deposit_money
            print("Deposited Sucessfully")
        else:
            print("Enter Valid Pin")
    def view_balance(self):
        print(self.balance)
    def choose(self):
        choice=int(input("Enter 1 To Withdraw\n2 To Deposit\n3 To Change Pin\n4 To View Balance\n5 To Exit: "))
        if choice!=1 and choice!=2 and choice!=3 and choice!=4 and choice!=5:
            print("Enter Valid Choice")
        elif choice==1:
            self.withdraw(int(input("Enter Money to be withdrawn: ")))
            print("Your new balance is ",self.balance)
            self.choose()
        elif choice==2:
            self.deposit(int(input("Enter Money to be Deposited: ")))
            print("Your new balance is ",self.balance)
            self.choose()
        elif choice==3:
            self.set_pin()
            print("Your new balance is ",self.balance)
            self.choose()
        elif choice==4:
            self.view_balance()
            self.choose()
        else:
            print("Thanks For Using Our Service",self.ac_name)
a1=bank(input("Enter Your Name: "))