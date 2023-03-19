f = None
with open("data.txt", "w") as f:
    data=f.readlines()
    print(data)
    f.seek(0)
    data=f.readline()
    print(data)
    print(f.closed)
print(f.closed)


f = None
for i in range (5):
    with open("data.txt", "w") as f:
        if i > 2:
            break
print(f.closed)
