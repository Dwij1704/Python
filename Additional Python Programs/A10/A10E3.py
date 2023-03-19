import random
def get_player_guess():
    i=input("Enter your guess: ")
    if i.isdigit()==False:
        print("Invalid guess: That is not an integer!")
    else:
        i=int(i)
    if i<0:
        print("Invalid guess: Number must be between 1 and 100!")
    elif i>100:
        print("Invalid guess: Number must be between 1 and 100!")
    else:
        return i
def check_player_guess(guess,num):
        if guess == num:
            print("Your guess is correct! The magic number is",num)
            return True
        elif guess < num:
               print('Your guess is too low.')
        elif guess > num:
               print('Your guess is too high.')
def main():
    print("Can you guess the magic number?")
    num = random.randint(1, 100)
    wish="Y"
    while wish=="Y" or "y":
        guess=get_player_guess()
        if check_player_guess(guess,num)==True:
            break
        wish=str(input("Would You Like To Continue(Y/N)"))
        print(wish)
    else:
        print("Your guess is correct! The magic number is",num)
main()
