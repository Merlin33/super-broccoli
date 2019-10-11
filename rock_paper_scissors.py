# Rock, Paper, Scissors Game

from time import sleep
import random
import sys

cpuWin = int(0)
userWin = int(0)

# Logic
choices = ['Rock','Paper','Scissors']

def rpsGame(selection):
    global cpuWin
    global userWin
    cpuHand = random.choice(choices)

    print('You have chosen ' + choices[(selection-1)] + '!')

    loading = 'Loading...'
    for i in range(10):
        print(loading[i], sep=' ', end=' ', flush=True); sleep(0.15)

    print('The Computer has drawn ' + cpuHand + '!')

    if selection == 1 and cpuHand == 'Rock':
        print('Draw!')
    elif selection == 1 and cpuHand == 'Paper':
        print('You Lose!')
        cpuWin += 1
    elif selection == 1 and cpuHand == 'Scissors':
        print('You Win!')
        userWin += 1
    elif selection == 2 and cpuHand == 'Rock':
        print('You Win!')
        userWin += 1
    elif selection == 2 and cpuHand == 'Paper':
        print('Draw!')
    elif selection == 2 and cpuHand == 'Scissors':
        print('You Lose!')
        cpuWin += 1
    elif selection == 3 and cpuHand == 'Rock':
        print('You Lose!')
        cpuWin += 1
    elif selection == 3 and cpuHand == 'Paper':
        print('You Win!')
        userWin += 1
    elif selection == 3 and cpuHand == 'Scissors':
        print('Draw!')
    else:
        print('Huh?')

    print('\nUser Wins: ' + str(userWin) + '\nCPU Wins: ' + str(cpuWin))
    

    print('\nWould you like to play again? (Y/N)')
    answer = input()

    if answer == 'Y' or answer == 'Yes' or answer == 'y':
        print('Great!')
    elif answer == 'N' or answer == 'No' or answer == 'n':
        print('Aw')
        sys.exit()
    else:
        print('Huh?')
        sys.exit()


while True:
    while True:
        try:
            selection = int(input('Choose your weapon.\n\nRock 1\nPaper 2\nScissors 3\n\n'))
        except ValueError:
            print('Sorry, I didn\'t understand that.\nPlease return 1, 2 or 3')
            continue
        else:
            break
        
    rpsGame(selection)

