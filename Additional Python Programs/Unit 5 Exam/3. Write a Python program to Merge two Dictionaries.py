# 3. Write a Python program to Merge two Dictionaries.
d1={x+5:x*2 for x in range(1,6)}
d2={x:x for x in range(1,6)}
print(d2)
print(d1)
for x,y in d1.items():
    d2[x]=y
print(d2)

# 2nd mehtod
d1={x+5:x*2 for x in range(1,6)}
d2={x:x for x in range(1,6)}
d2.update(d1)
print(d2)