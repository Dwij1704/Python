def arm(num):
    digit=0
    a=num
    arm=0
    l=int(len(str(num)))
    while num>0:
        digit=num%10
        arm=arm+(digit**l)
        num=num//10
    if a==arm:
        return True
    else:
        return False
print(arm(int(input("Enter a Number: "))))