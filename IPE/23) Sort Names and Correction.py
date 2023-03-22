class ContactBook():
    def __init__(self):
        self.mistakes = 0
        self.contacts = []
    def take_input(self):
        name = input("Please enter name #"+str(len(self.contacts))+"> ")
        if len(name.split(',')) == 1:
            self.mistakes += 1
            print ("Wrong Format... Should be LastName, FirstName")
            print ("You have done this",self.mistakes,"time(s) already! Fixing name..")
            flname = name.split(' ')
            name = flname[1]+", "+flname[0]
        self.contacts.append(name)
    def display_sorted(self):
        return "\n".join(sorted(self.contacts))

print ("Please enter names in format Lastname, Firstname")
cb = ContactBook()
another = True
while another:
    cb.take_input()
    ask_another = input("Add another? (yes/no) > ")
    another = False if ask_another == 'no' else True
# sort here
    print (cb.display_sorted())