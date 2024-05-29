import pytest

from functionality_rpg import player_first
from functionality_rpg import Warrior, Wizzard, Enemy

def test_player_first_attack_warrior():
    test_p = Warrior()
    test_e = Enemy()
    assert player_first("a", test_p, test_e) == "You did 20 damage"

def test_player_first_recoil_warrior():
    test_p = Warrior()
    test_e = Enemy()
    test_e.defense = 100
    assert player_first("a", test_p, test_e) == "You took 50 damage"


def test_player_first_attack_wizard():
    test_p = Wizzard()
    test_p.attack = 50
    test_e = Enemy()
    assert player_first("a", test_p, test_e) == "You did 20 damage"

def test_player_first_recoil_wizzard():
    test_p = Wizzard()
    test_e = Enemy()
    test_e.defense = 100
    assert player_first("a", test_p, test_e) == "You took 70 damage"



#Write test for class skills
...