# REMAKE   1d robo game -> for loop

from os import system


RoboX = 5
LENGTH = 10
option = ""
#game loop
while True:
    ################### 1. DRAW MAP ##############
    system("cls")
    print("\n")

    for x in range(1,LENGTH +1):  # 1..10
        if x == RoboX:
            print("R",end=" ")
        else:
            print(".",end=" ")
        


    print("\n")
    ################### 1. DRAW MAP ################

    ################### 2. READ INPUT ##############
    option = input(">>> ")
    ################### 2. READ INPUT ##############


    ################### 3. DECIDE ##################
    if option == "a": # move left
        RoboX -= 1
    if option == "d": # move right
        RoboX += 1
    if option == "x": #eXit
        system("cls")
        print("Thank you for playning! :)")
        break
       



    ################### 3. DECIDE ##############





    # game loop:
    #     1. draw the map
    #     2. read the input
    #     3. decide  