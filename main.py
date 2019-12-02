import random as r

# Global variables declared below
currentFloor = 0
p1 = "Player"
e1 = "Enemy"
i1 = "Item"
# Global variables declared above


class Player:
    def __init__(self, name, maxhp, currhp, weapon, armor, attack, defense, gold, exp, level):
        self.name = name
        self.maxhp = maxhp
        self.currhp = currhp
        self.weapon = weapon
        self.armor = armor
        self.attack = attack
        self.defense = defense
        self.gold = gold
        self.exp = exp
        self.level = level


class Enemy:
    def __init__(self, name, maxhp, hp, attack):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.attack = attack


class Item:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


def main():
    global currentFloor
    global p1
    currentFloor = 1
    print("What is your name?")
    print('')
    try:
        i = str(input('>>> '))
    except ValueError:
        main()
    else:
        p1 = Player(i, 20, 20, 'Basic Sword', 'Basic Armor', 3, 1, 0, 0, 1)
        menu()


def menu():
    global currentFloor
    global p1
    print("Tower of Perdition")
    print("Floor " + str(currentFloor))
    print("Name: " + p1.name)
    print("Health: " + str(p1.currhp) + '/' + str(p1.maxhp) + " points")
    print("Weapon: " + p1.weapon + " (" + str(p1.attack) + " damage)")
    print("Armor: " + p1.armor + " (" + str(p1.defense) + " resistance)")
    print("Gold: " + str(p1.gold))
    print("Player Level: " + str(p1.level) + " (" + str(p1.exp) + " points)")
    print("")
    print("Type 'explore' to climb the Tower of Perdition")
    print("")
    try:
        i = str(input('>>> '))
    except ValueError:
        menu()
    else:
        i = i.lower()
        if i == 'explore':
            generateFloor()
        else:
            menu()


def floor1():
    global e1
    e1 = Enemy("?", 10, 10, 3)
    x = r.randint(0, 1)
    if x == 0:
        e1.name = "Bat"
    if x == 1:
        e1.name = "Imp"


def floor2():
    global e1
    e1 = Enemy("?", 15, 15, 3)
    x = r.randint(0, 1)
    if x == 0:
        e1.name = "Troll"
    if x == 1:
        e1.name = "Ghoul"


def floor3():
    global e1
    e1 = Enemy("?", 20, 20, 4)
    x = r.randint(0, 1)
    if x == 0:
        e1.name = "Cyclops"
    if x == 1:
        e1.name = "Banshee"


def floor4():
    x = r.randint(1, 10)
    if x < 7:
        global e1
        e1 = Enemy("Vampire", 25, 25, 4)
    elif x > 8:
        shop()
    else:
        rest()


def floor5():
    global e1
    x = r.randint(1, 100)
    if x < 41:
        e1 = Enemy("Minotaur", 30, 30, 5)
    elif x < 51:
        e1 = Enemy("The MiniBoss", 60, 60, 2)
    elif x < 76:
        shop()
    else:
        rest()


def floor6():
    global e1
    x = r.randint(1, 100)
    if x < 41:
        e1 = Enemy("Wraith", 35, 35, 5)
    elif x < 51:
        e1 = Enemy("Demon Artifact", 1, 1, 1)
    elif x < 76:
        shop()
    else:
        rest()


def floor7():
    global e1
    x = r.randint(1, 100)
    if x < 41:
        e1 = Enemy("Scarecrow", 40, 40, 5)
    elif x < 51:
        e1 = Enemy("Angel Artifact", 1, 1, 1)
    elif x < 76:
        shop()
    else:
        rest()


def floor8():
    global e1
    x = r.randint(1, 100)
    if x < 41:
        e1 = Enemy("Skeletal Dragon", 40, 40, 6)
    elif x < 51:
        e1 = Enemy("The MiniBoss", 100, 100, 5)
    elif x < 76:
        shop()
    else:
        rest()


def floor9():
    x = r.randint(1, 2)
    if x == 1:
        shop()
    else:
        rest()


def floor10():
    global e1
    e1 = Enemy("Ghost of Perdition", 50, 50, 7)


def generateFloor():
    global currentFloor
    global e1
    if currentFloor == 1:
        floor1()
    if currentFloor == 2:
        floor2()
    if currentFloor == 3:
        floor3()
    if currentFloor == 4:
        floor4()
    if currentFloor == 5:
        floor5()
    if currentFloor == 6:
        floor6()
    if currentFloor == 7:
        floor7()
    if currentFloor == 8:
        floor8()
    if currentFloor == 9:
        floor9()
    if currentFloor == 10:
        floor10()
    preBattle()


def preBattle():
    print('')
    print("The " + e1.name + " has appeared! Type 'start' to fight")
    print("")
    try:
        i = str(input('>>> '))
    except ValueError:
        preBattle()
    else:
        i = i.lower()
        if i == 'start':
            battle()
        else:
            preBattle()


def battle():
    global p1
    global e1
    print('')
    print(p1.name + ": " + str(p1.currhp) + "/" + str(p1.maxhp))
    print(e1.name + ": " + str(e1.hp))
    print("")
    print("Type 'fight' to attack the enemy")
    print("")
    try:
        i = str(input('>>> '))
    except ValueError:
        battle()
    else:
        i = i.lower()
        if i == 'fight':
            attack()
        else:
            battle()

