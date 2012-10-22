#!/usr/bin/python
# encoding: utf-8

import sys
from random import randint
from time import sleep

class Game(object):

    def play(self):
        user_pt = 0
        cpu_pt = 0
        name = self.intro()

        try:
            while True: 
                user_hand = self.next_round()
                print "User has %s at the moment" % user_hand
                point = self.check(user_hand)
                if point == 1:
                    user_pt += 1
                elif point == 2:
                    cpu_pt += 1
                else:
                    pass
                
        except (EOFError, KeyboardInterrupt):
            self.finish(name, cpu_pt, user_pt)
            
    def intro(self):
        name = raw_input("Please enter your name: > ")
        print "\n************************"
        print "Hello %s :) " % name
        print "************************\n"
        sleep(1)
        return name
        
        
    def check(self, user):
        cpu_hand = randint(1, 3)
        schere = 1
        stein = 2
        papier = 3
        
        if user == 1:
            print "\nYour hand is: Schere"
        elif user == 2:
            print "\nYour hand is: Stein"
        else:
            print "\nYour hand is: Papier"
            
        if cpu_hand == 1:
            print "The CPU has: Schere\n"
        elif cpu_hand == 2:
            print "The CPU has: Stein\n"
        elif cpu_hand == 3:
            print "The CPU has: Papier\n"
        else:
            pass
        
        if user == cpu_hand:
            print "Nobody receives the point\n"
            sleep(3)
            return 0
            
        elif user == schere and cpu_hand == papier:
            print "You received the point\n"
            sleep(3)
            return 1
            
        elif user == papier and cpu_hand == stein:
            print "You received the point\n"
            sleep(3)
            return 1
            
        elif user == stein and cpu_hand == schere:
            print "You received the point\n"
            sleep(3)
            return 1
            
        else:
            print "The CPU receives a point\n"
            sleep(3)
            return 2
            
            
    def next_round(self):
        user_hand = 0
        
        print "Please choose your hand: \n"
        print "1. Schere \n"
        print "2. Stein \n"
        print "3. Papier \n"
        print "(To quit press CTRL-D)"
        try:
            user_hand = int(raw_input("> "))
            if user_hand not in range(1,4):
                print "This number is not valid, please try again"
                return self.next_round()
        except ValueError:
            print "This is not a number, please try again"
            return self.next_round()
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
