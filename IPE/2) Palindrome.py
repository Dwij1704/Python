#write a py prog to check if number is palindrome
def isPalindrome(number):
    rev=0
    a=number
    while number!=0:
        digit=number%10
        rev=rev*10+digit
        number=number//10
    if(rev==a):
        print("Number Is Palindrome")
    else:
        print("Number Is Not Palindrome")
n = int(input("Enter a number: "))
isPalindrome(n)