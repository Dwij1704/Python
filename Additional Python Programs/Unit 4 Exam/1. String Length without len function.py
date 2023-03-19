# Write a Python function to Find length of a string in python without using len function.
def leng(str):
    count=0
    for i in str:
        count+=1
    return count
print(leng(input("Enter a String: ")))