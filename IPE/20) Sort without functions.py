a=30
b=10
c=70
if a>b:
    if a>c:
        print(f"1st sorted number is {a}")
        if c>b:
            print(f"2nd sorted number is {c}")
            print(f"3nd sorted number is {b}")
        else:
            print(f"2nd sorted number is {b}")
            print(f"3nd sorted number is {c}")
    else:
        print(f"1st sorted number is {c}")
        print(f"2nd sorted number is {a}")
        print(f"3rd sorted number is {b}")
elif b>c:
    print(f"1st sorted number is {b}")
    if c>a:
        print(f"2nd sorted number is {c}")
        print(f"3rd sorted number is {a}")
    else:
        print(f"2nd sorted number is {a}")
        print(f"3rd sorted number is {c}")
else:
    print(f"1st sorted number is {c}")
    if b>a:
        print(f"2nd sorted number is {b}")
        print(f"3rd sorted number is {a}")
    else:
        print(f"2nd sorted number is {a}")
        print(f"3rd sorted number is {b}")