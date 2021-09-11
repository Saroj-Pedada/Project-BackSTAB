import Bollywood_Game 
import BINGO_Game 
import Snake_Water_Gun_Game 
import Tollywood_Game 
print("\n\nHello Guys ! Thank you for playing Back-STAB . This game consists of 4 mini games .")

while True :
    print("\n")
    print("--> Snake , Water and Gun game (S) ")
    print("--> TollWood game (T) ")
    print("--> BollWood game (B) ")
    print("--> BINGO game (BINGO) ")
    print("--> To Exit (E) ")
    print("\n")
    game_to_play = input("Enter the words given to play the corresponding game : ")
    if game_to_play == "s" or game_to_play == "S" :
        print("\n\n")
        Snake_Water_Gun_Game.SWG()
        continue
    elif game_to_play == "T" or game_to_play == "t" :
        print("\n\n")
        Tollywood_Game.Tollywood()
        continue
    elif game_to_play == "B" or game_to_play == "b" :
        print("\n\n")
        Bollywood_Game.Bollywood()
        continue
    elif game_to_play == "BINGO" or game_to_play == "bingo" or game_to_play == "Bingo" :
        print("\n\n")
        coru = input("Enter \"C\" if you want to play BINGO with computer generated matrix or else enter \"U\" if you want to play BINGO with your own matrix : ")
        if coru == "C" or coru == "c" :
            addiction_value = False
        elif coru == "U" or coru == "u" :
            addiction_value = True
        else :
            print("\n\n\t\t\t\tError 404 ! Please restart the program .\n\n")
            break
        BINGO_Game.BINGO(addiction_value)
        continue
    elif game_to_play == "E" or game_to_play == "e" :
        print("\n\n\t\t\t\tThank You for playing . \n\n")
        break
    else :
        print("\n\n\t\t\t\tError 404 ! Please restart the program .\n\n")
        break
