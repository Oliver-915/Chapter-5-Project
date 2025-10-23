#Number guessing game
#Oliver and Brycen

def main():
    menu()
        
def menu():
    print("The Number Guessing Game")
    print("Main Menu")
    print("Please choose one of the following")
    print("1 | Start New Game")
    print('2 | Exit')
    option = int(input("Chose a number 1 or 2: "))
    if option == 1:
        newgame()
    elif option == 2:
        exit()
    else:
        print("Choose a number 1 or 2.")
        
def newgame():
    name = input("Please enter your name")
    print("Would you like to change the range? The default is 1-100")
    range_change = input("Yes or No?: ")
    if range_change = Yes or yes:
        range()
    else: print("The range will be 1-1000")
    gamestart()

def gamestart():
    #gamestart here
    pass
def get_random():
    mini = 1
    maxi = 1000
    mini = int(input('Enter the minimum range: '))
    maxi = int(input('Enter the maximum range: '))
    
    random_int = random.randint(mini, maxi)
    
    return random_int
    
    
>>>>>>> Stashed changes

def exit():
    print("You are now exiting The Number Guessing Game:")