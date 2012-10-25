#!/usr/bin/python
# encoding: utf-8

import sys
from random import randint
from time import sleep

class Roshambo(object):

    schere = 1
    stein = 2
    papier = 3

    def __init__(self):
        self.user_points = 0
        self.cpu_points = 0
        self.name = ""

    def play(self):

        self.intro()

        try:
            while True: 
                    user_hand = self.user_hand()
                    cpu_hand = self.cpu_hand()
                    point = self.check_hand(user_hand, cpu_hand)
                    self.print_hand(user_hand, cpu_hand)
                    self.point_handler(point)
                    self.print_point(user_hand, cpu_hand)
                    sleep(3)
        except (EOFError, KeyboardInterrupt):
            self.finish()
               
    def intro(self):
        
        self.name = raw_input("Please enter your name: > ")
        print "\n************************"
        print "Hello %s :) " % self.name
        print "************************\n"
        sleep(1)
        
    def cpu_hand(self):

        return randint(1, 3)

    def check_hand(self, user_hand, cpu_hand):
        
        if user_hand == cpu_hand:
            return 0
        elif user_hand == Roshambo.schere and cpu_hand == Roshambo.papier:
            return 1 
        elif user_hand == Roshambo.papier and cpu_hand == Roshambo.stein:
            return 1
        elif user_hand == Roshambo.stein and cpu_hand == Roshambo.schere:
            return 1
        else:
            return 2

            
    def print_hand(self, user_hand, cpu_hand):

        if user_hand == 1:
            print "\nYour hand is: Schere"
        elif user_hand == 2:
            print "\nYour hand is: Stein"
        else:
            print "\nYour hand is: Papier"
            
        if cpu_hand == 1:
            print "The CPU has: Schere\n"
        elif cpu_hand == 2:
            print "The CPU has: Stein\n"
        elif cpu_hand == 3:
            print "The CPU has: Papier\n"

    def point_handler(self, point):

        if point == 1:
            self.user_points += 1
        elif point == 2:
            self.cpu_points += 1

    def print_point(self, user_hand, cpu_hand):

        if user_hand == cpu_hand:
            print "Nobody receives the point\n"  
        elif user_hand == Roshambo.schere and cpu_hand == Roshambo.papier:
            print "You received the point\n"    
        elif user_hand == Roshambo.papier and cpu_hand == Roshambo.stein:
            print "You received the point\n"    
        elif user_hand == Roshambo.stein and cpu_hand == Roshambo.schere:
            print "You received the point\n"    
        else:
            print "The CPU receives a point\n"
  
    def user_hand(self):

        user_hand = 0
        
        print "Please choose your hand: \n"
        print "1. Schere \n"
        print "2. Stein \n"
        print "3. Papier \n"
        print "(To quit press CTRL-D)"

        valid_input = False
        while not valid_input:
            try:
                user_hand = int(raw_input("> "))
                if user_hand not in range(1, 4):
                    print "Thats not a valid option, please try again"
                else:
                    valid_input = True    
            except ValueError:
                print "Thats not a number, please try again"
            
        return user_hand
        
    def finish(self):
        print "\n_____________________________"
        print "\nResult: %s %d CPU %d\n" % (self.name, self.user_points, self.cpu_points)
        if self.user_points > self.cpu_points:
            print "You won - Good work :)"
        elif self.user_points < self.cpu_points:
            print "You lost! I'm sorry"
        else:
            print "Nobody has won! Try again!"
        print "\nBye %s\n" % self.name

            
class ConsoleGame(Roshambo):

    def __init__(self):
        self.name = ""
        self.user_points = 0
        self.cpu_points = 0

class CpuGame(Roshambo):

    def __init__(self):
        self.name = "CPU"
        self.user_points = 0
        self.cpu_points = 0

    def play(self):
        try:
            while True: 
                    cpu_hand = Roshambo.cpu_hand(self)
                    cpu2_hand = Roshambo.cpu_hand(self)
                    point = Roshambo.check_hand(self, cpu_hand, cpu2_hand)
                    Roshambo.print_hand(self, cpu_hand, cpu2_hand)
                    Roshambo.point_handler(self, point)
                    Roshambo.print_point(self, cpu_hand, cpu2_hand)
                    sleep(3)
        except (EOFError, KeyboardInterrupt):
            self.finish()



a_game = CpuGame()
a_game.play()