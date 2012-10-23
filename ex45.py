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
        self.user_pt = 0
        self.cpu_pt = 0

    def play(self):

        name = self.intro()

        try:
            while True: 
                user_hand = self.next_round()
                cpu_hand = self.cpu_hand()
                point = self.check(user_hand, cpu_hand)
                self.print_hand(user_hand, cpu_hand, point)
                self.points(user_hand, cpu_hand, point)
        except (EOFError, KeyboardInterrupt):
            self.finish(name, self.cpu_pt, self.user_pt)
        
            
    def intro(self):
        
        name = raw_input("Please enter your name: > ")
        print "\n************************"
        print "Hello %s :) " % name
        print "************************\n"
        sleep(1)
        return name
        
    def cpu_hand(self):

        cpu = randint(1, 3)
        return cpu

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


    def points(self, user, cpu, point):

        if point == 1:
            self.user_pt += 1
        elif point == 2:
            self.cpu_pt += 1
        else:
            pass

        if user == cpu:
            print "Nobody receives the point\n"
            sleep(3)
            
        elif user == self.schere and cpu == self.papier:
            print "You received the point\n"
            sleep(3)
            
        elif user == self.papier and cpu == self.stein:
            print "You received the point\n"
            sleep(3)
            
        elif user == self.stein and cpu == self.schere:
            print "You received the point\n"
            sleep(3)
            
        else:
            print "The CPU receives a point\n"
            sleep(3)

           
    def next_round(self):

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
        
    def finish(self, name, cpu_pt, user_pt):
        print "\n_____________________________"
        print "\nResult: %s %d CPU %d\n" % (name, user_pt, cpu_pt)
        if user_pt > cpu_pt:
            print "You won - Good work :)"
        elif user_pt < cpu_pt:
            print "You lost! I'm sorry"
        else:
            print "Nobody has won! Try again!"
        print "\nBye %s\n" % name
            
a_game = Game()
a_game.play()