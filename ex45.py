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
        self.name = ""
        roundcount = 0

    def play(self):

        self.intro()
        whoplay = self.who_play()
        playmode = self.playmode()

        try:
            if whoplay == 1 and playmode == 2:
                while True: 
                    user_hand = self.user_hand()
                    cpu_hand = self.cpu_hand()
                    point = self.check(user_hand, cpu_hand)
                    self.print_hand(user_hand, cpu_hand)
                    self.point_handler(point)
                    self.print_point(user_hand, cpu_hand)
                    sleep(3)
            elif whoplay == 1 and playmode == 1:
                self.read_highscore()
            else:
                self.name = self.name + "_CPU"
                while True:
                    first_cpu_hand = self.cpu_hand()
                    second_cpu_hand = self.cpu_hand()
                    point = self.check(first_cpu_hand, second_cpu_hand)
                    self.print_hand(first_cpu_hand, second_cpu_hand)
                    self.point_handler(point)
                    self.print_point(first_cpu_hand, second_cpu_hand)
                    sleep(3)
        except (EOFError, KeyboardInterrupt):
            self.finish()
        
            
    def intro(self):
        
        self.name = raw_input("Please enter your name: > ")
        print "\n************************"
        print "Hello %s :) " % self.name
        print "************************\n"
        sleep(1)

    def who_play(self):

        print "You want let play the CPU instead of you?\n"
        print "1. I want to play self"
        print "2. I want to let play the CPU"

        valid_input = False
        while not valid_input:
            try:
                player = int(raw_input("> "))
                if player not in range(1, 3):
                    print "Thats not a valid option, please try again"
                else:
                    valid_input = True    
            except ValueError:
                print "Thats not a number, please try again"

        return player

    def playmode(self):
        print "You want to try to set a new Highscore?"
        print "You will have only 10 rounds to try it"
        print "1. Yes i want set a new Highscore"
        print "2. No. I just want to play for fun"

        valid_input = False
        while not valid_input:
            try:
                playmode = int(raw_input("> "))
                if playmode not in range(1, 3):
                    print "Thats not a valid option, please try again"
                else:
                    valid_input = True    
            except ValueError:
                print "Thats not a number, please try again"

        return playmode

        
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
            try:
                user_hand = int(raw_input("> "))
                if user_hand not in range(1, 4):
                    print "Thats not a valid option, please try again"
                else:
                    valid_input = True    
            except ValueError:
                print "Thats not a number, please try again"
            
        return user_hand

    def read_highscore(self):
        filename = "highscore.txt"
        highscore_file = open(filename, "r")
        print highscore_file.read()

    def write_highscore(self):
        filename = "highscore.txt"
        highscore_file = open(filename, "w")
        highscore_file.write(self.name":" self.user_points)
        print "Highscore saved"
        
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
            
a_game = Game()
a_game.play()