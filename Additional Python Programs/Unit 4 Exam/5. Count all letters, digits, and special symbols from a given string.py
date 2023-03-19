# 5. Count all letters, digits, and special symbols from a given string.
def totalcounts(str):
    alpha=0
    digit=0
    special=0
    for i in str:
        if i.isalpha():
            alpha+=1
        elif i.isdigit():
            digit+=1
        else:
            special+=1
    return alpha,digit,special
str1=input("Enter a String: ")
result=totalcounts(str1)
print("Total Alphabets: ",result[0],"Total Digit: ",result[1],"Total Special Characters: ",result[2])