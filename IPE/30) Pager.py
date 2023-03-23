def pager(filename):
        f=open(filename,"r")
        count=0
        for i in f.readlines():
            print(i)
            count+=1
            if count%25==0:
                inp=input("Enter continue to read more")
                if inp=="continue":
                    break
pager("Dwij.txt")