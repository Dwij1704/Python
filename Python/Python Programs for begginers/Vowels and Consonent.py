#write a py prog to find if the given alphabet is Vowels or Consonent
a=input("Enter Your Alphabet= ")
b=["a","e","i","o","u","A","E","I","O","U"]
#Using OR
if a=="a" or a=="e" or a=="i" or a=="o" or a=="u" or a=="A" or a=="E" or a=="I" or a=="O" or a=="U": print("Vowel")
else : print("Consonent")
#Using in
if a in b : print("Vowel")
else: print("Consonent")