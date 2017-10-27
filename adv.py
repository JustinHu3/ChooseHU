def main():
    # intro
    print("Pokemon: A Journey to Catch Them All")
    print("\nYou are still asleep.")
    print("You suddenly wake up realizing that today is the day to choose your pokemon.")
    print("You get dressed and run down the stairs to the exit of your house.")
    print("You sprint to Professor Maple's house.")
    print("\n\nWhich pokemon do you want to choose?")
    print("(1) Turtwig (2) Chimchar (3) Piplup")

    choice = input("Make your choice: ")

    if choice == 1:
        turtwig()

    elif choice == 2:
        chimchar()

    else:
        piplup()


def turtwig():
    print("\nAfter choosing Turtwig, Turtwig jumps into your arms.")
    print("turtwig bites your hand as a thank you for choosing turtwig.")
    print("\n\nProfessor Maple gives you a package that needs to be bought back. What do you do?")
    print(" (1) You accept his request (2) You ignore him")

    choices = input("Make your choice: ")

    if choices == 1:
        accept()
    else:
        if choices == 2:
            ignore()


def chimchar():
    print("\nAfter choosing Chimchar, Chimchar shoots a bit of fire.")
    print("chimchar jumps around happily as a thank you for choosing chimchar.")
    print("\n\nProfessor Maple gives you a package that needs to be bought back. What do you do?")
    print(" (1) You accept his request (2) You ignore him")

    choices = input("Make your choice: ")

    if choices == 1:
        accept()
    else:
        if choices == 2:
            ignore()


def piplup():
    print("\nAfter choosing Piplup, Piplup jumps into your arms.")
    print("piplup nudges your hand as a thank you for choosing piplup.")
    print("\n\nProfessor Maple gives you a package that needs to be bought back. What do you do?")
    print(" (1) You accept his request (2) You ignore him")

    choices = input("Make your choice: ")

    if choices == 1:
        accept()
    else:
        if choices == 2:
            ignore()


def accept():
    print("\nYou leave Professor Maple's lab.")
    print("You start to go into the tallgrass.")
    print("\n\nYou encounter your first wild Pokemon.")
    print("(1) You summon your Pokemon to fight (2)You turn and run")

    choices = input("Make your choice: ")

    if choices == 1:
        summon()
    else:
        if choices == 2:
            run()


def ignore():
    print("\nProfessor takes back your chosen Pokemon.")
    print("He kicked you out of his lab.")
    print("You never got to catch them all.")
    print("GAME OVER .-.")

    choices = input("Make your choice: ")

    if choices == 1:
        summon()
    else:
        if choices == 2:
            run()


def summon():
    print("\nYou say all right my first pokemon battle.")
    print("You summon your pokemon and fight.")
    print("\n\nWhat do you want your pokemon to do?")
    print("(1) Tackle (2) Tail Whip")

    choices = input("Make your choice: ")

    if choices == 1:
        tackle()
    else:
        if choices == 2:
            whip()


def run():
    print("\nYou run away, trying to protect your Pokemon.")
    print("but the wild pokemon catches up to you and attacks you.")
    print("The wild pokemon had a disease and you died to infections.")
    print("Game over ;-;")

    choices = input("Make your choice: ")

    if choices == 1:
        tackle()
    else:
        if choices == 2:
            whip()


def tackle():
    print("\nYour Pokemon hit the wild Pokemon for half health.")
    print("You tell your Pokemon to tackle again.")
    print("\n\nYou made the wild pokemon faint.")
    print("(1) You continue walking forward to the town (2) You turn back")

    choices = input("Make your choice: ")

    if choices == 1:
        forward()
    else:
        if choices == 2:
            backward()


def whip():
    print("\nYour Pokemon whipped its tail, the other Pokemon's defense decreased by half.")
    print("You made your Pokemon to tackle; you got a critcal hit.")
    print("\n\nYou made the wild pokemon faint.")
    print("(1) You continue walking forward to the town (2) You turn back")

    choices = input("Make your choice: ")

    if choices == 1:
        forward()
    else:
        if choices == 2:
            backward()


def forward():
    print("\nYou finally made it through the tall grass.")
    print("You first go to the pokecenter to heal your pokemon")
    print("You deliver the parcel and recieve a box.")
    print("He tells you, deliver the package to Professor Maple.")
    print("You accept the job.")
    print("You bring the box back to Professor Maple.")
    print("He opens the box, and gives you 5 Pokeballs.")
    print("He tells you, This is the start of a new adventure and your Pokemon.")
    print("Your adventure starts now.")
    print("You won the game.")


def backward():
    print("\nYou make it home safely.")
    print("You tell Maple what happened, he forgives you.")
    print("You give back your Pokemon and decided to help in Maple's Lab.")
    print("Game Over")


main()
