# Project file names: yahtzee.py, dice.py, scorecard.py, scorefuncs.py
# Author: Steven Spangler
# MRM 8000 Midterm Project
# Date created: 8/7/2016
# Python Version: 2.7

# Score analysis functions

def upper(dice,cat):
    score = dice.count(cat)*cat
    return score

def kind3(dice):
    score = 0
    for item in dice:
        if dice.count(item) >= 3:
            score = sum(dice)
    return score

def kind4(dice):
    score = 0
    for item in dice:
        if dice.count(item) >= 4:
            score = sum(dice)
    return score
    
def FH(dice):
    score = 0
    freq = {x:dice.count(x) for x in dice}
    freq2 = freq.values()
    if freq2 == [2,3] or freq2 == [3,2]:
        score = 25    
    return score

def SmStr(dice):
    score = 0
    poss1,poss2,poss3 = {1,2,3,4},{2,3,4,5},{3,4,5,6}
    sortdice = set(sorted(dice))
    if poss1.issubset(sortdice):
        score = 30
    elif poss2.issubset(sortdice):
        score = 30
    elif poss3.issubset(sortdice):
        score = 30
    return score
    
def LgStr(dice):
    score = 0
    if sorted(dice) == [1,2,3,4,5] or sorted(dice) == [2,3,4,5,6]:
        score = 40
    return score
    
def Ytz(dice):
    score = 0
    if len(set(dice)) == 1:
        score = 50
    return score
    
def Chance(dice):
    score = sum(dice)
    return score