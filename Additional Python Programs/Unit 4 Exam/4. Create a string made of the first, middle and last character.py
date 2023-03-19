# 4. Create a string made of the first, middle and last character
def rephrase(str):
    mid=int(len(str)/2)
    str2=str[0]+str[mid]+str[-1]
    return str2
print(rephrase(input("Enter a String: ")))