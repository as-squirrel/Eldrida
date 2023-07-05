import sqlite3
import pygame
from pygame import mixer

from colorama import init, Fore, Style

init(autoreset=False)

pygame.init()

# The game's music
music = pygame.mixer.music.load('bad.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.2)

# Establish connection to the database
conn = sqlite3.connect('database.db')

# Create a cursor object
c = conn.cursor()

# Create a table for users
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
              name TEXT NOT NULL UNIQUE, 
              password TEXT NOT NULL)''')

# Create a table for inventory
c.execute('''CREATE TABLE IF NOT EXISTS inventory
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
              user_id INTEGER NOT NULL, 
              name TEXT NOT NULL, 
              quantity INTEGER NOT NULL)''')

# Register user
def register(name, password):
    try:
        c.execute('''INSERT INTO users (name, password)
                     VALUES (?, ?)''', (name, password))
        conn.commit()
        print("Registration successful!")
    except sqlite3.IntegrityError:
        print("User already exists!")

# User login
def login(name, password):
    c.execute('''SELECT * FROM users WHERE name = ? AND password = ?''', (name, password))
    user = c.fetchone()
    if user:
        print("Login successful!")
        return user
    else:
        print("Incorrect username or password!")

# Add item to inventory
def add_to_inventory(user_id, name, quantity):
    try:
        c.execute('''INSERT INTO inventory (user_id, name, quantity)
                     VALUES (?, ?, ?)''', (user_id, name, quantity))
        conn.commit()
        print("Inventory added!")
    except sqlite3.Error as e:
        print("Error adding inventory:", e)

# Search inventory
def search_inventory(user_id, name):
    c.execute('''SELECT * FROM inventory WHERE user_id = ? AND name = ?''', (user_id, name))
    inventory = c.fetchone()
    if inventory:
        print("Inventory found:", inventory)
    else:
        print("Inventory not found!")

# Game loop
def guess_capital(country, correct_capital):
    print("Guess the capital!")
    print("Country:", country)

    input_text = input("Your answer: ")

    if input_text.lower() == correct_capital.lower():
        print("Correct! That is the capital of", country)
    else:
        print("Incorrect! The correct capital of", country, "is", correct_capital)

def guess_continent(country, correct_continent):
    print("Guess the continent!")
    print("Country:", country)

    input_text = input("Your answer: ")

    if input_text.lower() == correct_continent.lower():
        print("Correct! The country", country, "is located in", correct_continent)
        return True
    else:
        print("Incorrect! The country", country, "is located in", correct_continent)
        return False


def guess_highest_peak(country, correct_highest_peak):
    print("Guess the highest peak!")
    print("Country:", country)

    input_text = input("Your answer: ")

    if input_text.lower() == correct_highest_peak.lower():
        print("Correct! The highest peak of", country, "is", correct_highest_peak)
    else:
        print("Incorrect! The highest peak of", country, "is", correct_highest_peak)

def guess_longest_river(country, correct_longest_river):
    print("Guess the longest river!")
    print("Country:", country)

    input_text = input("Your answer: ")

    if input_text.lower() == correct_longest_river.lower():
        print("Correct! The longest river of", country, "is", correct_longest_river)
    else:
        print("Incorrect! The longest river of", country, "is", correct_longest_river)

def guess_state(country, correct_state):
    print("Guess the country!")
    print("State:", correct_state)

    input_text = input("Your answer: ")

    if input_text.lower() == correct_state.lower():
        print("Correct! The country", country, "has the state", correct_state)
    else:
        print("Incorrect! The country", country, "has the state", correct_state)

capitals = {
    "Germany": "Berlin",
    "France": "Paris",
    "Spain": "Madrid",
    "Italy": "Rome",
    "Canada": "Ottawa",
    "Australia": "Canberra",
    "South Africa": "Pretoria",
    "Indonesia": "Jakarta",
    "Estonia": "Tallinn",
    "Uruguay": "Montevideo",
    "Bangladesh": "Dhaka",
    "Kyrgyzstan": "Bishkek"
}

continents = {
    "Germany": "Europe",
    "France": "Europe",
    "Spain": "Europe",
    "Italy": "Europe",
    "Canada": "North America",
    "Australia": "Australia",
    "South Africa": "Africa",
    "Indonesia": "Asia",
    "Estonia": "Europe",
    "Uruguay": "South America",
    "Bangladesh": "Asia",
    "Kyrgyzstan": "Asia"
}

highest_peaks = {
    "Germany": "Zugspitze",
    "France": "Mont Blanc",
    "Spain": "Teide",
    "Italy": "Monte Bianco",
    "Canada": "Mount Logan",
    "Australia": "Mount Kosciuszko",
    "South Africa": "Table Mountain",
    "Indonesia": "Puncak Jaya",
    "Estonia": "Suur Munamägi",
    "Uruguay": "Cerro Catedral",
    "Bangladesh": "Keokradong",
    "Kyrgyzstan": "Pik Pobedy"
}

longest_rivers = {
    "Germany": "Rhine",
    "France": "Seine",
    "Spain": "Ebro",
    "Italy": "Po",
    "Canada": "Mackenzie River",
    "Australia": "Murray River",
    "South Africa": "Orange River",
    "Indonesia": "Kapuas River",
    "Estonia": "Pärnu River",
    "Uruguay": "Uruguay River",
    "Bangladesh": "Jamuna River",
    "Kyrgyzstan": "Naryn River"
}

states = {
    "Germany": "Bavaria",
    "France": "Île-de-France",
    "Spain": "Madrid",
    "Italy": "Lazio",
    "Canada": "Ontario",
    "Australia": "New South Wales",
    "South Africa": "Gauteng",
    "Indonesia": "Java",
    "Estonia": "Harju",
    "Uruguay": "Montevideo",
    "Bangladesh": "Dhaka",
    "Kyrgyzstan": "Chuy"
}

logged_in = False

def clear_inventory():
    # Delete the inventory of the current user ID from the database
    c.execute('''DELETE FROM inventory WHERE user_id = ?''', (user[0],))
    conn.commit()

while True:
    # Display main menu
    print(Fore.YELLOW + "Welcome to the text adventure!" + Style.RESET_ALL)
    print("1 - Register")
    print("2 - Log in")
    print("3 - Quit")

    choice = input("Choice: ")

    if choice == "1":
        # Start registration process
        name = input("Username: ")
        password = input("Password: ")
        register(name, password)

    elif choice == "2":
        # Start login process
        name = input("Username: ")
        password = input("Password: ")
        user = login(name, password)
        if user:
            logged_in = True

    elif choice == "3":
        # Quit program
        break

    else:
        print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)

    while logged_in:
        # Game loop
        print(Fore.GREEN + "You are logged in!" + Style.RESET_ALL)
        print("1 - Show inventory")
        print("2 - Start adventure")
        print("3 - Log out")

        choice = input("Choice: ")

        if choice == "1":
            # Show inventory
            c.execute('''SELECT * FROM inventory WHERE user_id = ?''', (user[0],))
            inventory = c.fetchall()
            if inventory:
                print(Fore.CYAN + "Your inventory:" + Style.RESET_ALL)
                for item in inventory:
                    print(item[2], "x", item[3])

                print(">---------------------------------------<")
            else:
                print(Fore.CYAN + "Your inventory is empty." + Style.RESET_ALL)
                print(">---------------------------------------<")

        elif choice == "2":
            # Start adventure
            print("You enter a dark forest...")
            print("You find a treasure!")
            print("1 - Open treasure")
            print("2 - Ignore treasure")

            choice = input("Choice: ")

            if choice == "1":
                # Open treasure
                print("Inside the treasure, you find a powerful weapon!")
                print("1 - Take the weapon")
                print("2 - Leave the weapon behind")

                choice = input("Choice: ")

                if choice == "1":
                    # Take the weapon
                    print("You take the weapon and feel its power!")
                    print("You have successfully completed the adventure!")
                    # Add item to inventory
                    add_to_inventory(user[0], "Weapon", 1)

                elif choice == "2":
                    # Leave the weapon behind
                    print("You decide to leave the weapon behind...")
                    print("The adventure continues!")

            elif choice == "2":
                # Ignore treasure
                print("You decide to ignore the treasure...")
                print("The adventure continues!")

            print("Suddenly, you are attacked by an orc!")
            print("1 - Fight")
            print("2 - Flee")

            choice = input("Choice: ")

            if choice == "1":
                # Fight
                print("The orc strikes you with his club, and you die...")
                print(Fore.RED + "Game Over!" + Style.RESET_ALL)
                clear_inventory()
                break

            elif choice == "2":
                # Flee
                print("In the distance, you see a castle!")
                print("You enter and find safety.")
                print("-----------------------------------------")
                print("You encounter a priest who wants to bless you.")
                print("1 - Accept the blessing")
                print("2 - Decline the blessing")

                choice = input("Choice: ")

                if choice == "1":
                    # Accept the blessing
                    print("You receive the blessing and feel the power of God!")
                    print("The adventure continues!")

                    print("Suddenly, a mighty dragon appears before you!")
                    print("1 - Fight with the blessed weapon")
                    print("2 - Beg the dragon for mercy")
                    print("3 - Attempt to run away")

                    choice = input("Choice: ")

                    elif choice == "1":
                        # Fight with the blessed weapon
                        if "Blessed Weapon" in inventory:
                            print("With your blessed weapon, you bravely engage in battle against the dragon.")
                            # Here you can implement the battle mechanics

                        else:
                            print("You don't have a suitable weapon to face the dragon. You die...")
                            print(Fore.RED + "Game Over!" + Style.RESET_ALL)
                            clear_inventory()
                            break

                    elif choice == "2":
                        # Beg the dragon for mercy
                        print("You kneel down and beg the dragon for mercy.")
                        print("The dragon appears to be compassionate and lets you go unharmed.")

                    elif choice == "3":
                        # Attempt to run away
                        print("You try to flee from the dragon.")
                        # Here you can implement the escape mechanics

                        print("You continue your adventure and arrive at a mysterious temple.")
                        print("1 - Enter the temple")
                        print("2 - Bypass the temple and continue")

                        choice = input("Choice: ")

                        if choice == "1":
                            # Enter the temple
                            print("You enter the temple and find a wondrous old chest.")
                            print("You examine it closely and realize it can only be opened by solving a riddle.")
                            print("1 - Solve the riddle")
                            print("2 - Ignore the chest")

                            choice = input("Choice: ")

                                elif choice == "1":
                                    # Solve the riddle
                                    print("A mystical voice speaks up and presents you with a riddle.")
                                    correct_continent = continents["Germany"]
                                    is_solution_correct = guess_continent("Germany", correct_continent)

                                    if is_solution_correct:
                                        print("As if by magic, the chest opens, and you find an ancient magical talisman inside.")
                                        print("1 - Take the talisman")
                                        print("2 - Ignore the talisman")

                                        choice = input("Choice: ")

                                        if choice == "1":
                                            # Take the talisman
                                            print("You take the magical talisman and feel its power.")
                                            add_to_inventory(user[0], "Talisman", 1)

                                            # Here you can add the new riddle
                                            print("After storing the talisman in your inventory, you discover a mysterious door in the temple.")
                                            print("Next to the door, there is an inscription that reads:")
                                            print("Guess the highest elevation in Germany to open the door.")

                                            guess_highest_elevation("Germany", highest_elevations["Germany"])

                                            # Continue the story after the highest elevation riddle
                                            print("The door opens with a loud creak, revealing a dark corridor that leads deeper into the temple.")
                                            print("You decide to explore the corridor and proceed cautiously.")
                                            print("After a few minutes, you reach a large chamber where a glowing crystal sits atop a pedestal.")
                                            print("You sense a powerful energy emanating from the crystal.")
                                            print("1 - Touch the crystal")
                                            print("2 - Ignore the crystal and continue")

                                            choice = input("Choice: ")

                                            if choice == "1":
                                                # Touch the crystal
                                                print("As you touch the crystal, a surge of magical energy courses through your body.")
                                                print("You feel empowered and gain new abilities.")
                                                print("1 - Fire spell")
                                                print("2 - Healing spell")

                                                choice = input("Choice: ")

                                            elif choice == "1":
                                                # Fire spell
                                                print("You now possess the mighty fire spell. Flames ignite around your hands.")
                                                add_to_inventory(user[0], "Fire Spell", 1)
                                                print("You add the fire spell to your inventory and feel ready for upcoming challenges.")
                                            elif choice == "2":
                                                # Healing spell
                                                print("You now hold the power of healing in your hands. You can close wounds and restore health.")
                                                add_to_inventory(user[0], "Healing Spell", 1)
                                                print("You add the healing spell to your inventory and feel ready for upcoming challenges.")
                                        
                                        elif choice == "2":
                                            # Ignore the crystal
                                            print("You decide to ignore the crystal and continue through the temple.")
                                            print("You're curious about what awaits you.")

                                    elif choice == "2":
                                        # Ignore the chest
                                        print("You choose to ignore the chest and leave the temple.")

                                else:
                                    print("You didn't solve the riddle, and the chest remains locked.")
                                    print("You leave the temple and continue on your journey.")

                        elif choice == "2":
                            # Bypass the temple and continue
                            print("You decide to bypass the mysterious temple and continue your journey.")
                            print("Who knows what awaits you on your path.")

                elif choice == "2":
                    # Decline
                    print("You continue your adventure and come across a deep gorge.")
                    print("1 - Jump across the gorge")
                    print("2 - Look for another way")

                    choice = input("Choice: ")

    if choice == "1":
        # Jump across the gorge
        print("You take a running start and leap across the gorge.")
        print("It's a daring jump, but you safely make it to the other side.")
        print("You feel relieved and proud of your agility.")

    elif choice == "2":
        # Look for another way
        print("You decide to look for another way around the gorge.")
        print("After some time, you discover a narrow bridge that spans the gorge.")
        print("You cautiously cross the bridge and safely reach the other side.")

    print("During your adventure, you come across an abandoned village.")
    print("1 - Explore the village")
    print("2 - Pass by the village")

    choice = input("Choice: ")

    if choice == "1":
        # Explore the village
        print("Curious, you decide to explore the abandoned village.")
        print("You enter the narrow streets of the village and see that the houses are in decay, reclaimed by nature.")
        print("An eerie silence hangs in the air, only broken by the faint rustling of the wind.")
        print("As you make your way through the deserted streets, you notice that many of the houses have been ransacked, with personal belongings scattered about.")

        print("Suddenly, you hear a faint crying sound in the distance.")
        print("You follow the sound and arrive at a small house at the edge of the village.")
        print("The door is half-open, and the crying grows louder.")
        print("You enter the house and find a young woman sitting in a corner, sobbing.")

        print("1 - Talk to the woman")
        print("2 - Leave the house")

    elif choice == "2":
        # Pass by the village
        print("You choose to pass by the abandoned village and continue on your journey.")

choice = input("Choice: ")

if choice == "1":
    # Talk to the woman
    print("You approach the woman slowly and speak to her gently.")
    print("She looks up, tears streaming down her face.")
    print("She tells you that the village has been plagued by a dark force that drove the villagers away.")
    print("Her family was separated, and she is the only one who remained.")

    print("1 - Comfort the woman and offer help")
    print("2 - Leave the village and continue the adventure")

    choice = input("Choice: ")

    if choice == "1":
        # Comfort the woman and offer help
        print("You sit down next to the woman and take her hand.")
        print("You assure her that you will help her find her family and free the village from the dark force.")
        print("Her face brightens a little, and she thanks you for your support.")

        print("Together, you set out to explore the village and search for clues about the missing family members.")
        print("You search the houses, talk to the few remaining villagers, and uncover more and more signs of the presence of the dark force.")

        print("After some time, you discover an old hidden entrance to a secret cave beneath the village.")
        print("You decide to enter, hoping to find answers and perhaps a way to free the village.")

        print("The cave is dark and filled with dangers. You have to navigate past poisonous spider webs, balance on unstable bridges, and decipher mysterious mechanisms to proceed. But you don't give up and bravely fight your way through the challenges.")

print("Eventually, you reach the deepest part of the cave, where you encounter a sinister figure – the leader of the dark force terrorizing the village. An epic battle ensues, where you use your newfound weapon and abilities to confront the leader. You fight fiercely as the cave echoes with the sounds of your battle.")

print("Thanks to your heightened senses and the powerful weapon, you manage to defeat the leader of the dark force. He disappears into a dark mist that slowly dissipates, bathing the cave in warm light.")

print("As the mist clears, a mysterious portal appears before you. It seems to be a connection to another dimension. You feel a strong presence and an inexplicable pull from beyond the portal.")

print("1 - Enter the portal")
print("2 - Ignore the portal and return to the village")

choice = input("Choice: ")

if choice == "1":
    print("You and the saved woman step through the portal together and suddenly find yourselves in a fascinating yet unfamiliar world. The landscape is breathtaking, with shimmering waterfalls, luminous plants, and exotic creatures.")
    
    print("You explore this new world full of adventure and secrets. Together, you embark on a quest to find the woman's missing family members and face the challenges that await you here.")
    
    print("Throughout your journey, you encounter fascinating beings and befriend some of them. You discover hidden treasures that make you even more powerful and gain experience and wisdom.")
    
    print("After many thrilling adventures and fierce battles, you succeed in tracking down the woman's missing family members and safely bringing them back. You have kept your promise and freed the village from the dark force.")
    
    print("The village flourishes once again, and the residents return. You are celebrated as heroes and rewarded as a token of gratitude for your courage and bravery. The saved woman is grateful for your help and joins you to continue experiencing adventures by your side.")
    
    print("Together, you explore the new world.")
    
    print("The woman asks if you want to stay with her in the village or seek a new adventure.")
