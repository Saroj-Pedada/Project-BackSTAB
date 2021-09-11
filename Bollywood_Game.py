import random
import re
import movslist
def Bollywood():
    while True :
        print("\n\n\t\t\t\"A\" is for adding any new movies.")
        print("\t\t\t\"P\" is for playing the game.")
        user_input = input("\n\t\t\tEnter any character (P/A) : ")
        if str(user_input) == "P" or str(user_input) == "p" :
            ord_name = []
            mov_name = []
            print("\n\n\t\t\tLets Play BOLLYWOOD!\n\n")
            mov_selected = random.choice(movslist.Movies)
            unilen = len(set(mov_selected))
            length = len(mov_selected)
            for m in range(length) :
                ord_name.append(ord(str(mov_selected[m])))
            ord_name = sorted(ord_name)
            ord_name = list(dict.fromkeys(ord_name))
            print("The number of letters in the name of the movie are (may/mayn't include space) "+str(length)+".")
            count_of_loss = 0
            test_str = mov_selected
            test_sub = " "
            res = [i.start() for i in re.finditer(test_sub, test_str)]
            numoftimes = len(res)
            tin = []
            for f in range(numoftimes) :
                tin.append(res[f]+1)
            if numoftimes == 0 :
                print(length*" _ ")
                print("\n\n\t\tCopy the above layout and start guessing. Good Luck!\n\n")
            if numoftimes == 1 :
                print((tin[0]-1)*" _ "+" | "+(length-tin[0])*" _ ")
                print("\n\n\t\tCopy the above layout and start guessing. Good Luck!\n\n")
            if numoftimes == 2 :
                print((tin[0]-1)*" _ "+" | "+(tin[1]-tin[0]-1)*" _ "+" | "+(length-tin[1])*" _ ")
                print("\n\n\t\tCopy the above layout and start guessing. Good Luck!\n\n")
            if numoftimes == 3 :
                print((tin[0]-1)*" _ "+" | "+(tin[1]-tin[0]-1)*" _ "+" | "+(tin[2]-tin[1]-1)*" _ "+" | "+(length-tin[2])*" _ ")
                print("\n\n\t\tCopy the above layout and start guessing. Good Luck!\n\n")
            if ord(" ") in ord_name :
                mov_name.append(ord(" "))
            for x in range(0,10+unilen-numoftimes) :
                mov_name = sorted(mov_name)
                if count_of_loss < 10 and mov_name == ord_name :
                    yn = input("You have exceeded the maximum number of trials. If you got the movie name type Y(YES) or N(NO) : ")
                    if str(yn) == "Y" or str(yn) == "y" :
                        ans = input("\n\t\tEnter the movie name : ")
                        if str(ans) == str(mov_selected) :
                            print("\n\n\t\tYAY ! You won the game.")
                            break
                        else :
                            print("\n\n\t\tYou Lose! Better Luck Next Time.")
                            print("\t\tThe name of the movie is "+mov_selected+".")
                            break
                    elif str(yn) == "N" or str(yn) == "n" :
                        print("\n\n\t\tYou Lose! Better Luck Next Time.")
                        print("\t\tThe name of the movie is "+mov_selected+".")
                        break
                    else :
                        print("\n\n\t\tERROR 504! Please restart The program.\n\n")
                        break
                if count_of_loss == 10 and ord_name != mov_name:
                    print("\n\n\t\tYou Lose! Better Luck Next Time.")
                    print("\t\tThe name of the movie is "+mov_selected+".")
                    break
                a = input("Enter any letter : ")
                for y in range(length) :
                    if str(a) == str(mov_selected[y]) :
                        print("Correct Guess! It is in position number "+str(y+1)+".")
                        mov_name.append(ord(str(a)))
                        mov_name = list(dict.fromkeys(mov_name))
                if str(a) not in str(mov_selected) :
                    count_of_loss+=1
                    print("Not present in the title. You lost a chance. You still have "+str(9-count_of_loss+1)+" chances left.")
        elif str(user_input) == "A" or str(user_input) == "a" :
            while True :
                nameofmov = input("\n\t\tEnter the name of the movie to add : ")
                f = open("movslist.py", "a")
                f.write("\nMovies.append(\""+nameofmov+"\")\nMovies = list(dict.fromkeys(Movies))")
                f.close()
                print("\n\n\t\t\tThank You For Adding")
                ny = input("\n\t\tIf you want to add more , press Y(YES) or N(NO) : ")
                if str(ny) == "Y" or str(ny) == "y" :
                    continue
                elif str(ny) == "N" or str(ny) == "n" :
                    break
                else :
                    print("\n\n\t\tERROR 504! Please restart the program\n\n\n")
                    break
        else :
            print("\n\n\t\tERROR 504! Please restart the program\n\n\n")
        yon = input("\n\n\tPress Y(YES) to restart the program or N(NO) to stop : ")
        if str(yon) == "Y" or str(yon) == "y" :
            continue
        elif str(yon) == "N" or str(yon) == "n" :
            print("\n\n\t\tThank You For Playing !\n\n\n")
            break
        else :
            print("\n\n\t\tERROR 504! Please restart the program\n\n\n")
            break
