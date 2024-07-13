import time
import math
import random


#VARIABLES

sPATTACK = 0        #Amount of sP applied in ATK
spDEFENCE = 0       #Amount of sP applied in DEF
sPSPEED = 0         #Amount of sP applied in SPD
sPINTELLIGENCE = 0  #Amount of sP applied in INT
sPHP = 0            #Amount of sP applied in HP
playMode = "x"

#FUNCTIONS

def sPASSIGNMENT():
    global sPATTACK
    global spDEFENCE
    global sPSPEED
    global sPINTELLIGENCE
    global sPHP
    SPUsage = input("You have levelled up! Would you like to use you sP now? (Y/N): ")
    if SPUsage == "Y":
        print("Which attribute would you like to add it to?")
        print("ATK: " + str(sPATTACK))
        print("DEF: " + str(spDEFENCE))
        print("SPD: " + str(sPSPEED))
        print("INT: " + str(sPINTELLIGENCE))
        print("HP: " + str(sPHP))
        spUSE = input("Type the attribute's name here: ")
        if spUSE == "ATK":
            sPATTACK += 1
        elif spUSE == "DEF":
            spDEFENCE += 1
        elif spUSE == "SPD":
            sPSPEED += 1
        elif spUSE == "INT":
            sPINTELLIGENCE += 1
        elif spUSE == "HP":
            sPHP += 1
        else:
            print("It will be cancelled. Try with the command.")
    else:
        print("It will be cancelled. Try with the command.")
    #return sPATTACK, spDEFENCE, sPSPEED, sPINTELLIGENCE, sPHP

def attributeOutPut():
    print("ATK: " + str(sPATTACK))
    print("DEF: " + str(spDEFENCE))
    print("SPD: " + str(sPSPEED))
    print("INT: " + str(sPINTELLIGENCE))
    print("HP: " + str(sPHP))

def userStatsOutPut():
    print("HP: " + str(sPATTACK))

def slowText(text):
    global sleepTime
    for char in text:
        print(char, end='', flush=True)
        time.sleep(sleepTime)

def classSelection():
    global selectedClass
    sleepTime = 0.03
    slowText("Please note the weaknesses listed below: \n")
    slowText("Warriors are stronger against Archers.\n")
    slowText("Archers are stronger against Tanks.\n")
    slowText("Tanks are stronger against Warriors.\n")
    slowText("Mages are weaker against other classes, but also do more damage against other classes.\n")
    selectedClass = input("Here are four classes you can select from: \n - warrior \n - archer \n - tank \n - mage\nWhich class would you like to choose: ")
    if selectedClass == "warrior":
        for classSelectionLoop in range(0, 9):
            ClassData[0][classSelectionLoop] = ClassData[1][classSelectionLoop]
    elif selectedClass == "archer":
        for classSelectionLoop in range(0, 9):
            ClassData[0][classSelectionLoop] = ClassData[2][classSelectionLoop]
    elif selectedClass == "tank":
        for classSelectionLoop in range(0, 9):
            ClassData[0][classSelectionLoop] = ClassData[3][classSelectionLoop]
    elif selectedClass == "mage":
        for classSelectionLoop in range(0, 9):
            ClassData[0][classSelectionLoop] = ClassData[4][classSelectionLoop]
    else:
        slowText("Typo? Select again.\n")
        classSelection()

def menu():
    global sleepTime
    global playMode
    global savefileInput
    global savefileName
    global savefile
    sleepTime = 0.05
    slowText("Hello user, to the game!\n")
    slowText("What mode would you like to play today?\n")
    playMode = input("Lonely... I'm so lonely... (singleplayer)         Friends! (multiplayer)\n")
    if playMode == "singleplayer":
        savefileInput = input("Great, loner! Do you have a savefile? (Y/N): ")
        if savefileInput == "Y":
            savefilePath = input("What is the name of your save: ")
            with open(savefilePath, "rt") as savefile:
                print(savefile.read())
        else:
            savefileName = input("We will be creating one for you. Name your save: ")
            with open(savefileName, "xt") as savefile:
                classSelection()
                for j in range(0, 9):
                    savefile.write(f"{ClassData[0][j]}\n")
    elif playMode == "multiplayer":
        slowText("On BETA phase. Please try again after the next update. Thank you!")
        menu()
    else:
        slowText("Wrong input? We will take you to the menu. Please don't do it again.\n")
        menu()

