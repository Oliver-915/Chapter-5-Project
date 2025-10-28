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
        newgame()
    elif option == 2:
        get_range_and_random()
    elif option == 3:
        exit()
    else:
        print("Choose a number 1, 2 or 3.")
        

def newgame():
    p1 = get_name_p1()
    p2 = get_name_p2()
    mini = get_mini()
    maxi = get_maxi()
    rand = get_random(mini, maxi)
    p1guess = -1
    p2guess = -1
    count = 0
    
    while p1guess != rand and p2guess != rand:
        p1guess = int(input(f'{p1} guess your number between {mini} and {maxi}: '))
        p2guess = int(input(f'{p2} guess your number between {mini} and {maxi}: '))
        
        if p1guess == rand and p2guess == rand:
            print(f'You both won in {count} turn(s)')
            break
        elif p1guess == rand:
            print(f'{p1}: You guessed correctly')
            print(f'{p1} wins!')
            print(f'It took {count} turns')
            break
            
        elif p1guess > rand:
            print(f'{p1}: To high')
        elif p1guess < rand:
            print(f'{p1}: To low')
    
        if p2guess == rand:
            print(f'{p2}: You guessed correctly')
            print(f'{p2} wins!')
            print(f'It took {count} turns')
            break
        elif p2guess > rand:
            print(f'{p2}: To high')
        elif p2guess < rand:
            print(f'{p2}: To low')
            
        count = count +1
        print('turn:', count)
        


def get_name_p1():
    p1 = input('Enter player 1s name: ')
    return p1

def get_name_p2():
    p2 = input('Enter player 2s name: ')
    return p2

def get_mini():
    mini = int(input('Enter the minimum range integer: '))
    return mini

def get_maxi():
    maxi = int(input('Enter the maximum range integer: '))
    return maxi

def get_random(mini, maxi):
    rand = 1
    rand = random.randint(mini, maxi)
    return rand
    

def exit():
    print("You are now exiting The Number Guessing Game:")



main()