#!/bin/sh

import tabulate
import numpy as np

#this is just to transform None into empty spaces.
def getStringValue(value):
	if value is None:
		return	 " "
	else:
		return str(value)

class TerminalInterface():

	def __init__(self):
		pass

	#Given a board, make a graphical representation of it.
	def printBoard(self, board):

		#we print a 2D "table"
		table = []

		#first transform 1-D list into a 2-d list
		for i in range(len(board)):
			stringValue = getStringValue(board[i])
			table.append(stringValue)

		#Tabulate requires 2-d tables, lets resize
		table =  np.resize(board,(3,3))
		print "\n"
		print tabulate.tabulate(table, tablefmt="grid")

	def sendWelcomeScreen(self):
		print "Welcome to Tic-Tac-Toe!\n"

	#asks the player if they want to go first.
	def askForPlayerSymbol(self):
		playerFirst = ""
		print("---X goes first---")
		while playerFirst.upper() not in ["Y","N"]:
			playerFirst = raw_input("Do you want to go first? (y or n)")

		if playerFirst.upper() == "Y":
			return "X"
		else:
			return "O"

	#gets the players move. Note that only the game engine knows if its valid or not.
	#so we make no additional checks, other than number check
	def getPlayersMove(self):

		waitingInput = True
		while waitingInput:
			chosenMove = raw_input("Choose your move (1-9): ")
			if chosenMove is None or not str.isdigit(chosenMove):
				print "please enter a number"
			else:
				waitingInput = False

		return int(chosenMove)

	def sendCongrats(self):
		print "\nYOU WIN! CONGRATULATIONS!\n"
		print "Thanks for playing!\n\n"

	def sendSorry(self):
		print "\nYou lose. Better luck next time.\n"
		print "Thanks for playing!\n\n"

	def sendDrawMessage(self):
		print "\nIt's a draw!.\n"
		print "Thanks for playing!\n\n"


	#passing of general messages to the player
	def printMessage(self, msg):
		print msg





