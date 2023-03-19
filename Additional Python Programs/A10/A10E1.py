def all_divisible(tup,divisor):
    print()
    for i in tup:
        if i%divisor!=0:
            return False
    return True
def any_divisible(tup,divisor):
    print()
    for i in tup:
        if i%divisor==0:
            return True
    return False
def difference(tup):
    sort=tuple(sorted(tup,reverse=True))
    result=sort[0]
    for i in sort:
        if result==i:
            continue    
        result=result-i
    return result
num=(3, 7, 1, 15)
print(all_divisible(num, 5))
print(any_divisible(num, 2))
print(difference(num))