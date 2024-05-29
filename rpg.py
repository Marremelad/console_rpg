import functionality_rpg
from os import system

rpg = functionality_rpg


def main():
    while True:
        try:
            choice = main_menu()
            if choice == "1":
                system("cls")
                player = rpg.Player.get_player()
                break
            elif choice == "2":
                system("cls")
                player = rpg.load_player()
                break
            elif choice == "3":
                exit()
        except EOFError:
            system("cls")
            print("You have no profile to save")
            input()

    while True:
        try:
            if not player.checkpoint:
                system("cls")
                stage_1(player)
                player.checkpoint = "stage_2"
                input()

            if player.checkpoint == "stage_2":
                system("cls")
                stage_2(player)
                player.checkpoint = "stage_3"
                input()
            if player.checkpoint == "stage_3":
                system("cls")
                stage_3(player)
                print("You win")
                break
        except EOFError:
            save(player)


def main_menu():
    while True:
        system("cls")
        print(f"    MENU    \n\n1.New Game\n\n2.Load Game\n\n3.Exit")
        choices = ["1", "2", "3"]
        choice = input(
            "\nSelect an option by typing its associated number and pressing enter. Example '1' for 'New Game'.\n"
        )
        if choice in choices:
            return choice


def save(player):
    system("cls")
    choice = input("Would you like to save the game and return to the main menu?: ")
    if choice == "yes":
        rpg.save_player(player)
        main_menu()


def stage_1(player):
    enemy = rpg.Bandit()
    rpg.dialogue(f"Wellcome to stage 1. You will now be fighting {enemy.name}.")
    rpg.combat(player, enemy)


def stage_2(player):
    enemy = rpg.Troll()
    rpg.dialogue(f"Wellcome to stage 2. You will now be fighting {enemy.name}.")
    rpg.combat(player, enemy)


def stage_3(player):
    enemy = rpg.Dragon()
    rpg.dialogue(f"Wellcome to stage 3. You will now be fighting {enemy.name}.")
    rpg.combat(player, enemy)


main()
