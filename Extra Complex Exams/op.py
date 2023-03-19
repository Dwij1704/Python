def revenue_target(n, r1, r2, target):
    revenue = 0
    tv_rooms = 0
    for m in range(1, 13):
        for d in range(1, 32):
            if m == 2 and d > 28:
                break
            if m in [4, 6, 9, 11] and d > 30:
                break
            patients = (6 - m) ** 2 + abs(d - 15)
            if patients <= n:
                revenue += patients * r1
            else:
                revenue += n * r1 + (patients - n) * r2
                tv_rooms += patients - n
    while revenue < target:
        tv_rooms += 1
        revenue += r2
    return tv_rooms

n = 20
r1 = 1500
r2 = 1000
target = 7119500

result = revenue_target(n, r1, r2, target)

print("Number of TV rooms to buy:", result)
