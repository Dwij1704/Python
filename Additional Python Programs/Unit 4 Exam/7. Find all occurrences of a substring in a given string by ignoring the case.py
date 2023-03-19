# 7. Find all occurrences of a substring in a given string by ignoring the case.
def calc_occurence(str,f_string):
    count=(str.upper()).count(f_string.upper())
    return(count)
print(calc_occurence(input("Enter a String: "),input("Enter a string to find: ")))