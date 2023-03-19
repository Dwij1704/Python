# 6. Write a Python program that accepts a string and calculate the number of uppercase letters and lowercase letters.
def totalcases(str):
    upper=0
    lower=0
    for i in str:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    return upper,lower
result=totalcases(input("Enter a String: "))
print("Upper Case:",result[0],"Lower Case:",result[1])