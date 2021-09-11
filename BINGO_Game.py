import Sublist
import Sorter
import random
def BINGO(addiction) :
    while addiction == True :
        print("\n\n\t\t\tLets Play BINGO!\n\n")    
        Player1 = input("Enter the name of Player 1 : ")
        Player2 = input("Enter the name of Player 2 : ")
        n = int(input("\n\nEnter the number of rows / columns : "))    
        slots = []
        for x in range(n) :
            slots.append(((x+1)*n)-n)
        naturality = []
        for y in range(n*n) :
            naturality.append(y+1)
        print("\n\nEnter the elements row by row ("+Player1+") : \n")
        bingo1 = [[0 for p in range(n)] for q in range(n)]
        for i in range(n) :
            for j in range(n) :
                bingo1[i][j] = int(input())
        sleep1 = [bingo1[i][j] for i in range(n) for j in range(n)]
        sleep1.sort()
        print("\n\nEnter the elements row by row ("+Player2+") : \n")
        bingo2 = [[0 for i in range(n)] for j in range(n)]
        for p in range(n) :
            for q in range(n) :
                bingo2[p][q] = int(input())
        sleep2 = [bingo2[i][j] for i in range(n) for j in range(n)]
        sleep2.sort()
        if sleep1 == naturality and sleep2 == naturality :
            row_matrix1 = []
            for a in range(n) :
                row_matrix1.append(bingo1[a])    
            row_matrix2 = []
            for b in range(n) :
                row_matrix2.append(bingo2[b])
            column_matrix1 = []
            additional1 = []
            for c in range(n) :
                for d in range(n) :
                    additional1.append(bingo1[d][c])
            column_matrix1 = [additional1[i:i+n] for i in slots]
            column_matrix2 = []
            additional2 = []
            for c in range(n) :
                for d in range(n) :
                    additional2.append(bingo2[d][c])
            column_matrix2 = [additional2[j:j+n] for j in slots]
            diagonal_matrix1 = []
            diagonal_matrix2 = []
            for a in range(n) :
                for b in range(n) :
                    if a == b :
                        diagonal_matrix1.append(bingo1[a][b])
                    if a + b == n-1 :
                        diagonal_matrix2.append(bingo1[a][b])
            diagonal1 = []
            diagonal1.append(diagonal_matrix1)
            diagonal1.append(diagonal_matrix2)
            diagonal_matrix3 = []
            diagonal_matrix4 = []
            for a in range(n) :
                for b in range(n) :
                    if a == b :
                        diagonal_matrix3.append(bingo2[a][b])
                    if a + b == n-1 :
                        diagonal_matrix4.append(bingo2[a][b])
            diagonal2 = []
            diagonal2.append(diagonal_matrix3)
            diagonal2.append(diagonal_matrix4)
            row_matrix1 = Sorter.sortByRow(row_matrix1,n,True)
            row_matrix2 = Sorter.sortByRow(row_matrix2,n,True)
            column_matrix1 = Sorter.sortByRow(column_matrix1,n,True)
            column_matrix2 = Sorter.sortByRow(column_matrix2,n,True)
            diagonal1 = Sorter.sortByRow(diagonal1,2,True)
            diagonal2 = Sorter.sortByRow(diagonal2,2,True)
            input_numbers = []
            lists = []
            while True :
                number = int(input("\nEnter a number : "))
                if number <= n*n :
                    input_numbers.append(number)
                    input_numbers.sort()
                    count1 = 0
                    count2 = 0
                    if len(input_numbers) >= n :
                        lists = Sublist.choose_sets(input_numbers,n)
                    for x in range(n) :
                        if row_matrix1[x] in lists :
                            count1 = count1 + 1
                        if column_matrix1[x] in lists :
                            count1 = count1 + 1    
                        if row_matrix2[x] in lists :
                            count2 = count2 + 1
                        if column_matrix2[x] in lists :
                            count2 = count2 + 1    
                    if diagonal1[0] in lists :
                        count1 = count1 + 1
                    if diagonal1[1] in lists :
                        count1 = count1 + 1
                    if diagonal2[0] in lists :
                        count2 = count2 + 1
                    if diagonal2[1] in lists :
                        count2 = count2 + 1
                    if count1 >= n and count2 < n :
                        print("\n\n\t\t\t\tBINGOOOOO!!!")
                        print("\n\n\t\t\t"+Player1+" is the winner . Congratulations  !!! \n\n")
                        break
                    elif count2 >= n and count1 < n :
                        print("\n\n\t\t\t\tBINGOOOOO!!!")
                        print("\n\n\t\t\t"+Player2+" is the winner . Congratulations  !!! \n\n")
                        break
                    elif count1 >=n and count2 >= n :
                        print("\n\n\t\tGuys its a TIE ! Nice One !\n\n")
                        break
                    else :
                        print("\n\t\t\t"+Player1+"\'s score is "+str(count1))
                        print("\t\t\t"+Player2+"\'s score is "+str(count2))
                        continue
                else :
                    print("\n\n\t\tError 420 ! Try restarting the program .\n\n")
                    print("\n\n")
                    break
        else :
            print("\n\n\t\tError 504 ! Please restart the program .\n\n")
            break
        yn = input("\n\nEnter \"Y\" to restart the program or \"N\" to exit : ")
        if yn == "Y" or yn == "y" :
            print("\n\n")
            continue
        elif yn == "N" or yn == "n" :
            print("\n\n")
            break
        else :
            print("\n\n\t\tError 504 ! Please restart the program .\n\n")
            print("\n\n")
            break
    while addiction == False :
        print("\n\n\t\t\tLets Play BINGO!\n\n")    
        Player1 = input("Enter the name of Player 1 : ")
        Player2 = input("Enter the name of Player 2 : ")
        n = int(input("\n\nEnter the number of rows / columns : "))    
        slots = []
        for x in range(n) :
            slots.append(((x+1)*n)-n)
        saroj = [x+1 for x in range(n*n)]
        random.shuffle(saroj)
        bingo1 = [saroj[a:a+n] for a in slots]
        saroj = [y+1 for y in range(n*n)]
        random.shuffle(saroj)
        bingo2 = [saroj[b:b+n] for b in slots]
        if bingo1 != bingo2 :
            row_matrix1 = []
            for a in range(n) :
                row_matrix1.append(bingo1[a])    
            row_matrix2 = []
            for b in range(n) :
                row_matrix2.append(bingo2[b])
            column_matrix1 = []
            additional1 = []
            for c in range(n) :
                for d in range(n) :
                    additional1.append(bingo1[d][c])
            column_matrix1 = [additional1[i:i+n] for i in slots]
            column_matrix2 = []
            additional2 = []
            for c in range(n) :
                for d in range(n) :
                    additional2.append(bingo2[d][c])
            column_matrix2 = [additional2[j:j+n] for j in slots]
            diagonal_matrix1 = []
            diagonal_matrix2 = []
            for a in range(n) :
                for b in range(n) :
                    if a == b :
                        diagonal_matrix1.append(bingo1[a][b])
                    if a + b == n-1 :
                        diagonal_matrix2.append(bingo1[a][b])
            diagonal1 = []
            diagonal1.append(diagonal_matrix1)
            diagonal1.append(diagonal_matrix2)
            diagonal_matrix3 = []
            diagonal_matrix4 = []
            for a in range(n) :
                for b in range(n) :
                    if a == b :
                        diagonal_matrix3.append(bingo2[a][b])
                    if a + b == n-1 :
                        diagonal_matrix4.append(bingo2[a][b])
            diagonal2 = []
            diagonal2.append(diagonal_matrix3)
            diagonal2.append(diagonal_matrix4)
            input_numbers = []
            lists = []
            print("\n\n\t\t\t\t"+Player1+"'s BINGO matrix is : \n\n")
            for a in range(n) :
                for b in range(n) :
                    print("\t"+str(bingo1[a][b]),end="")
                print("\n")
            print("\n\n\t\t\t\t"+Player2+"'s BINGO matrix is : \n\n")
            for a in range(n) :
                for b in range(n) :
                    print("\t"+str(bingo2[a][b]),end="")
                print("\n\n")
            print("\n\n\n\t\t\tCopy the above layout and start playing the game .")
            row_matrix1 = Sorter.sortByRow(row_matrix1,n,True)
            row_matrix2 = Sorter.sortByRow(row_matrix2,n,True)
            column_matrix1 = Sorter.sortByRow(column_matrix1,n,True)
            column_matrix2 = Sorter.sortByRow(column_matrix2,n,True)
            diagonal1 = Sorter.sortByRow(diagonal1,2,True)
            diagonal2 = Sorter.sortByRow(diagonal2,2,True)
            while True :
                number = int(input("\nEnter a number : "))
                if number <= n*n :
                    input_numbers.append(number)
                    input_numbers.sort()
                    count1 = 0
                    count2 = 0
                    if len(input_numbers) >= n :
                        lists = Sublist.choose_sets(input_numbers,n)
                    for x in range(n) :
                        if row_matrix1[x] in lists :
                            count1 = count1 + 1
                        if column_matrix1[x] in lists :
                            count1 = count1 + 1    
                        if row_matrix2[x] in lists :
                            count2 = count2 + 1
                        if column_matrix2[x] in lists :
                            count2 = count2 + 1    
                    if diagonal1[0] in lists :
                        count1 = count1 + 1
                    if diagonal1[1] in lists :
                        count1 = count1 + 1
                    if diagonal2[0] in lists :
                        count2 = count2 + 1
                    if diagonal2[1] in lists :
                        count2 = count2 + 1
                    if count1 >= n and count2 < n :
                        print("\n\n\t\t\t\tBINGOOOOO!!!")
                        print("\n\n\t\t\t"+Player1+" is the winner . Congratulations  !!! \n\n")
                        break
                    elif count2 >= n and count1 < n :
                        print("\n\n\t\t\t\tBINGOOOOO!!!")
                        print("\n\n\t\t\t"+Player2+" is the winner . Congratulations  !!! \n\n")
                        break
                    elif count1 >=n and count2 >= n :
                        print("\n\n\t\tGuys its a TIE ! Nice One !\n\n")
                        break
                    else :
                        print("\n\t\t\t"+Player1+"\'s score is "+str(count1))
                        print("\t\t\t"+Player2+"\'s score is "+str(count2))
                        continue
                else :
                    print("\n\n\t\tError 420 ! Try restarting the program .\n\n")
                    print("\n\n")
                    break
        else :
            print("\n\n\t\tError 504 ! Please restart the program .\n\n")
            break
        yn = input("\n\nEnter \"Y\" to restart the program or \"N\" to exit : ")
        if yn == "Y" or yn == "y" :
            print("\n\n")
            continue
        elif yn == "N" or yn == "n" :
            print("\n\n")
            break
        else :
            print("\n\n\t\tError 504 ! Please restart the program .\n\n")
            print("\n\n")
            break
