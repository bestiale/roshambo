#!/usr/bin/python
# encoding: utf-8

import sys
from random import randint
from time import sleep

class Game(object):
    user_pt = 0
    cpu_pt = 0
    schere = 1
    stein = 2
    papier = 3

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

    def check(self, user, cpu):
        
        if user == cpu:
            return 0
            
        elif user == self.schere and cpu == self.papier:
            return 1
            
        elif user == self.papier and cpu == self.stein:
            return 1
            
        elif user == self.stein and cpu == self.schere:
            return 1
            
        else:
            return 2
            
    def print_hand(self, user, cpu, point):

        if user == 1:
            print "\nYour hand is: Schere"
        elif user == 2:
            print "\nYour hand is: Stein"
        else:
            print "\nYour hand is: Papier"
            
        if cpu == 1:
            print "The CPU has: Schere\n"
        elif cpu == 2:
            print "The CPU has: Stein\n"
        elif cpu == 3:
            print "The CPU has: Papier\n"
        else:
            pass

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
            return 0
            
        elif user == self.schere and cpu == self.papier:
            print "You received the point\n"
            sleep(3)
            return 1
            
        elif user == self.papier and cpu == self.stein:
            print "You received the point\n"
            sleep(3)
            return 1
            
        elif user == self.stein and cpu == self.schere:
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