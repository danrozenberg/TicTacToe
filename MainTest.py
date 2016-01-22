import unittest
import Game

class MainTest(unittest.TestCase):

    def test_game(self):
        tictactoe = Game.TicTacToe()
        tictactoe.new_game()

if __name__ == '__main__':
    unittest.main()
