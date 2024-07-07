import time


#FUNCTIONS

sPATTACK = 0        #Amount of sP applied in ATK
spDEFENCE = 0       #Amount of sP applied in DEF
sPSPEED = 0         #Amount of sP applied in SPD
sPINTELLIGENCE = 0  #Amount of sP applied in INT
sPHP = 0            #Amount of sP applied in HP

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

#FUNCTIONS END


ClassName = ["TEST","Warrior","Archer","Tank","Mage","Paladin","Arbalist","Mech","Pyromancer","Assasin","Sheriff","Air Bomber","Necromancer"]
ClassData = [
                [0, 0, 100, 0, 0, 0, 10, 0, 0], #SELECTION CLASS
                [3, 3, 97, 1, 15, 0, 10, 0, 0], #Warrior
                [4, 2, 95, 1, 10, 0, 10, 0, 0], #Archer
                [3, 4, 99, 1, 25, 0, 10, 0, 0], #Tank
                [4, 2, 97, 2, 10, 0, 10, 0, 0], #Mage
                [4, 5, 95, 1, 20, 0, 10, 0, 0], #Paladin
                [6, 3, 98, 1, 25, 0, 10, 0, 0], #Arbalist
                [6, 5, 95, 1, 35, 0, 10, 0, 0], #Mech
                [4, 4, 95, 2, 10, 0, 10, 0, 0], #Pyromancer
                [4, 4, 95, 1, 10, 0, 10, 0, 0], #Assasin
                [4, 4, 95, 1, 10, 0, 10, 0, 0], #Sheriff
                [4, 4, 95, 1, 10, 0, 10, 0, 0], #Air bomber
                [4, 4, 95, 2, 10, 0, 10, 0, 0]  #Necromancer
                #Attack, Defence, Speed, Intelligence, Health, XP obtained, XP required, Level, sP obtained
                ]
#TEST
#x = int(input("Input a value to add to the XP: "))
#ClassData[0][5] += x
#TESTEND
sleepTime = 0.1
slowText("Loading.....................\n")
slowText("Patching up resources.......\n")
slowText("Clearing cache..............\n")
sleepTime = 0.05
savefileInput = input(print("Hello, user! Do you have a savefile you would like to load? (Y/N): "))
if savefileInput == "Y":
    savefilePath = input(print("Type out the path in which you have your save-file: "))
    savefile = open(savefilePath, "rt")
    print(savefile)
elif savefileInput == "N":
    savefileName = input(print("We will be creating one for you. Name your save: "))
    savefile = open(savefileName, "x")
    print(savefile)
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