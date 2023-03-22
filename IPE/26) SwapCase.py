# Create a function that will return another string similar to the input string, but with its case inverted. For
# example, input of “Mr. Ed” will result in “mR. eD” as the output string. Note: Use of the built-in swapcase
# function is prohibited.
def swap(string):
    new_string=""
    for i in range(len(string)):
        if string[i].isupper():    
            new_string+=string[i].lower()
        else:
            new_string+=string[i].upper()
    print(new_string)
swap("Mr. Ed")