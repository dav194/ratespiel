# guessing_game v1.0

import random

def game():
    number = random.randint(1, 100)

    wins = False
    zähler = 0

    while not wins: # alternative: wins == False
        zähler = zähler+1 # Kurzform zähler += 1
        try:
            guess = int(input("Geben Sie eine Zahl zwischen 1 und 100 ein: "))
            if guess < 1 or guess > 100:
                raise ValueError
        except ValueError:
            print("FEHLER: Es können nur Zahlen zwischen 1 und 100 eingegeben werden.")
            continue
        if number == guess:
            print(f"->{number}<- gewinnt! Versuche: {zähler}")
            wins = True
        elif guess > number:
            print("Die gesuchte Zahl ist kleiner.")
        else:
            print("Die gesuchte Zahl ist größer.")
# bis hier ist die Funktion "game()"
#Spiel = True
#while Spiel:
while True:
    game()
    userinput = False
    while not userinput:
        ask = input("Möchten Sie noch mal spielen? [y/n]: ")
        if ask == "y":
            userinput = True
        elif ask == "n":
            exit()
        else:
            print("Nur y oder n eingeben!")
    #else:
        #Spiel = False