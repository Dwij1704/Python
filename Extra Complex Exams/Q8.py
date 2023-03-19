rooms=int(input("Enter total number of rooms: "))
if rooms<5 or rooms>100:
    print("Enter number of rooms in the range of 5-100")
tv_rate=int(input("Enter rate for TV rooms: "))
non_tv_rate=int(input("Enter rate for non TV rooms: "))
revenue=int(input("Enter Revenue target: "))
total_patients=0
days=0
d_pat=0
d_rev=0
for i in range(1,13):
    if i%2==0:
        if i==2:
            for j in range(1,29):
                total_patients+=(6-i)**2 + abs(j-15)
                if (6-i)**2 + abs(j-15)<rooms:
                    days+=1
                    d_pat=(6-i)**2 + abs(j-15)<rooms
                    d_rev+=d_pat*non_tv_rate
        for j in range(1,30):
            total_patients+=(6-i)**2 + abs(j-15)
            if (6-i)**2 + abs(j-15)<rooms:
                days+=1
                d_pat=(6-i)**2 + abs(j-15)<rooms
                d_rev+=d_pat*non_tv_rate
    else:
        for j in range(1,30):
            total_patients+=(6-i)**2 + abs(j-15)
            if (6-i)**2 + abs(j-15)<rooms:
                days+=1
                d_pat=(6-i)**2 + abs(j-15)<rooms
                d_rev+=d_pat*non_tv_rate
print(total_patients)
print(days)
print(d_rev)
for i in range(rooms):
    if (i*tv_rate)*(365-days)>=revenue:
        print("Done")