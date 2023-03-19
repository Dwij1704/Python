# 11. Replace each special symbol with # in the following string.
import string
org=input("Enter a String: ")
for char in string.punctuation:
    org=org.replace(char,"#")
print(org)