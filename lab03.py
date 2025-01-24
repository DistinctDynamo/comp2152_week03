import random

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

combatStrength = get_combat_strength("Enter your combat strength(1-6): ")
mCombatStrength = get_combat_strength("Enter the monster's combat strength(1-6): ")

for j in range(1, 21, 2):
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    heroWeapon = weapons[heroRoll-1]
    monsterWeapon = weapons[monsterRoll-1]
                            
    heroTotal = combatStrength + heroRoll
    monsterTotal = mCombatStrength + monsterRoll

    print(f"\n hero rolled {heroRoll}, monster rolled {monsterRoll}")
    print(f"\n hero selected {heroWeapon}, monster selected {monsterWeapon}")
    print(f"\n hero total strength: {heroTotal}, Monster totall strength: {monsterTotal}")

    # Determine the winner
    if heroTotal > monsterTotal:
        print("Hero wins!")
    elif monsterTotal > heroTotal:
        print("Monster wins!")
    else:
        print("It's a tie!")

    if j !=11:
        print("Battle concluded after 20 rounds!")
