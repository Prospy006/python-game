CharacterName = ["N/A", "Ryan", "Harshid", "Steve", "Fawaaz", "Nithilan", "Prospy", "JK"]
CharacterData = [
                [0, 0, 100, 0, 0, 10, 0, 0], #N/A (No class)
                [3, 3, 97, 15, 0, 10, 0, 0], #Ryan (Warrior - Assasin)
                [3, 3, 97, 15, 0, 10, 0, 0], #Harshid (Warrior - Paladin)
                [3, 3, 97, 15, 0, 10, 0, 0], #Steve (Warrior - N/A)
                [2, 5, 99, 25, 0, 10, 0, 0], #Fawaaz (Tank - Air Bomber)
                [4, 4, 95, 10, 0, 10, 0, 0], #Nithilan (Mage - Pyromancer)
                [2, 5, 99, 25, 0, 10, 0, 0], #Prospy (Tank - Mech)
                [4, 4, 95, 10, 0, 10, 0, 0]  #JK (Mage - N/A)
                #Attack, Defence, Speed, Health, XP obtained, XP required, Level, sP obtained
                ]
#TEST
x = int(input("Input a value to add to the XP: "))
CharacterData[0][4] += x
#TESTEND
i = 0
for i in range(len(CharacterData)):
    if CharacterData[i][4] >= CharacterData[i][5]:
        CharacterData[i][4] -= CharacterData[i][5]
        CharacterData[i][5] *= 1.2
        CharacterData[i][6] += 1
        CharacterData[i][7] += 1
print(CharacterData[0][5], CharacterData[0][4])