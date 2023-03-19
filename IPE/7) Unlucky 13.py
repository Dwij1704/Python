l1=[0,13,2,3,4,13,2]
flag=0
sum=0
for i in l1:
    if i==13:
        flag=1
        continue
    if flag==1:
        flag=0
        continue
    sum+=i
print(sum)