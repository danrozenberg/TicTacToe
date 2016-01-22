__author__ = 'dan'

class GameEngine(object):

    def __init__(self):
        self.board = [None] * 9
        self.players_symbol = ""
        self.current_turns_symbol = "X"
        self.winning_symbol = ""

    def process_move(self, move):
        if self.is_valid_move(move):
            self.board[move - 1] = self.current_turns_symbol
            self.advance_turn()

    def advance_turn(self):
        if self.current_turns_symbol == "X":
            self.current_turns_symbol = "O"
        else:
            self.current_turns_symbol = "X"

    #returns True if valid, error string otherwise
    def is_valid_move(self, move):
        if move > len(self.board) or move < 1:
            print "please select a valid square."
            return False
        elif self.board[move - 1] is not None:
            print "this square is already full, please select an empty one."
            return False
        else:
            return True

    #checks if its the player's turn. If false, its the comptuer's
    def is_players_turn(self):
        return self.players_symbol == self.current_turns_symbol

    def is_player_winner(self):
        return self.is_victory_achieved() and \
               self.winning_symbol == self.players_symbol

    def is_player_loser(self):
        return self.is_victory_achieved() and\
               self.winning_symbol != self.players_symbol

    #game is always over when we have no free spots in the board
    def is_game_over(self):
        return self.board.count(None) == 0 or self.is_victory_achieved()

    #returns winning symbol if there is a victory, False otherwise
    def is_victory_achieved(self):
        return self.is_diagonal_victory() or self.is_horizontal_victory() or\
               self.is_vertical_victory()

    def is_horizontal_victory(self):
        board = self.board
        if board[0] == board[1] == board[2] is not None:
            self.winning_symbol = board[0]
            return True
        elif board[3] == board[4] == board[5] is not None:
            self.winning_symbol = board[3]
            return True
        elif board[6] == board[7] == board[8] is not None:
            self.winning_symbol = board[6]
            return True
        else:
            return False

    def is_vertical_victory(self):
        board = self.board
        if board[0] == board[3] == board[6] is not None:
            self.winning_symbol = board[0]
            return True
        elif board[1] == board[4] == board[7] is not None:
            self.winning_symbol = board[1]
            return True
        elif board[2] == board[5] == board[8] is not None:
            self.winning_symbol = board[2]
            return True
        else:
            return False

    def is_diagonal_victory(self):
        board = self.board
        if board[0] == board[4] == board[8] is not None:
            self.winning_symbol = board[0]
            return True
        elif board[2] == board[4] == board[6] is not None:
            self.winning_symbol = board[2]
            return True
        else:
            return False
