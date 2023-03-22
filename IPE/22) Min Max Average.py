sum=0
count=0
while True:
    inp=input("Enter input: ")
    if count==0:
        min=int(inp)
        max=int(inp)
    if inp=="done":
        break
    inp=int(inp)
    if max<inp:
        max=inp
    if min>inp:
        min=inp
    sum+=inp
    count+=1
print(f"Average: {sum/count}, Max: {max}, Min: {min}")