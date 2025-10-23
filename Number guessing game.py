#Number guessing game
#Oliver and Brycen
import math
import random
def main():
    menu()
        
def menu():
    print("The Number Guessing Game")
    print("Main Menu")
    print("Please choose one of the following")
    print("1 | Start New Game")
    print('2 | Choose Range')
    print('2 | Exit')
    option = int(input("Chose a number 1, 2 or 3: "))
    if option == 1:
        newgame(p1, p2, mini, maxi)
    elif option == 2:
        get_range_and_random()
    elif option == 3:
        exit()
    else:
        print("Choose a number 1, 2 or 3.")
        

def newgame(p1, p2, mini, maxi):
    p1 = ''
    p2 = ''
    mini = 1
    maxi = 1000
    get_names()
    get_range_and_random()
    p1guess = int(input(f'{player1} guess your number inbetween {mini} and {maxi}: '))
    




def get_names():
    p1 = input('Enter player 1s name: ')
    p2 = input('Enter player 2s name: ')
    return p1
    return p2

    
    
    

def get_range_and_random():
    mini = float(input('Enter the minimum range integer: '))
    maxi = float(input('Enter the maximum range integer: '))
    return mini
    return maxi
    rand = 1
    rand = random.randint(mini, maxi)
    return rand


    

def exit():
    print("You are now exiting The Number Guessing Game:")



main()