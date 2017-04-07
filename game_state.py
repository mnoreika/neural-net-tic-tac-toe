CROSS_SYMBOL = 'X'
NOUGHT_SYMBOL = 'O'
EMPTY_SYMBOL = '-'


class GameState():

	def __init__(self):
		self.board = ['-' for x in range(9)]
		self.game_over = False
		self.winner = None