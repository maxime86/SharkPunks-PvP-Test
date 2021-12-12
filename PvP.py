from SharkPunk import SharkPunk
import random
import Functions


def Turn(player1, player2):
    
    global sharkAttacking, sharkDefending

    sharkAttacking = "Shark 1" if player1.attackNext else "Shark 2"
    sharkDefending = "Shark 2" if player1.attackNext else "Shark 1"

    if player1.attackNext :
        damage = Functions.Attack(player1.pm, player1.am, player2.dm)
        player2.hp = max(0, player2.hp - damage)
        player2.attackNext = True
        player1.attackNext = False
    else: 
        damage = Functions.Attack(player2.pm, player2.am, player1.dm)
        player1.hp = max(0, player1.hp - damage)
        player1.attackNext = True
        player2.attackNext = False

    return damage


def Game(player1, player2, viewSharkDesc, viewDetails, viewStats):

    global damageMadeByPlayer2 
    global damageMadeByPlayer1
    global attackMissedByShark2 
    global attackMissedByShark1
    global numberofTurns
    global startingShark
    damageMadeByPlayer2 = 0.0
    damageMadeByPlayer1 = 0.0
    attackMissedByShark2 = 0.0
    attackMissedByShark1 = 0.0
    startingShark = ""


    if viewSharkDesc: 
        print("----- Shark 1 -----")
        print("Shark has Helmet = True")
        print("Shark has Glasses = True")
        print("Shark Right Weapon = Hand")
        print("Shark Left Weapon = Bazooka")
        print("Shark has Armor = True")
        print("")
        print("----- Shark 2 -----")
        print("Shark has Helmet = False")
        print("Shark has Glasses = False")
        print("Shark Right Weapon = Hand")
        print("Shark Left Weapon = Hand")
        print("Shark has Armor = True")
        print("")

    """Determine which player start"""
    if random.randint(1, 2) == 1 :
        player1.attackNext = True
        startingShark = "Shark 1"
        if viewDetails : print("Shark 1 starts")
    else :    
        player2.attackNext = True
        startingShark = "Shark 2"
        if viewDetails : print("Shark 2 starts")
    
    i = 1

    while (player1.hp > 0 and player2.hp > 0) :
        
        if viewDetails and (i % 2) == 1: 
            print("")
            print("----- Turn {} -----".format(round((i+1)/2)))

        damage = Turn(player1, player2)
        if player1.attackNext: damageMadeByPlayer2 += damage
        else: damageMadeByPlayer1 += damage
        i += 1
        if viewDetails:
            print("{} - Attack".format(sharkAttacking))
            if (damage == 0):
                print("{} - Attack missed".format(sharkAttacking))
            else:
                print("{} - {} damages to {}".format(sharkAttacking, damage, sharkDefending))

            print("Shark 1 - HP = {}".format(player1.hp))
            print("Shark 2 - HP = {}".format(player2.hp))
            print("------------------")
            

        if (damage == 0):
            if player1.attackNext: attackMissedByShark2 += 1
            else: attackMissedByShark1 += 1


    if player1.hp > 0 :
        player1.win = True
        if viewDetails or viewStats:             
            print("------------------")
            print("Shark 2 win")
            print("------------------")
    else : 
        player2.win = True
        if viewDetails or viewStats: 
            print("------------------")
            print("Shark 2 win")
            print("------------------")

    numberofTurns = round(i/2)

    if viewStats: 
        print("------------------")
        print("Number of turns = {}".format(round(i/2)))
        print("Damages made by Shark 1 = {}".format(damageMadeByPlayer1))
        print("Damages made by Shark 2 = {}".format(damageMadeByPlayer2))
        print("Attack missed by Shark 1 = {}".format(attackMissedByShark1))
        print("Attack missed by Shark 2 = {}".format(attackMissedByShark2))
        print("Average damages made by Shark 1 = {}".format(damageMadeByPlayer1/(round(i/2))))
        print("Average damages made by Shark 2 = {}".format(damageMadeByPlayer2/(round(i/2))))
        print("------------------")
        print("")

    return "Shark 1" if player1.win == True else "Shark 2"
