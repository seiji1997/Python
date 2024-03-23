import utils
import random

print('Let\'s play Rock-Paper-Scissors!')
player_name = input('Enter your name: ')
print('What will you play? (0: Rock, 1: Scissors, 2: Paper)')
player_hand = int(input('Enter a number: '))

if utils.validate(player_hand):
    computer_hand = random.randint(0, 2)
    
    if player_name == '':
        utils.print_hand(player_hand)
    else:
        utils.print_hand(player_hand, player_name)

    utils.print_hand(computer_hand, 'Computer')
    
    result = utils.judge(player_hand, computer_hand)
    print('The result was ' + result)
else:
    print('Please enter a valid number')
