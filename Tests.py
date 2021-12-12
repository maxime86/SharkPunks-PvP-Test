import PvP
from SharkPunk import SharkPunk
import copy

def TestXGames(x, s1, s2):
    
    totalDamageShark1 = 0.0
    totalDamageShark2 = 0.0
    totalmissedShark1 = 0.0
    totalmissedShark2 = 0.0
    totalnumberofTurns = 0.0
    numberOfWinShark1 = 0.0
    numberOfStartShark1 = 0.0
    numberOfStartShark2 = 0.0
    numberOfwinWhenStartShark1 = 0.0
    numberOfwinWhenStartShark2 = 0.0
    numberOfWinShark2 = 0.0
    numberOfWinStartingShark = 0.0

    for i in range(1, x + 1):

        shark1 = copy.copy(s1)
        shark2 = copy.copy(s2)
        winner = PvP.Game(shark1, shark2, False, False, False)
        totalDamageShark1 += PvP.damageMadeByPlayer1
        totalDamageShark2 += PvP.damageMadeByPlayer2
        totalmissedShark1 +=  PvP.attackMissedByShark1
        totalmissedShark2 +=  PvP.attackMissedByShark2
        totalnumberofTurns += PvP.numberofTurns

        if winner == "Shark 1": numberOfWinShark1 += 1 
        else: numberOfWinShark2 += 1

        if PvP.startingShark == winner: numberOfWinStartingShark +=1

        if PvP.startingShark == "Shark 1":
            numberOfStartShark1 += 1
            if winner == "Shark 1":
                numberOfwinWhenStartShark1 +=1
        if PvP.startingShark == "Shark 2":
            numberOfStartShark2 += 1
            if winner == "Shark 2":
                numberOfwinWhenStartShark2 +=1

    print("")
    print("-------------------------")
    print("Number of games = {}".format(x))
    print("Average number of turns = {}".format(totalnumberofTurns/x))
    print("Average % Win by starting Shark = {}%".format(numberOfWinStartingShark*100/x))

    print("")
    print("---------Shark 1---------")
    print("Damages made by Shark 1 = {}".format(totalDamageShark1))
    print("Average damages made by Shark 1 = {}".format(totalDamageShark1/x))
    print("Attack missed by Shark 1 = {}".format(totalmissedShark1/x))
    print("Number of wins Shark 1 = {}".format(numberOfWinShark1))
    print("% win Shark 1 = {}%".format(numberOfWinShark1*100/x))
    print("% win when Shark 1 starts = {}%".format(numberOfwinWhenStartShark1*100 / numberOfStartShark1))
    print("")
    print("---------Shark 2---------")
    print("Damages made by Shark 2 = {}".format(totalDamageShark2))
    print("Average damages made by Shark 2 = {}".format(totalDamageShark2/x))
    print("Attack missed by Shark 2 = {}".format(totalmissedShark2/x))
    print("Number of wins Shark 2 = {}".format(numberOfWinShark2))
    print("% win Shark 2 = {}%".format(numberOfWinShark2*100/x))
    print("% win when Shark 2 starts = {}%".format(numberOfwinWhenStartShark2*100 / numberOfStartShark2))


shark1 = SharkPunk(0, 0, "Gun", "Gun", 1, 0)
shark2 = SharkPunk(0, 0, "Hand", "Hand", 1, 0)
TestXGames(1000, shark1, shark2)