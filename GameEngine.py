__author__ = 'dan'

class GameEngine():

	def __init__(self):
		self.board = [None] * 9
		self.playerSymbol = ""
		self.currentTurnsSymbol = "X"
		self.winningSymbol = ""

	def processMove(self, move):
		if self.isValidMove(move):
			self.board[move - 1] = self.currentTurnsSymbol
			self.advanceTurn()

	def advanceTurn(self):
		if self.currentTurnsSymbol == "X":
			self.currentTurnsSymbol = "O"
		else:
			self.currentTurnsSymbol = "X"

	#returns True if valid, error string otherwise
	def isValidMove(self, move):
		if move > len(self.board) or move < 1:
			print "please select a valid square"
			return False
		elif self.board[move - 1] is not None:
			print "this square is already full, please select an empty one"
			return False
		else:
			return True

	#checks if its the player's turn. If false, its the comptuer's
	def isPlayersTurn(self):
		return self.playerSymbol == self.currentTurnsSymbol

	def isPlayerWinner(self):
		return self.isVictoryAchieved() and self.winningSymbol == self.playerSymbol

	def isPlayerLoser(self):
		return self.isVictoryAchieved() and self.winningSymbol <> self.playerSymbol

	#game is always over when we have no free spots in the board
	def isGameOver(self):
		return self.board.count(None) == 0 or self.isVictoryAchieved()

	#returns winning symbol if there is a victory, False otherwise
	def isVictoryAchieved(self):
		return self.isDiagonalVictory() or self.isHorizontalVictory() or self.isVerticalVictory()

	def isHorizontalVictory(self):
		board = self.board
		if board[0] == board[1] == board[2] is not None:
			self.winningSymbol = board[0]
			return True
		elif board[3] == board[4] == board[5] is not None:
			self.winningSymbol = board[3]
			return True
		elif board[6] == board[7] == board[8] is not None:
			self.winningSymbol = board[6]
			return True
		else:
			return False

	def isVerticalVictory(self):
		board = self.board
		if board[0] == board[3] == board[6] is not None:
			self.winningSymbol = board[0]
			return True
		elif board[1] == board[4] == board[7] is not None:
			self.winningSymbol = board[1]
			return True
		elif board[2] == board[5] == board[8] is not None:
			self.winningSymbol = board[2]
			return True
		else:
			return False

	def isDiagonalVictory(self):
		board = self.board
		if board[0] == board[4] == board[8] is not None:
			self.winningSymbol = board[0]
			return True
		elif board[2] == board[4] == board[6] is not None:
			self.winningSymbol = board[2]
			return True
		else:
			return False