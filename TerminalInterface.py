#!/bin/sh

import tabulate
import numpy as np

#this is just to transform None into empty spaces.
def get_string_value(value):
    if value is None:
        return   " "
    else:
        return str(value)

class TerminalInterface():

    def __init__(self):
        pass

    #Given a board, make a graphical representation of it.
    def print_board(self, board):

        #we print a 2D "table"
        table = []

        #first transform 1-D list into a 2-d list
        for i in range(len(board)):
            string_value = get_string_value(board[i])
            table.append(string_value)

        #Tabulate requires 2-d tables, lets resize
        table = np.resize(board, (3, 3))
        print "\n"
        print tabulate.tabulate(table, tablefmt="grid")

    def send_welcome_screen(self):
        print "Welcome to Tic-Tac-Toe!\n"

    #asks the player if they want to go first.
    def ask_for_player_symbol(self):
        player_first = ""
        print "---X goes first---"
        while player_first.upper() not in ["Y", "N"]:
            player_first = raw_input("Do you want to go first? (y or n)")

        if player_first.upper() == "Y":
            return "X"
        else:
            return "O"

    #  gets the players move. Note that only the game engine
    #    knows if its valid or not.
    #  So we make no additional checks, other than number check
    def get_players_move(self):
        waiting_input = True
        while waiting_input:
            chosen_move = raw_input("Choose your move (1-9): ")
            if chosen_move is None or not str.isdigit(chosen_move):
                print "please enter a number"
            else:
                waiting_input = False

        return int(chosen_move)

    def send_congrats(self):
        print "\nYOU WIN! CONGRATULATIONS!\n"
        print "Thanks for playing!\n\n"

    def send_sorry(self):
        print "\nYou lose. Better luck next time.\n"
        print "Thanks for playing!\n\n"

    def send_draw_message(self):
        print "\nIt's a draw!.\n"
        print "Thanks for playing!\n\n"


    #passing of general messages to the player
    def print_message(self, msg):
        print msg





