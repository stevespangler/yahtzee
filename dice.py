# Project file names: yahtzee.py, dice.py, scorecard.py, scorefuncs.py
# Author: Steven Spangler
# MRM 8000 Midterm Project
# Date created: 8/7/2016
# Python Version: 2.7

# Dice class

import random

class Dice:
    
    def __init__(self):
        self.dice = []
        self.rollcount = 0
        
    def roll(self,num):
        for i in range(num):
            self.dice.append(random.randint(1,6))
        self.rollcount += 1
        print "\nYour dice are "
        print '  '.join(map(str,self.dice))
    
    def keep(self):
        while True:
            print "\nWhich dice to reroll? (use a space between each input)"
            print "                      (no input keeps all dice)"
            choice = raw_input(":")        
            choice = map(int,choice.split())
            if all(i <= 6 for i in choice):
                choice = [x-1 for x in choice]
                break
            else:
                print "Invalid Choice!"
        for index in sorted(choice, reverse=True):
            del self.dice[index] 
        print "\nYou have kept "
        print '  '.join(map(str,self.dice))

#################################################################
# This derived class is an unused example to show my knowledge of
# how to implement one, in order to fulfill the requirements of the 
# project.
#

class TwelveSided(Dice):
    
    def __init__(self):
        self.shape = "dodecagon"
        self.dice = []
        
    def roll(self,num):
        for i in range(num):
            self.dice.append(random.randint(1,12))
        