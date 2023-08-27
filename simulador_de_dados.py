import random       # Importing random module


# ------------ function definition

def roll_dice():
    numero = random.randint(1, 6)
    if numero == 1:
        print("-----------")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("-----------")

    elif numero == 2:
        print("-----------")
        print("|         |")
        print("| 0     0 |")
        print("|         |")
        print("-----------")

    elif numero == 3:
        print("-----------")
        print("|    0    |")
        print("|    0    |")
        print("|    0    |")
        print("-----------")

    elif numero == 4:
        print("-----------")
        print("| 0     0 |")
        print("|         |")
        print("| 0     0 |")
        print("-----------")

    elif numero == 5:
        print("-----------")
        print("| 0     0 |")
        print("|    0    |")
        print("| 0     0 |")
        print("-----------")

    elif numero == 6:
        print("-----------")
        print("| 0  0  0 |")
        print("|         |")
        print("| 0  0  0 |")
        print("-----------")


print("                    Simulador de dados                  ")
x = 's'
while x.lower() == "s":
    roll_dice()             # function call
    choice = input("Você quer jogar novamente? (s/n): ")       # choice from user

    if choice.lower() == "n":
        exit(0)
