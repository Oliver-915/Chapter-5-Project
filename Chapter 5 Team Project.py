def main():
    print("The Number Guessing Game")
    print("Main Menu")
    print("Please choose one of the following")
    print("1 | Start New Game")
    print("2 | Choose Range")
    print('3 | Exit')
    option = int(input("Chose a number 1-3: "))
    if option == 1:
        newgame()
    elif option == 2:
        range()
    elif option == 3:
        exit()
    else:
        print("Choose a number 1-3.")
        
def newgame():
    print("newgame")

def range():
    numrange_min = 1
    numrange_max = 100
    numrange_min = int(input("Please enter the min number range, default is 1"))
    numrange_max = int(input("Please enter the max number range, default is 1000"))
    

def exit():
    print("You are now exiting The Number Guessing Game:")