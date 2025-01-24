# Dice options using list() and range()
diceOptions = list(range(1,7))

# Weapons Array
weapons = ["fist","Knife","Club","Gun","Bomb","Nuclear Bomb"]

# Display available weapons
print("Available Weapons: ", ','.join(weapons))

def get_combat_strength(prompt):
    while True:
        try:
            value=int(input(prompt))
            if 1 <= value <= 6:
                return value
            else:
                print("invalid input! Please enter a number between 1-6.")
        except ValueError:
            print("Invalid input.")