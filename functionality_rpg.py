import csv
import datetime
import random
import time

# Player class
class Player:
    player_count = 0

    def __init__(self, name="Player"):
        self.name = name
        Player.player_count += 1
        self.player_number = Player.player_count

    def __str__(self):
        return f"My name is {self.name} and i am player number {self.player_number}"

    # Returns name
    @staticmethod
    def get_name():
        name = input("What is your name?\n")
        return name

    # Gets player name and class
    @staticmethod
    def get_player():
        name = Player.get_name()
        while True:
            classes = ["warrior", "wizzard"]
            choice = input("Choose a class, warrior or wizzard\n").lower()
            if choice in classes:
                if choice == "warrior":
                    return Warrior(name)
                else:
                    return Wizzard(name)


# Warrior class, child class to Player
class Warrior(Player):
    def __init__(self, name="Nameless Warrior"):
        super().__init__(name)
        self.cl = "warrior"
        self.weapon = "Sword"
        self.health = 100  # 100
        self.attack = 100  # 50
        self.defense = 50  # 50
        self.skill = {"Pierce": 100}
        self.checkpoint = None

    def __str__(self):
        return f"I am a warrior with {self.health} hp, {self.attack} attack {self.defense} defense and my skill is {self.skill}"


# Wizzard class, child class to Player
class Wizzard(Player):
    def __init__(self, name="Nameless Wizzard"):
        super().__init__(name)
        self.cl = "wizzard"
        self.weapon = "Staff"
        self.health = 100  # 100
        self.attack = 30  # 30
        self.defense = 30  # 30
        self.skill = {"Fireball": 100}
        self.checkpoint = None

    def __str__(self):
        return f"I am a wizzard with {self.health} hp, {self.attack} attack {self.defense} defense and my skill is {self.skill}"


# Default enemy used for testing and debugging
class Enemy:
    name = "Placeholder"
    health = 100  # 100
    attack = 20  # 20
    defense = 30  # 30


# Enemies
class Bandit:
    name = "Bandit"
    health = 10
    attack = 10
    defense = 10


class Troll:
    name = "Troll"
    health = 10
    attack = 10
    defense = 10


class Dragon:
    name = "Dragon"
    health = 10
    attack = 10
    defense = 10


# Functions


# Initalises combat
def combat(player, enemy):
    while True:
        if first() == True:
            print(player_first(player_first_choice(), player, enemy))
            status = check_health_player(player, enemy)
        else:
            print(enemy_first(player, enemy))
            status = check_health_enemy(player)

        if status == True:
            print(f"You have slain {enemy.name}!")
            return True
        elif status == False:
            return False
        else:
            print("Get ready for the next turn")


# Decides who goes first
def first():
    player = random.randint(1, 10)
    enemy = random.randint(1, 5)
    if player > enemy:
        return True
    else:
        return False


# Lets player choose between attacking and using a skill
def player_first_choice():
    while True:
        choices = ["a", "s"]
        choice = input("What do you want to do? Attack or use a skill?\n")
        if choice in choices:
            return choice


# If player goes first
def player_first(choice, player, enemy):
    if choice == "a":
        damage = player.attack - enemy.defense
        if damage > 0:
            enemy.health -= damage
            return f"You did {damage} damage"
        else:
            player.health += damage  # Damage is dealt to player if attack is lower than enemy defense
            return f"You took {damage * -1} damage"
    else:
        if not player.skill:
            return "You have no available skill"
        else:
            damage = list(player.skill.values())[0] - enemy.defense
            enemy.health -= damage
            return f"You did {damage} skill damage"


# Checks player and enenmy health after player action
def check_health_player(player, enemy):
    if player.health <= 0:
        return False
    elif enemy.health <= 0:
        return True
    else:
        return


# If enemy goes first
def enemy_first(player, enemy):
    print("The enemy goes first and chooses to attack you!")
    damage = enemy.attack - player.defense
    if damage > 0:
        player.health -= damage
        return f"You took {damage} damage"
    else:
        return "You blocked the attack sucessfully"  # Enemy does not take recoil damage


# Checks player health after enemy action
def check_health_enemy(player):
    if player.health <= 0:
        return False
    else:
        return


# Saves a players profile into a CSV file
def save_player(player):

    file = saved_profiles()

    with open(f"{file}.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "class",
                "name",
                "weapon",
                "health",
                "attack",
                "defense",
                "skill",
                "checkpoint",
            ],
        )
        writer.writerow(
            {
                "class": player.cl,
                "name": player.name,
                "weapon": player.weapon,
                "health": player.health,
                "attack": player.attack,
                "defense": player.defense,
                "skill": player.skill,
                "checkpoint": player.checkpoint,
            }
        )


# Loads a players profile into the game using a csv file
def load_player():
    display_saved_profiles()
    load = validate_file()
    with open(f"{load}.csv") as file:
        reader = csv.DictReader(
            file,
            fieldnames=[
                "class",
                "name",
                "weapon",
                "health",
                "attack",
                "defense",
                "skill",
                "checkpoint",
            ],
        )
        rows = [row for row in reader]
        player = load_class(rows)
    return player


# Checks class of loaded profile and creates a class objekt
def load_class(rows):
    if rows[0]["class"] == "warrior":
        player = Warrior()
        load_stats(rows, player)
    else:
        player = Wizzard()
        load_stats(rows, player)
    return player


# Asigns values to the classes atributes
def load_stats(rows, player):
    player.name = rows[0]["name"]
    player.weapon = rows[0]["weapon"]
    player.health = int(rows[0]["health"])
    player.attack = int(rows[0]["attack"])
    player.defense = int(rows[0]["defense"])
    player.skill = rows[0]["skill"]
    player.checkpoint = rows[0]["checkpoint"]
    return player


# Appends file names to  the "saved_profiles" file
def saved_profiles():
    while True:
        new_file = input("Enter name of profile you want to save: ")
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        with open("saved_profiles.csv") as file:
            for row in file:
                if new_file in row:
                    print("A file with this name already exists")
                    break
            else:
                with open("saved_profiles.csv", "a", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=["file", "date"])
                    writer.writerow({"file": new_file, "date": date})
                    break
    return new_file


# Displays available profiles
def display_saved_profiles():
    print("Available profiles")
    with open("saved_profiles.csv") as file:
        reader = csv.DictReader(file, fieldnames=["file", "date"])
        for row in reader:
            print(row["file"], row["date"])


def validate_file():
    while True:
        file_name = input("Enter name of file to load: ")
        with open("saved_profiles.csv") as file:
            for row in file:
                if file_name in row:
                    return file_name
                else:
                    print("file does not exist")


# Simulates speech in text format
def dialogue(string):
    for line in string:
        for i in line:
            print(i, end="", flush=True)
            time.sleep(0.05)  # Change to speed up or slow down character output
            if i == "\n":
                time.sleep(1.5)  # Change to speed up or slow down new-line output
