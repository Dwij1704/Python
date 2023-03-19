class order:
    def __init__(self):
        self.total_order=0
        self.count=int(input("Enter Total Pizzas: "))
        self.pizza=[]
        self.no_toppings=[]
        for i in range(self.count):
            self.pizza.append([])
            self.no_toppings.append(0)
    def select_size(self):
        for i in range(self.count):
            size=int(input("Enter 1. For Small Pizza\n2. For Medium Pizza\n3. For Large Pizza: "))
            if size==1:
                self.total_order+=50
                self.pizza[i].append("Small")
            elif size==2:
                self.total_order+=100
                self.pizza[i].append("Medium")
            elif size==3:
                self.total_order+=200
                self.pizza[i].append("Large")
            else:
                print("Invalid Choice")
    def select_topping(self):
        for i in range(self.count):
            while True:
                topping=int(input("Enter 1. For Tomato\n2. For Olives\n3. For Corn\n4. For Capsicum\n5. For Mushroom\n6. For Brocolli\n7. For Jalepenos\n8. To Finish: "))
                if topping==1:
                    self.total_order+=20
                    self.pizza[i].append("Tomato")
                elif topping==2:
                    self.total_order+=20
                    self.pizza[i].append("Olives")
                elif topping==3:
                    self.total_order+=20
                    self.pizza[i].append("Corn")
                if topping==4:
                    self.total_order+=20
                    self.pizza[i].append("Capsicum")
                elif topping==5:
                    self.total_order+=20
                    self.pizza[i].append("Mushroom")
                elif topping==6:
                    self.total_order+=20
                    self.pizza[i].append("Brocolli")
                elif topping==7:
                    self.total_order+=20
                    self.pizza[i].append("Jalepenos")
                elif topping==8:
                    break
                else:
                    print("Invalid Choice")
                self.no_toppings[i]+=1
    def select_cheese(self):
        for i in range(self.count):
            size=int(input("Enter 1. For Mozrella\n2. For Double Cheese\n3. For 7-Cheese: "))
            if size==1:
                self.total_order+=50
                self.pizza[i].append("Mozrella")
            elif size==2:
                self.total_order+=70
                self.pizza[i].append("Double Cheese")
            elif size==3:
                self.total_order+=100
                self.pizza[i].append("7-Cheese")
            else:
                print("Invalid Choice")
    def display(self):
        print("Your Total Order is of Rupees",self.total_order)
        print("Your Order Details are:")
        count=0
        for i in self.pizza:
            count+=1
            countj=0
            flag=0
            for j in i:
                countj+=1
                if countj==1:
                    print("Size Of Your Pizza",count," is",j)
                    continue
                if countj<self.no_toppings[count-1]+2:
                    if flag==0:
                        print("Toppings for Your Pizza are: ",end="")
                        flag=1
                    print(j,end=" ")
                    continue
                print("\nCheese for Your Pizza is ",j)
                print("-----------------------------------------------------")
bill=order()
bill.select_size()
bill.select_topping()
bill.select_cheese()
bill.display()