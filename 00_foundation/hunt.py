import random
import math

BOARD_SIZE = 5  # initial board size

def generate_position(size):
    # generate x and y coordinates in the range between 0 and size
    x = random.randrange(0, size)  # x coordinate
    y = random.randrange(0, size)  # y-coordinate

    return (x, y)

def calc_distance(pos1, pos2):
    # Calculate the distance between two points
    diff_x = pos1[0] - pos2[0]
    diff_y = pos1[1] - pos2[1]

    return math.sqrt(diff_x**2 + diff_y**2)

def move_position(direction, pos):
    # Move pos according to direction

    current_x, current_y = pos

    if direction == "n":
        current_y -= 1
    elif direction == "s":
        current_y += 1
    elif direction == "w":
        current_x -= 1
    elif direction == "e":
        current_x += 1

    return (current_x, current_y)

def suika_wari():
    suika_pos = generate_position(BOARD_SIZE)  # watermelon's coordinates
    player_pos = generate_position(BOARD_SIZE)  # player's coordinates

    # Repeat the process while the position of the watermelon and the player are different
    while suika_pos != player_pos:
        # Display the distance between the watermelon and the player
        distance = calc_distance(player_pos, suika_pos)
        print("Distance to watermelon:", distance)

        # Move the player according to key input
        c = input("n: move north, s: move south, e: move east, w: move west")
        player_pos = move_position(c, player_pos)

    print("Watermelon split!")

suika_wari()
