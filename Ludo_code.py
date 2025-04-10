import random

colors = ["Red", "Green", "Yellow", "Blue"]
start_positions = {
    "Red": 1,
    "Green": 1,
    "Yellow": 1,
    "Blue": 1,
}

def roll_dice():
    return random.randint(1, 6)

def move_token(position, dice_roll):
    new_position = position + dice_roll
    if new_position >= 52:
        exit
    return new_position


def play_ludo():
    player_positions = {color: start_positions[color] for color in colors}

    while True:
        for color in colors:
            print(f"\n{color}'s turn:")
            dice_roll = roll_dice()
            print(f"Dice roll: {dice_roll}")

            position = player_positions[color]
            new_position = move_token(position, dice_roll)
            player_positions[color] = new_position

            print(f"{color} moved from {position} to {new_position}")

            if new_position>=52:
                print(f"{color} has won!")
                return

            input("Press Enter to continue")

play_ludo()
