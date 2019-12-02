# IMPORTANT NOTE: To test, you must run the command "pytest test.py -s"
# The "-s" is required due to the nature of the functions requiring user input in the middle of their use

import pytest

import main.py as m


def test_case1():
    global p1
    p1.gold = 99
    m.shop()
    assert(p1.gold == 99)
    # Not enough gold to buy item


def test_case2():
    global p1
    p1.gold = 1000
    m.shop()
    assert(p1.gold < 1000)
    # Enough gold to buy item


def test_case3():
    global p1
    p1.level = 1
    m.levelUp()
    assert(p1.level == 2)
    # A level up increases player level by 1


def test_case4():
    global p1
    p1.currhp = 1
    m.rest()
    assert(p1.currhp == p1.maxhp)
    # Resting to restore health sets current hp equal to max hp


def test_case5():
    global p1
    p1.attack = 3
    m.rest()
    assert(p1.attack == 5)
    # Resting to sharpen blade increases player attack by 2
