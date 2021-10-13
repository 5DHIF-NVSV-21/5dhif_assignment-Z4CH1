import random
import time

print(
"\nSchere-Stein-Papier\n"
"---------------------------------------\n"
)

SSP = ["Schere","Stein","Papier"]

time.sleep(0.5)
print("Regeln:\n")
time.sleep(0.3)
print(">Schere schneidet Papier")
time.sleep(0.3)
print(">Papier umwickelt Stein")
time.sleep(0.3)
print(">Stein  schleift  Schere")
time.sleep(0.3)
print("\n---------------------------------------\n")
time.sleep(0.3)

def Main():

    time.sleep(0.5)
    
    userInput = int(input("Wähle:\n Schere[1]\n Stein [2]\n Papier[3]\n"))
    comInput = random.randint(1,3)  

    print("---------------------------------------\n")

    if userInput == comInput:
        print("Unendschieden!\nDu und der Computer hatten beide",SSP[userInput-1],"\n")
    elif userInput == 1 and comInput == 2:
        print("Du hast leider verloren!\nDu hattest",SSP[userInput-1],"und der Computer hatte",SSP[comInput-1],"\n")
    elif userInput == 1 and comInput == 3:
        print("Du hast gewonnen!\nDu hattest",SSP[userInput-1],"und der Computer hatte",SSP[comInput-1],"\n")
    elif userInput == 2 and comInput == 1:
        print("Du hast gewonnen!\nDu hattest",SSP[userInput-1],"und der Computer hatte",SSP[comInput-1],"\n")
    elif userInput == 2 and comInput == 3:
        print("Du hast leider verloren!\nDu hattest",SSP[userInput-1],"und der Computer hatte",SSP[comInput-1],"\n")
    elif userInput == 3 and comInput == 1:
        print("Du hast leider verloren!\nDu hattest",SSP[userInput-1],"und der Computer hatte",SSP[comInput-1],"\n")
    elif userInput == 3 and comInput == 2:
        print("Du hast gewonnen!\nDu hattest",SSP[userInput-1],"und der Computer hatte",SSP[comInput-1],"\n")
    else:
        print("")

    def restart():
        time.sleep(0.5)
        print("---------------------------------------\n")
        restart = input("Noch eine Runde? Ja[J], Nein[N]\n")
    
        if restart.lower() == "j":
            print("")
            Main()
        elif restart.lower() == "n":
            print("")
        else:
            time.sleep(0.5)
            restart()
    restart()
if __name__ == "__main__":
    Main()