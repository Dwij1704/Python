sum1=0
sum2=0
temp=0
digit=0
l=0

for i in range(1,101):
    sum1=0
    temp=i
    l=len(str(i))
    while l>0:
        digit=temp%10
        sum1=sum1+(digit**l)
        temp=temp//10
        l-=1
    if sum1==i:
        print(i,"is a Diserium Number")
    temp=i
    while temp>0:
        digit=temp%10
        sum2=sum2+digit
        temp=temp//10
    if(sum2%i==0):
        print(i,"is a harshad number")