# SharkPunks-PvP-Test
This code written in Python use a very basic logic to implement a very simplified PvP using SharkPunks.
It has been written as a test: refactoring needed


## Summary:
* Allow a PvP battle between 2 SharkPunks. 
* Written in Python there is no UI
* Game played through the *Tests.py*  --> define the attributes of the 2 SharkPunks (Left and right weapons, armor, helmet, glasses)
* *Tests.py* allows to simulate x games with 2 predefined SharkPunks
 
 
## Logic:
* Each SharkPunks starts with 100 HP
* Based on the attributes of each Sharks **am** (attack multiplier), **dm** (defense multiplier), **pm** (precision mutliplier) will be computed. Current logic is:
  * **am** = 1 x (rightweapon ? 1.1 : 1) x (leftweapon ? 1.1 : 1)
  * **dm** = 1 x (armor ? 1.1 : 1) x (helmet ? 1.1 : 1)
  * **pm** = 1 if Shark has glasses else 0
  * This 2 multipliers are created at the initiation of each Shark and will remain constant during the battle: *SharkPunk.py*
* A random draw will decide which Shark starts attacking first

A turn works as follow:
* the attacking shark will get an attack power (**ap**) randomly computed:
  * **ap** = random(0.7, 1)
* the defending shark will get a defense power (**df**) randomly computed:
  * **dp** = random(0, 0.3)
* There is a precision factor based on the precision mutliplier:  
  * **pa** = 1 if random.random() <= (0.92 if pm == 1 else 0.90) else 0
* Damage taken by the defensive shark will be:
  * **damage**= round((ap - dp) x 15) x am / dp
  * the factor 15 has been chosen such as 10 turns in average are needed to have a winner with 100HP

**All this logic is very simple and lots of tests with different scenarios (shark attributes) would be needed to ensure the good balance of the game**


## Tests:
Here are the results of some tests games made on 1000 random battles (all these results are directly returned by the *tests.py* file:

1. Battle between Shark with no attributes: sharks #0 vs #97 as example
<img width="302" alt="Screen Shot 2021-12-12 at 3 25 46 PM" src="https://user-images.githubusercontent.com/32247660/145728367-118b86a2-6724-460c-99d3-27cdc93cfc33.png">

2. Battle between Shark1: weaponright and Shark2: no attributes
<img width="309" alt="Screen Shot 2021-12-12 at 5 10 55 PM" src="https://user-images.githubusercontent.com/32247660/145731551-f0187fbe-cec7-490a-a523-08fdb71018d8.png">

3. Battle between Shark1: weaponright and Shark2: armor
<img width="314" alt="Screen Shot 2021-12-12 at 4 55 50 PM" src="https://user-images.githubusercontent.com/32247660/145731119-3aa7e9f5-16f2-4750-8cf3-b1fc611f9e1a.png">


## Ideas:
* Implement **XP** and **Levels**:
  * The winner of each battle woul be rewarded with a specilic number of XP based on the difference of levels and attributes with the opponents. When a specific number of XP is reached the level increases by 1. Increased level would improve the defense and attack multipliers
  * Make sure game is still balance --> Restriction in battle between Sharks of different levels?
  * To avoid **farming** the number of games played in 24 hours would be capped

* Implement special attacks based on the other coins of the ecosystem in your wallet:
  * if you own $LevX token, our dictator can fight on your side, **am** increased for the x next turns
  * if you own $Maid, $Master or Maid NFT, you can call your maid, disturbing your opponent: **pm** high probability to be 0 for the x next turns
  * if you own $Sushi, $Xsushi, you can feed your opponent with 🍣, **am** and **dm** of your opponent decreased 
  * if you own $Sushib, $Xsushib, you are surrounded by $love, **dm** increased


## Questions:
* How to get the attributes of the SharkPunks?
  * Attributes do not seem to be stored on-chain. 
  * Only 366 SharkPunks --> Still possible to store the attributes manually in a file or DB
  * How to change that for the new mints?

* What would be on-chain and off-chain?
  * Level and XP seems to be the 2 only attributes on-chain
  * Games could be done off-chain, XP could be saved in a file or DB and when new level reached the owner of the Shark can decide to save the new level on-chain

* UI/language used? 



