import random

class RandomStrategy():

	def getMove(self, board):
		availableNumbers = []
		for i in range(len(board)):
			if board[i] is None:
				availableNumbers.append(i)

		#computer choose an index, but we have to increase 1 to transform it into a number
		return random.choice(availableNumbers) + 1