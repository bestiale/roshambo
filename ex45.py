#!/usr/bin/python
# encoding: utf-8

import sys
from random import randint
from time import sleep

class Game(object):

    schere = 1
    stein = 2
    papier = 3

    def __init__(self):
        self.user_points = 0
        self.cpu_points = 0

    def play(self):

        name = self.intro()

        try:
            while True: 
                user_hand = self.user_hand()
                cpu_hand = self.cpu_hand()
                point = self.check(user_hand, cpu_hand)
                self.print_hand(user_hand, cpu_hand, point)
                self.point_handler(point)
                self.print_point(user_hand, cpu_hand)
                sleep(3)
        except (EOFError, KeyboardInterrupt):
            self.finish(name, self.cpu_points, self.user_points)
        
            
    def intro(self):
        
        name = raw_input("Please enter your name: > ")
        print "\n************************"
        print "Hello %s :) " % name
        print "************************\n"
        sleep(1)
        return name
        
    def cpu_hand(self):

        return randint(1, 3)

    def check(self, user_hand, cpu_hand):
        
        if user_hand == cpu_hand:
            return 0
            
        elif user_hand == Game.schere and cpu_hand == Game.papier:
            return 1
            
        elif user_hand == Game.papier and cpu_hand == Game.stein:
            return 1
            
        elif user_hand == Game.stein and cpu_hand == Game.schere:
            return 1
            
        else:
            return 2
            
    def print_hand(self, user_hand, cpu_hand, point):

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
            
        elif user_hand == Game.schere and cpu_hand == Game.papier:
            print "You received the point\n"
            
        elif user_hand == Game.papier and cpu_hand == Game.stein:
            print "You received the point\n"
            
        elif user_hand == Game.stein and cpu_hand == Game.schere:
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
            user_hand = int(raw_input("> "))
            if user_hand not in range(1, 4):
                print("Thats not a valid option, please try again")
            else:
                valid_input = True 
            
        return user_hand
        
    def finish(self, name, cpu_points, user_points):
        print "\n_____________________________"
        print "\nResult: %s %d CPU %d\n" % (name, user_points, cpu_points)
        if user_points > cpu_points:
            print "You won - Good work :)"
        elif user_points < cpu_points:
            print "You lost! I'm sorry"
        else:
            print "Nobody has won! Try again!"
        print "\nBye %s\n" % name
            
a_game = Game()
a_game.play()