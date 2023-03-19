class count:
    def __init__(self):
        self.vowel=0
        self.upper=0
        self.lower=0
        self.number=0
        self.spaces=0
        self.consonant=0
        self.string=input("Enter a String: ")
    def count_upper(self):
        for let in self.string:
            if let.isupper():
                self.upper+=1
    def count_lower(self):
        for let in self.string:
            if let.islower():
                self.lower+=1
    def count_vowels(self):
        for let in self.string:
            if let in "aeiouAEIOU":
                self.vowel+=1
    def count_numbers(self):
        for let in self.string:
            if let.isdecimal():
                self.number+=1
    def count_spaces(self):
        for let in self.string:
            if let.isspace():
                self.spaces+=1
    def count_consonant(self):
        for let in self.string:
            if let.isalpha():
                if let in "aeiouAEIOU":
                    self.consonant+=1
    def display(self):
        print("Total Numbers are",self.number,",Uppercase are",self.upper,",Lowercase are",self.lower,",consonants are",self.consonant,",Spaces are",self.spaces,",Vowels are",self.vowel)
    def runall(self):
        self.count_consonant()
        self.count_lower()
        self.count_numbers()
        self.count_spaces()
        self.count_upper()
        self.count_vowels()
        self.display()
count().runall()