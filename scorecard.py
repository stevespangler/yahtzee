# Project file names: yahtzee.py, dice.py, scorecard.py, scorefuncs.py
# Author: Steven Spangler
# MRM 8000 Midterm Project
# Date created: 8/7/2016
# Python Version: 2.7

# Scorecard class

from prettytable import PrettyTable
import scorefuncs as s

class Scorecard:

    def __init__(self,name):
        self.playername = name
        self.ones = "--"
        self.twos = "--"
        self.threes = "--"
        self.fours = "--"
        self.fives = "--"
        self.sixes = "--"
        self.upperbonus = "--"
        self.kind3 = "--"
        self.kind4 = "--"
        self.FH = "--"
        self.SmStr = "--"
        self.LgStr = "--"
        self.Ytz = "--"
        self.chance = "--"
        self.YtzBon = "--"

    def printcard(self):
        print "\n********** %s's Scorecard **********" % self.playername
        score = PrettyTable()
        score.add_column("UPPER SECTION",["Ones","Twos","Threes","Fours","Fives",
                        "Sixes"," ","Upper Bonus"])
        score.add_column("score", [self.ones,self.twos,self.threes,self.fours,
                                   self.fives,self.sixes,"--",self.upperbonus])
        score.add_column("LOWER SECTION", ["Three of a Kind","Four of a Kind","Full House",
            "Small Straight","Large Straight","Yahtzee","Chance","Yahtzee Bonus"])
        score.add_column("score", [self.kind3,self.kind4,self.FH,self.SmStr,
                                   self.LgStr,self.Ytz,self.chance,self.YtzBon])
        print (score)
    
    def total(self):
        if self.ones + self.twos + self.threes + self.fours + self.fives + self.sixes >= 63:
            self.upperbonus = 35
        else:
            self.upperbonus = 0
        if self.YtzBon == "--":
            self.YtzBon = 0
        upscore = self.ones+self.twos+self.threes+self.fours+self.fives\
                    +self.sixes+self.upperbonus
        lowscore = self.kind3+self.kind4+self.FH+self.SmStr+self.LgStr\
                    +self.Ytz+self.chance+self.YtzBon
        totscore = upscore + lowscore
        self.printcard()
        print "Upper section total = %d" % upscore
        print "Lower section total = %d" % lowscore
        print "\n%s, your total score is %d" % (self.playername,totscore)
        return totscore

    def joker(self,dice):
        a = list(set(dice))
        if a == [1] and self.ones == "--":
            self.ones = 5
        elif a == [2] and self.twos == "--":
            self.twos = 10
        elif a == [3] and self.threes == "--":
            self.threes = 15
        elif a == [4] and self.fours == "--":
            self.fours = 20
        elif a == [5] and self.fives == "--":
            self.fives = 25
        elif a == [6] and self.sixes == "--":
            self.sixes = 30
        else:
            if self.kind3 != "--" and self.kind4 != "--" and self.FH != "--" \
                    and self.SmStr != "--" and self.LgStr != "--" and self.chance != "--":
                while True:
                    choose = raw_input("Enter the number of the upper section category to zero")
                    if choose == 1 and self.ones == "--":
                        self.ones = 0 
                        break
                    elif choose == 2 and self.twos == "--":
                        self.twos = 0
                        break
                    elif choose == 3 and self.threes == "--":
                        self.threes = 0
                        break
                    elif choose == 4 and self.fours == "--":
                        self.fours = 0
                        break
                    elif choose == 5 and self.fives == "--":
                        self.fives = 0
                        break
                    elif choose == 6 and self.sixes == "--":
                        self.sixes = 0
                        break
                    else:
                        print "Invalid choice! Either improper input or category already filled."
            else:
                while True:
                    choose = raw_input("Enter a lower section category to complete!").lower()
                    if choose == "three of a kind" and self.kind3 == "--":
                        self.kind3 = sum(dice)
                        break
                    elif choose == "four of a kind" and self.kind4 == "--":
                        self.kind4 = sum(dice)
                        break
                    elif choose == "full house" and self.FH == "--":
                        self.FH = 25
                        break
                    elif choose == "small straight" and self.SmStr == "--":
                        self.SmStr = 30
                        break
                    elif choose == "large straight" and self.LgStr == "--":
                        self.LgStr = 40
                        break
                    elif choose == "chance" and self.chance == "--":
                        self.chance = sum(dice)
                        break
                    else:
                        print "Invalid choice! Either improper input or category already filled."                               
            
    def addturn(self,dice):
        self.printcard()
        while True:
            cat = raw_input("Which category would you like to score for this turn? ").lower()
            if cat == "ones" and self.ones == "--":
                self.ones = s.upper(dice,1)
                break
            elif cat == "twos" and self.twos == "--":
                self.twos = s.upper(dice,2)
                break
            elif cat == "threes" and self.threes == "--":
                self.threes = s.upper(dice,3)
                break
            elif cat == "fours" and self.fours == "--":
                self.fours = s.upper(dice,4)
                break
            elif cat == "fives" and self.fives == "--":
                self.fives = s.upper(dice,5)
                break
            elif cat == "sixes" and self.sixes == "--":
                self.sixes = s.upper(dice,6)
                break
            elif cat == "three of a kind" and self.kind3 == "--":
                self.kind3 = s.kind3(dice)
                break
            elif cat == "four of a kind" and self.kind4 == "--":
                self.kind4 = s.kind4(dice)
                break
            elif cat == "full house" and self.FH == "--":
                self.FH = s.FH(dice)
                break
            elif cat == "small straight" and self.SmStr == "--":
                self.SmStr = s.SmStr(dice)
                break
            elif cat == "large straight" and self.LgStr == "--":
                self.LgStr = s.LgStr(dice)
                break
            elif cat == "yahtzee":
                if self.Ytz == "--":
                    self.Ytz = s.Ytz(dice)
                elif self.Ytz == 0:
                    self.joker(dice)
                elif self.Ytz == 50:
                    if s.Ytz(dice) == 50:
                        if self.YtzBon == "--":
                            self.YtzBon = 100
                        elif self.YtzBon%100 == 0:
                            self.YtzBon += 100 
                        self.joker(dice)
                break
            elif cat == "chance" and self.chance == "--":
                self.chance = s.Chance(dice)
                break
            else:
                print "Invalid choice! Please type category exactly as it appears on scorecard."
        self.printcard()