# 8. Calculate the sum and average of the digits present in a string.
def calc(str):
    sum=0
    count=0
    for i in str:
        if i.isdigit():
            sum+=int(i)
            count+=1
    return sum, sum/count
result=calc(input("Enter a String: "))
print("Sum:",result[0],"Average:",result[1])