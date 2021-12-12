class SharkPunk:
    def __init__(self, helmet, glasses, weaponLeft, weaponRight, armor, level):
        self.pm = True if glasses > 0 else False 
        self.dm = getDefenseMultiplier(helmet, armor, level)
        self.am = getAttackultiplier(weaponLeft, weaponRight, level)
        self.hp = getHp(level)
        self.attackNext = False
        self.level = level
        self.xp = 0
        self.win = False

def getDefenseMultiplier(helmet, armor, level):
    dm = 1.0
    if helmet : dm *= 1.1
    if armor : dm *= 1.1
    return dm

def getAttackultiplier(weaponLeft, weaponRight, level):
    am = 1.0
    if weaponLeft != "Hand" : am *= 1.1
    if weaponRight != "Hand" : am *=  1.1
    return am

def getHp(level):
    return 100