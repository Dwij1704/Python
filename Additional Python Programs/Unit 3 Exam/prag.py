print("ENter choice 1 for farenheat to celcious 2 for celsious to farehnheat")
ch=int(input("Enter choice"))
def cc():
    c=float(input("Enter Celcious"))
    f=((9/5)*c)+32
    print(f)
def far():
    f=float(input("Enter Fareheanheat"))
    c=(f-32)*(5/9)
    print(c)
if ch==1:
    far()
elif ch==2:
    cc()
else:
    print("ENter Valid CHoice")