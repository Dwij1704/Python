def findchr(string,chr):
    flag=0
    for i in range(len(string)):
        if string[i]==chr:
            print(f"Index of {chr} is {i} in first occurence")
            flag=1
            break
    if flag!=1:
        print(f"Index Couldnt be Found -1")
findchr("Dwij","i")

def rfindchr(string,chr):
    flag=0
    for i in range(len(string)-1,-1,-1):
        if string[i]==chr:
            print(f"Index of {chr} is {i} in last occurence")
            flag=1
            break
    if flag!=1:
        print(f"Index Couldnt be Found -1")
rfindchr("DwiDj","D")
def subchr(string, chr, newchar):
    flag=0
    for i in range(len(string)):
        if string[i]==chr:
            string=string[0:i]+newchar+string[i+1:]
            print(string)
            flag=1
            break
    if flag!=1:
        print(f"Character Couldnt be Found")
subchr("Dwij","D","S")