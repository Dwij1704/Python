# 8. Write a Python program for Words Frequency in String Shorthands.
str="This tutorial for Python tutorial"
word={key:str.count(key) for key in str.split()}
print(word)