def attack():
    global p1
    global e1
    playerRoll = r.randint(0, 10)
    if playerRoll == 0:
        print('You swung your sword and missed!')
    elif 0 < playerRoll < 4:
        e1.hp = e1.hp - (p1.attack - 1)
        print('You dealt ' + str(p1.attack - 1) + ' damage.')
    elif 3 < playerRoll < 8:
        e1.hp = e1.hp - (p1.attack)
        print('You dealt ' + str(p1.attack) + ' damage.')
    elif 7 < playerRoll < 11:
        e1.hp = e1.hp - (p1.attack + 1)
        print('You dealt ' + str(p1.attack + 1) + ' damage.')
    if e1.hp <= 0:
        postBattle()
    enemyRoll = r.randint(0, 10)
    if enemyRoll == 0:
        print('You blocked the enemy attack!')
    elif 0 < enemyRoll < 4:
        p1.currhp = p1.currhp + p1.defense - (e1.attack - 1)
        print('The enemy dealt ' + str(e1.attack - 1 - p1.defense) + ' damage.')
    elif 3 < enemyRoll < 8:
        p1.currhp = p1.currhp + p1.defense - (e1.attack)
        print('The enemy dealt ' + str(e1.attack - p1.defense) + ' damage.')
    elif 7 < enemyRoll < 11:
        p1.currhp = p1.currhp + p1.defense - (e1.attack + 1)
        print('The enemy dealt ' + str(e1.attack + 1 - p1.defense) + ' damage.')
    if p1.currhp <= 0:
        death()
    else:
        battle()


def postBattle():
    global p1
    global e1
    global currentFloor
    print('')
    print("The enemy has been slain!")
    print("You have gained " + str(3*e1.maxhp) + " gold and " + str(20*e1.attack) + " experience points!")
    if e1.name == "Demon Artifact":
        print("The mysterious artifact has granted your weapon +3 attack!")
        p1.attack += 3
    elif e1.name == "Angel Artifact":
        print("The mysterious artifact has granted your armor +3 defense!")
        p1.defense += 3
    elif e1.name == "Ghost of Perdition":
        print("You won!!! Thanks for playing!")
        print("")
        print("Type anything to play again")
        print("")
        try:
            i = str(input('>>> '))
        except ValueError:
            main()
        else:
            i = i.lower()
            if i == 'restart':
                main()
            else:
                main()
    print("")
    print("Type anything to continue")
    print("")
    i = str(input('>>> '))
    p1.gold += 3*e1.maxhp
    p1.exp += 20*e1.attack
    currentFloor += 1
    if 100 <= p1.exp:
        levelUp()
    else:
        menu()


def death():
    print('')
    print("You have died.")
    print("")
    print("Type 'restart' to play again")
    print("")
    try:
        i = str(input('>>> '))
    except ValueError:
        death()
    else:
        i = i.lower()
        if i == 'restart':
            main()
        else:
            death()


def levelUp():
    global p1
    print('')
    print('You have leveled up!')
    print('Your max health has increased by 2 points.')
    print("")
    print("Type anything to continue")
    print("")
    i = str(input('>>> '))
    p1.maxhp += 4
    p1.exp -= 100
    p1.level += 1
    p1.currhp = p1.maxhp
    menu()


def rest():
    global p1
    global currentFloor
    print("")
    print("This floor appears to be empty. Would you like to rest for a while or sharpen your sword?")
    print("")
    print("Type 'rest' to restore your health or type 'sharpen' to increase your attack")
    print("")
    try:
        i = str(input('>>> '))
    except ValueError:
        battle()
    else:
        i = i.lower()
        if i == 'rest':
            p1.currhp = p1.maxhp
            currentFloor += 1
            print("Your health has been fully restored.")
            menu()
        elif i == 'sharpen':
            p1.attack += 2
            currentFloor += 1
            print("Your attack power has increased.")
            menu()
        else:
            rest()


def shop():
    global p1
    global i1
    global currentFloor
    itemRoll = r.randint(1,5)
    if itemRoll == 1:
        i1 = Item("Potion", 100)
    elif itemRoll == 2:
        i1 = Item("Steel Armor", 400)
    elif itemRoll == 3:
        i1 = Item("Steel Sword", 400)
    elif itemRoll == 4:
        i1 = Item("Legendary Armor", 700)
    elif itemRoll == 5:
        i1 = Item("Legendary Sword", 700)
    print("")
    print("A vendor has appeared. Would you like to buy " + i1.name + " for " + str(i1.cost) + " gold?")
    print("Type 'yes' to purchase, or type 'no' to leave.")
    print("")
    try:
        i = str(input('>>> '))
    except ValueError:
        shop()
    else:
        i = i.lower()
        if i == 'yes':
            if p1.gold < i1.cost:
                currentFloor += 1
                print("You do not have enough gold.")
                menu()
            elif itemRoll == 1:
                p1.gold -= i1.cost
                p1.currhp = p1.maxhp
                currentFloor += 1
                print("Your health has been fully restored.")
                menu()
            elif itemRoll == 2:
                p1.gold -= i1.cost
                p1.armor = i1.name
                p1.defense = 3
                currentFloor += 1
                print("Thanks for doing business!")
                menu()
            elif itemRoll == 3:
                p1.gold -= i1.cost
                p1.weapon = i1.name
                p1.attack = 5
                currentFloor += 1
                print("Thanks for doing business!")
                menu()
            elif itemRoll == 4:
                p1.gold -= i1.cost
                p1.armor = i1.name
                p1.defense = 5
                currentFloor += 1
                print("Thanks for doing business!")
                menu()
            elif itemRoll == 5:
                p1.gold -= i1.cost
                p1.weapon = i1.name
                p1.attack = 7
                currentFloor += 1
                print("Thanks for doing business!")
                menu()
        elif i == 'no':
            currentFloor += 1
            print("Maybe another time.")
            menu()
        else:
            shop()


main()
