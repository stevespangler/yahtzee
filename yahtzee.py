#!/usr/bin/env python
# Project file names: yahtzee.py, dice.py, scorecard.py, scorefuncs.py
# Author: Steven Spangler
# MRM 8000 Midterm Project
# Date created: 8/7/2016
# Python Version: 2.7

import dice
import scorecard

print "\nLet's play Yahtzee!"
gamedice = dice.Dice()

playercount = int(raw_input("1 or 2 players? "))
if playercount == 2:
    player1 = scorecard.Scorecard(raw_input("What is Player 1's name? "))
    player2 = scorecard.Scorecard(raw_input("What is Player 2's name? "))
   
    for x in range(13):
        player1.printcard()
        print "\n%s, it's your turn." % player1.playername
        while gamedice.rollcount < 3:
            raw_input("Press Enter to roll ...... ")
            gamedice.roll(5-len(gamedice.dice))
            if gamedice.rollcount < 3:
                gamedice.keep()
        gamedice.rollcount = 0
        player1.addturn(gamedice.dice)    
        gamedice.dice = []
        
        player2.printcard()
        print "\n%s, it's your turn." % player2.playername
        while gamedice.rollcount < 3:
            raw_input("Press Enter to roll ...... ")
            gamedice.roll(5-len(gamedice.dice))
            if gamedice.rollcount < 3:
                gamedice.keep()
        gamedice.rollcount = 0
        player2.addturn(gamedice.dice)    
        gamedice.dice = []
    player1.total()
    player2.total()

elif playercount == 1:
    player1 = scorecard.Scorecard(raw_input("What is Player 1's name? "))
#    player1.playername = raw_input("What is your name? ")
    
    player1.printcard()
    for x in range(13):
        while gamedice.rollcount < 3:
            raw_input("Press Enter to roll ...... ")
            gamedice.roll(5-len(gamedice.dice))
            if gamedice.rollcount < 3:
                gamedice.keep()
        gamedice.rollcount = 0
        player1.addturn(gamedice.dice)    
        gamedice.dice = []
    player1.total()