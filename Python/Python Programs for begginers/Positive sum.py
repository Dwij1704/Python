#write a py prog to determine and add only positive numbers
n=int(input("Enter Total Number= "))
sum=0
negcount=0
for i in range(n):
    print("Enter",i,"Number= ",end="")
    x=int(input())
    if x<0:
        negcount+=1
        continue
    else:
        sum+=x
print("Total negative number are",negcount,"and the sum of positive numbers is",sum)