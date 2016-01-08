#!/bin/sh
import sys
import GameEngine
import TerminalInterface
import RandomStrategy

class Game():

	def __init__(self):
		self.interface = TerminalInterface.TerminalInterface()
		self.engine = GameEngine.GameEngine()
		self.strategy = RandomStrategy.RandomStrategy()
		self.newGame()

	def newGame(self):
		self.interface.sendWelcomeScreen()
		self.engine.playerSymbol = self.interface.askForPlayerSymbol()
		self.playTheGame()

	#Game's steady-state
	def playTheGame(self):
		while not self.engine.isGameOver():
			self.playersTurn()
			self.computersTurn()
		self.finishTheGame()

	def playersTurn(self):
		if self.engine.isPlayersTurn() and not self.engine.isGameOver():
			self.interface.printMessage("\n=== Player's Turn ===")

			#wait for correct input before processing
			playersMove = self.interface.getPlayersMove()
			while not self.engine.isValidMove(playersMove):
				playersMove = self.interface.getPlayersMove()

			#now that we have a valid move, we process it.
			self.engine.processMove(playersMove)
			self.printTheBoard()

	def computersTurn(self):
		if not self.engine.isPlayersTurn() and not self.engine.isGameOver():
			self.interface.printMessage("\n=== Computer's Turn ===")
			currentBoard = self.engine.board
			computersMove = self.strategy.getMove(currentBoard)
			self.engine.processMove(computersMove)
			self.printTheBoard()

	def printTheBoard(self):
		currentBoard = self.engine.board
		self.interface.printBoard(currentBoard)

	def finishTheGame(self):
		if self.engine.isPlayerWinner():
			self.interface.sendCongrats()
		elif self.engine.isPlayerLoser():
			self.interface.sendSorry()
		else:
			self.interface.sendDrawMessage()

		#end of program
		sys.exit()

if __name__=='__main__':
	game = Game()
	game.newGame()