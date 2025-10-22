def main():
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
        

def range():
    numrange_min = 1
    numrange_max = 100
    numrange_min = int(input("Please enter the min number range, default is 1"))
    numrange_max = int(input("Please enter the max number range, default is 1000"))
    
    

def exit():
    print("You are now exiting The Number Guessing Game:")