#ARRAYS

ClassName = ["TEST","Warrior","Archer","Tank","Mage","Paladin","Arbalist","Mech","Pyromancer","Assasin","Sheriff","Air Bomber","Necromancer"]
ClassData = [
                 [0, 0, 100, 0, 0, 0, 10, 0, 0], #SELECTION CLASS
                #ORIGINALS
                 [3, 3, 97, 1, 15, 0, 10, 0, 0], #Warrior
                 [4, 2, 95, 1, 10, 0, 10, 0, 0], #Archer
                 [3, 4, 99, 1, 25, 0, 10, 0, 0], #Tank
                 [4, 2, 97, 2, 10, 0, 10, 0, 0], #Mage
                #VARIANTS S1
                 [6, 7, 94, 2, 30, 0, 10, 0, 0], #Paladin
                 [8, 4, 96, 2, 25, 0, 10, 0, 0], #Arbalist
                 [6, 5, 95, 2, 50, 0, 10, 0, 0], #Mech
                 [9, 5, 94, 4, 20, 0, 10, 0, 0], #Pyromancer
                #VARIANTS S2
                 [5, 4, 92, 2, 25, 0, 10, 0, 0], #Assasin
                 [7, 5, 94, 2, 25, 0, 10, 0, 0], #Sheriff
                [10, 3, 97, 2, 40, 0, 10, 0, 0], #Air bomber
                 [4, 3, 95, 4, 25, 0, 10, 0, 0]  #Necromancer
                #Attack, Defence, Speed, Intelligence, Health, XP obtained, XP required, Level, sP obtained
                ]

EnemyName = ["TEST", "Ant", "Skeleton Warrior", "Skeleton Archer", "Miltank", "Horness", "Kraken", "Siren"]
EnemyData = [
                [0, 0, 100, 0, 0],   #TEST
                [1, 0, 99, 1, 3],    #Ant
                #Birth Guardian
                [5, 6, 95, 2, 25],   #Skeleton Warrior
                [7, 4, 94, 3, 20],   #Skeleton Archer
                #Skeletor
                [6, 8, 97, 4, 30],   #Miltank
                [9, 4, 94, 5, 20],   #Horness
                #Minotaur
                [6, 9, 90, 6, 40],   #Siren
                [12, 10, 93, 8, 35], #Kraken
                #Poseidon
                #Attack, Defence, Speed, XP Drop, Health
]

BossName = ["TEST", "Birth Guardian", "Skeletor", "Minotaur", "Poseidon"]
BossData = [
                [0, 0, 100, 0, 0],     #TEST
                [3, 2, 98, 9, 10],     #Birth Guardian
                [10, 5, 95, 20, 35],   #Skeletor
                [15, 8, 92, 40, 50],   #Minotaur
                [25, 15, 88, 55, 75],  #Poseidon
                #Attack, Defence, Speed, XP Drop, Health
]
#TEST
#x = int(input("Input a value to add to the XP: "))
#ClassData[0][5] += x
#TESTEND
sleepTime = 0.1
slowText("Loading..............\n")
slowText("Patching up resources.......\n")
slowText("Booting v1.0.1...........\n")
menu()
#TEST
#i = 0
#for i in range(len(ClassData)):
#    if ClassData[i][5] >= ClassData[i][6]:
#        sPASSIGNMENT()
#        ClassData[i][5] -= ClassData[i][6]
#        ClassData[i][6] *= 1.2
#        ClassData[i][7] += 1
#        ClassData[i][8] += 1
#attributeOutPut()
#TESTEND