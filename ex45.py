#!/usr/bin/python
# encoding: utf-8

import sys
from random import randint
from time import sleep

class Roshambo(object):

    SCHERE = 1
    STEIN = 2
    PAPIER = 3

    def __init__(self):
        self.player1_points = 0
        self.player2_points = 0
        self.name = ""
        self.name_cpu = ""
               
    def intro(self):
        
        name = raw_input("Please enter your name: > ")
        print "\n************************"
        print "Hello %s :) " % name
        print "************************\n"
        sleep(1)
        return name
        
    def cpu_hand(self):

        return randint(1, 3)

    def check_hand(self, player1_hand, player2_hand):
        
        if player1_hand == player2_hand:
            return 0
        elif player1_hand == Roshambo.SCHERE and player2_hand == Roshambo.PAPIER:
            return 1 
        elif player1_hand == Roshambo.PAPIER and player2_hand == Roshambo.STEIN:
            return 1
        elif player1_hand == Roshambo.STEIN and player2_hand == Roshambo.SCHERE:
            return 1
        else:
            return 2
  
    def print_hand(self, user_name, name_cpu, user_hand, cpu_hand):

        if user_hand == 1:
            print "\n%s's hand is: Schere" % user_name
        elif user_hand == 2:
            print "\n%s's hand is: Stein" % user_name
        else:
            print "\n%s's hand is: Papier" % user_name
            
        if cpu_hand == 1:
            print "The %s has: Schere\n" % name_cpu
        elif cpu_hand == 2:
            print "The %s has: Stein\n" % name_cpu
        elif cpu_hand == 3:
            print "The %s has: Papier\n" % name_cpu

    def point_handler(self, point):

        if point == 1:
            self.player1_points += 1
        elif point == 2:
            self.player2_points += 1

    def print_point(self, name, name_cpu, player1_hand, player2_hand):

        if player1_hand == player2_hand:
            print "Nobody receives the point\n"  
        elif player1_hand == Roshambo.SCHERE and player2_hand == Roshambo.PAPIER:
            print "%s received the point\n" % name   
        elif player1_hand == Roshambo.PAPIER and player2_hand == Roshambo.STEIN:
            print "%s received the point\n" % name   
        elif player1_hand == Roshambo.STEIN and player2_hand == Roshambo.SCHERE:
            print "%s received the point\n" % name
        else:
            print "The %s receives a point\n" % name_cpu

    def print_result(self, name, name_cpu):
        print "\n_____________________________"
        print "\nResult: %s %d %s %d\n" % (name, self.player1_points, name_cpu, self.player2_points)
        if self.player1_points > self.player2_points:
            print "You won - Good work :)"
        elif self.player1_points < self.player2_points:
            print "You lost! I'm sorry"
        else:
            print "Nobody has won! Try again!"
        print "\nBye %s\n" % name

            
class ConsoleGame(object):

    def __init__(self):
        self.game = Roshambo()
        self.name = ""
        self.name_cpu = "CPU"

    def play(self):

        self.name = self.game.intro()

        try:
            while True: 
                    player1_hand = self.user_hand()
                    player2_hand = self.game.cpu_hand()
                    point = self.game.check_hand(player1_hand, player2_hand)
                    self.game.print_hand(self.name, self.name_cpu, player1_hand, player2_hand)
                    self.game.point_handler(point)
                    self.game.print_point(self.name, self.name_cpu, player1_hand, player2_hand)
                    sleep(3)
        except (EOFError, KeyboardInterrupt):
            self.game.print_result(self.name)

    def user_hand(self):

        user_hand = 0
        
        print "Please choose your hand:\n"
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

class CpuGame(object):

    def __init__(self):
        self.game = Roshambo()
        self.name = "First CPU"
        self.name_cpu = "Second CPU"

    def play(self):
        print "\n\n***************************"
        print "Welcome to CPU vs CPU Mode"
        print "***************************\n"
        try:
            while True: 
                    cpu_hand = self.game.cpu_hand()
                    cpu2_hand = self.game.cpu_hand()
                    point = self.game.check_hand(cpu_hand, cpu2_hand)
                    self.game.print_hand(self.name, self.name_cpu, cpu_hand, cpu2_hand)
                    self.game.point_handler(point)
                    self.game.print_point(self.name, self.name_cpu, cpu_hand, cpu2_hand)
                    sleep(3)
        except (EOFError, KeyboardInterrupt):
            self.game.print_result(self.name, self.name_cpu)

a_game = CpuGame()
a_game.play()