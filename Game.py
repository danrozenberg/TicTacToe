#!/bin/sh
import sys
import GameEngine
import TerminalInterface
import RandomStrategy

class Game(object):

    def __init__(self):
        self.interface = TerminalInterface.TerminalInterface()
        self.engine = GameEngine.GameEngine()
        self.strategy = RandomStrategy.RandomStrategy()
        self.new_game()

    def new_game(self):
        self.interface.send_welcome_screen()
        self.engine.players_symbol = self.interface.ask_for_player_symbol()
        self.play_the_game()

    #Game's steady-state
    def play_the_game(self):
        while not self.engine.is_game_over():
            self.players_turn()
            self.computers_turn()
        self.finish_the_game()

    def players_turn(self):
        if self.engine.is_players_turn() and not self.engine.is_game_over():
            self.interface.print_message("\n=== Player's Turn ===")

        #wait for correct input before processing
        players_move = self.interface.get_players_move()
        while not self.engine.is_valid_move(players_move):
            players_move = self.interface.get_players_move()

        #now that we have a valid move, we process it.
        self.engine.process_move(players_move)
        self.print_the_board()

    def computers_turn(self):
        if not self.engine.is_players_turn() and not self.engine.is_game_over():
            self.interface.print_message("\n=== Computer's Turn ===")
            current_board = self.engine.board
            computers_move = self.strategy.get_move(current_board)
            self.engine.process_move(computers_move)
            self.print_the_board()

    def print_the_board(self):
        current_board = self.engine.board
        self.interface.print_board(current_board)

    def finish_the_game(self):
        if self.engine.is_player_winner():
            self.interface.send_congrats()
        elif self.engine.is_player_loser():
            self.interface.send_sorry()
        else:
            self.interface.send_draw_message()

        #end of program
        sys.exit()

if __name__ == '__main__':
    GAME = Game()
    GAME.new_game()
