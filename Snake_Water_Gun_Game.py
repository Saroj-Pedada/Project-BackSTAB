import random
def SWG() :
    while True :
        a = ["snake", "gun", "water"]
        print("The computer has chosen its choice .\nType your choice as (\"snake\" or \"gun\" or \"water\" or \"E\" to exit).")
        b = input("Snake , Gun or Water : ")
        c = random.choice(a)
        if b == "snake" and c=="water" :
            print("The computer chose : " + c)
            print("YOU WIN !")
            print("\n")
            continue
        if b == "water" and c=="snake" :
            print("The computer chose : " + c)
            print("YOU LOSE !")
            print("\n")
            continue
        if b == "water" and c=="gun" :
            print("The computer chose : " + c)
            print("YOU WIN !")
            print("\n")
            continue
        if b == "gun" and c=="water" :
            print("The computer chose : " + c)
            print("YOU LOSE !")
            print("\n")
            continue
        if b == "gun" and c=="snake" :
            print("The computer chose : " + c)
            print("YOU WIN !")
            print("\n")
            continue
        if b == "snake" and c=="gun" :
            print("The computer chose : " + c)
            print("YOU LOSE !")
            print("\n")
            continue
        if b == c :
            print("The computer chose : " + c)
            print("TIE !")
            print("\n")
            continue
        if b == "E" or "e" :
            print("\n\n\t\t\tThank you for playing !\n\n")
            break
        else :
            print("\n\n\t\t\t\tError 420 ! Try restarting the program .\n\n")
            break
