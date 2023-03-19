class library:
    def __init__(self):
        self.title=""
        self.author=""
        self.publisher=""
    def inputs(self):
        self.title=input("Enter Title of the Book: ")
        self.author=input("Enter Author of the Book: ")
        self.publisher=input("Enter Publisher of the Book: ")
    def display(self):
        books=[]
        ch=input("Enter Y to contine and N to exit: ")
        if ch=="Y":
            choice=input("Enter 1. To Add Book\n2. To Display Books: ")
            if choice==1:
                books.append(library().inputs())
            elif choice==2:
                for i in books:
                    print(i)
        else:
            print("Enter Valid Choice")
books=library()
books.display()