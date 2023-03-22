dollar=float(input("Enter amount in less than a dollar: $"))
dollar=int(dollar*100)
quater=dollar//25
dollar-=(quater*25)
dime=dollar//10
dollar-=(dime*10)
nickel=dollar//5
dollar-=(nickel*5)
cent=dollar
print(f"You need {quater} Quaters, {dime} Dime, {nickel} Nickel and {cent} cents") 
# Enter amount in less than a dollar: $0.67
# You need 2 Quaters, 1 Dime, 1 Nickel and 2 cents