def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name='Guest'):
    hands = ['Rock', 'Scissors', 'Paper']
    print(name + ' played ' + hands[hand])

def judge(player, computer):
    if player == computer:
        return 'Draw'
    elif player == 0 and computer == 1:
        return 'Win'
    elif player == 1 and computer == 2:
        return 'Win'
    elif player == 2 and computer == 0:
        return 'Win'
    else:
        return 'Lose'
