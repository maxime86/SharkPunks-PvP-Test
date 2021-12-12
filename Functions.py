import random

"""pm stand for Precision Mutliplier"""
"""dm stand for Defense Multiplier"""
"""am stand for Attack Multiplier"""

def Attack(pm, am, dm):
    """This function make one turn of damage"""

    ap = attackPower()
    if precision(pm) == 0: return 0
    
    dp = defensePower()
    return attackDamage(ap,dp, am, dm)
   

def attackDamage(ap, dp, am, dm):
    """This function compute the damage taken by the defender"""
    return int(round((ap - dp) * 15)) * am / dm

def attackPower():
    """This function compute the attack power"""
    return random.uniform(0.70, 1) 

def defensePower():
    """This function compute the defense power"""
    return random.uniform(0, 0.30) 

def precision(pm):
    """This function return the precision
        If 0 then the shot will be missed"""
    p = 1 if random.random() <= (0.92 if pm else 0.90) else 0
    return p






