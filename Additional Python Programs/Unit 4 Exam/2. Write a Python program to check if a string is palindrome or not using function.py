# 2. Write a Python program to check if a string is palindrome or not using function
def palindrome(str):
    str1=str[-1::-1]
    if str==str1:
        return True
    else:
        return False
print(palindrome(input("Enter String: ")))