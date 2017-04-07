from __future__ import print_function
from game_state import *


class TicTacToeGame():
	def __init__(self):
		self.game_state = GameState()

	def play_symbol(self, position, symbol):
		self.game_state.board[position - 1] = symbol


	def square_occupied(self, position):
		if self.game_state.board[position - 1] == '-':
			return False
		else:
			return True

	def horizontal_win(self):
		game_board = self.game_state.board

		for i in range(0, 6, 3):
			dominating_symbol = game_board[i]
			horizontal_win = True

			for j in range(i, i + 3):
				if game_board[j] != dominating_symbol or game_board[j] == EMPTY_SYMBOL:
					horizontal_win = False

			if horizontal_win:
				self.game_state.winner = dominating_symbol
				return True									
	
		return False		

	def vertical_win(self):
		game_board = self.game_state.board

		for i in range(3):
			dominating_symbol = game_board[i]
			horizontal_win = True

			for j in range(i, i + 7, 3):
				if game_board[j] != dominating_symbol or game_board[j] == EMPTY_SYMBOL:
					horizontal_win = False

			if horizontal_win:
				self.game_state.winner = dominating_symbol
				return True									
	
		return False

	def diagonal_left_right_win(self, game_board):
		# Check diagonal from top left corner to bottom right corner
		dominating_symbol = game_board[0]
		diagonal_win = True

		for i in range(0, 9, 4):
			if game_board[i] != dominating_symbol or game_board[i] == EMPTY_SYMBOL:
				diagonal_win = False

		if diagonal_win:
			self.game_state.winner = dominating_symbol
			return True		

	def diagonal_right_left_win(self, game_board):
		# Check diagonal from top right corner to bottom left corner
		dominating_symbol = game_board[2]
		diagonal_win = True

		
		for i in range(2, 7, 2):
			if game_board[i] != dominating_symbol or game_board[i] == EMPTY_SYMBOL:
				diagonal_win = False

		if diagonal_win:
			self.game_state.winner = dominating_symbol
			return True		

		return False		

	def diagonal_win(self):
		game_board = self.game_state.board
		
		if self.diagonal_right_left_win(game_board) or self.diagonal_left_right_win(game_board):
			return True

		return False	

	def draw(self):
		game_board = self.game_state.board

		for i in range(9):
			if game_board[i] == EMPTY_SYMBOL:
				print ("Returning false")
				return False

		return True					


	def game_over(self):
		if self.horizontal_win() or self.vertical_win() or self.diagonal_win():
			self.game_state.game_over = True
			return True
		
		elif self.draw():
			self.game_state.game_over = True
			self.game_state.winner = EMPTY_SYMBOL	
			return True

		return False	

	def print_board(self):
		for i in range(9):
			print (self.game_state.board[i], end="")

			if ((i + 1) % 3 == 0):
				print ("")	 	