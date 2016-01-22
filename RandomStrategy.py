import random

class RandomStrategy(object):

    def get_move(self, board):
        available_numbers = []
        for i in range(len(board)):
            if board[i] is None:
                available_numbers.append(i)

        # computer choose an index, but we have to
        #  increase 1 to transform it into a number
        return random.choice(available_numbers) + 1
