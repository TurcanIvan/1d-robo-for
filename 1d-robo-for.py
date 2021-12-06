# REMAKE   1d robo game -> for loop

from os import system


RoboX   = 5
RoboHP  = 100
RoboBT  = 100
bombX   = 8
bombX1  = 3
Battery = 1
heart   = 10
Score   = 1000

LENGTH = 10
option = ""

#game loop
while True:
    ################### 1. DRAW MAP ##############
    system("cls")
    print("\n")

    for x in range(1,LENGTH +1):  # 1..10
        if x == RoboX:
            print("🤖",end=" ")
        elif x == bombX or x == bombX1:
            print("💣",end= " ")   
        elif x == heart:
            print("🖤",end= " ")
        elif x ==  Battery:
            print("🔋",end= " ")
        else:
            print(".",end=" ")
        

    print("\nHP:", RoboHP)
    print("BT:", RoboBT)
    print("Score:", Score)
    print("\n")
    ################### 1. DRAW MAP ################

    ################### 2. READ INPUT ##############
    option = input(">>> ")
    ################### 2. READ INPUT ##############


    ################### 3. DECIDE ##################
    if option == "a" and RoboX > 1 : # move left
        RoboX -= 1
        RoboBT -= 1
    if option == "d" and RoboX < 10: # move right HW+
        RoboX += 1
        RoboBT -= 1

    # check if bombX or bombX1
    if RoboX == bombX and RoboHP > 0:
        bombX   = False
        RoboHP -= 10
        Score  -= 100
    if RoboX == bombX1 and RoboHP > 0:
        bombX1   = False
        RoboHP -= 10
        Score  -= 100   
    elif RoboX == bombX or RoboX == bombX1 and RoboHP == 0:
        print("GAME OVER!!")
        break
    if RoboX == heart:
        RoboHP += 10
        heart = False
    if RoboX == Battery:
        RoboBT += 5
        Battery = False             
    if option == "x": #eXit
        system("cls")
        print("Thank you for playning! :)")
        break     
    ################### 3. DECIDE ##############

    # HW1: frontier check RIGHT
    # HW2: place second bomb
    # HW3*: place some hearts -> HP +
    # HW4*: place some coins -> score
    # HW5*: add variable -> state of boms,coins,...


    # game loop:
    #     1. draw the map
    #     2. read the input
    #     3. decide  