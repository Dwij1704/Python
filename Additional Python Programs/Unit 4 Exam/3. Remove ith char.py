# 3. Write a program to remove i’th character from string in Python
def removechar(str,i):
    str2=str[0:i]+str[i+1::]
    return str2
print(removechar(input("Enter a String: "),int(input("Enter index to remove: "))))