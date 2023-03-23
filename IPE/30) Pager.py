def pager(filename):
        f=open(filename,"r")
        flag=0
        count=0
        for i in f.readlines():
            print(i)
            count+=1
            if count%25==0:
                inp=input("Enter continue to read more: ")
                if inp=="continue":
                    continue
                else:
                    flag=1
            if flag==1:
                break
pager("Dwij.txt")