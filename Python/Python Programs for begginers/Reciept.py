#write a py prog to find print a reciept type format
Milkshake = 4.99
Friesandperi = 2.59
Coke = 1.00
Cheeseburger = 4.99
Tax = "13%"
print("""Food Item       Price
==========      =======
Cheeseburger    $  """+str(Cheeseburger)+"""
 + Coke         $  """+str(Coke)+"""
Fries w/peri    $  """+str(Friesandperi)+"""
Milkshake       $  """+str(Milkshake)+"""
                -------
Sub-total:      $  11.57
Tax ("""+Tax+"""):      $  1.50
    Total:      $  13.07""")