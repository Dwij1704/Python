def rev(original_number):
    digit=0
    i=0
    rev=0
    while original_number>0:
        digit=original_number%10
        rev=rev*10+digit
        original_number=original_number//10
    return rev
print(rev(int(input("Enter a number: "))))