import pygame

from block import Block
from game import TicTacToeGame
from player import Player
from game_state import CROSS_SYMBOL, NOUGHT_SYMBOL, EMPTY_SYMBOL

WHITE_SQUARE = pygame.image.load('Sprites/white_square.png')
CROSS_SQUARE = pygame.image.load('Sprites/cross_square.png')
NOUGHT_SQUARE = pygame.image.load('Sprites/nought_square.png')
TITLE = "Tic Tac Toe"


class TicTackToeUI():

	def __init__(self):
		pygame.init()
		pygame.display.set_caption(TITLE)

		self.font = pygame.font.SysFont("monospace", 25, bold = True)
		self.screen = pygame.display.set_mode((300, 300))
		self.sprite_list = pygame.sprite.Group()
		self.clock = pygame.time.Clock()

		self.render_ui = True

	def get_sprite(self, path):
		image = pygame.image.load(path)
		image = pygame.transform.scale(image, (100, 100))
		sprites.append(image)
		return image

	def load_blocks(self):
		position = 1;
		for i in range(3):
			for j in range(3):
				block = Block(WHITE_SQUARE, 100, 100, position)
				block.rect.x = j * 100
				block.rect.y = i * 100
				position += 1;

				self.sprite_list.add(block)	

	def render_visuals(self, game):
		self.sprite_list.draw(self.screen)

		pygame.draw.aaline(self.screen, (0, 0, 0), (100, 0), (100, 300))
		pygame.draw.aaline(self.screen, (0, 0, 0), (200, 0), (200, 300))
		pygame.draw.aaline(self.screen, (0, 0, 0), (300, 0), (300, 300))
		pygame.draw.aaline(self.screen, (0, 0, 0), (0, 100), (300, 100))
		pygame.draw.aaline(self.screen, (0, 0, 0), (0, 200), (300, 200))

		if game.game_state.game_over:
			label_over = self.font.render("Game over!", 1, (242, 58, 58))

			if game.game_state.winner == EMPTY_SYMBOL:
				label_winner = self.font.render("Draw.", 1, (242, 58, 58)) 
				self.screen.blit(label_winner, (120, 150)) 		
			else:
				label_winner = self.font.render("%s won." % (game.game_state.winner), 1, (242, 58, 58)) 
				self.screen.blit(label_winner, (100, 150)) 		
			
			self.screen.blit(label_over, (80, 120))

	def handle_play(self, clicked_sprites, game, played_symbol, symbol_square):
		if not game.square_occupied(clicked_sprites[0].position):
			clicked_sprites[0].image = symbol_square
			game.play_symbol(clicked_sprites[0].position, played_symbol)

			game.print_board()

			if game.game_over():
				print ("Game over")

	def play(self):
		game = TicTacToeGame()
		currentPlayer = Player.CROSS

		self.load_blocks()

		while self.render_ui:
			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					self.render_ui = False

				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						pos = pygame.mouse.get_pos()

						# Make a list of sprites that were clicked by the mouse
						clicked_sprites = [s for s in self.sprite_list if s.rect.collidepoint(pos)]

						# Debug log 
						print ("Position: ", clicked_sprites[0].position)

						if not game.game_state.game_over:
							if currentPlayer == Player.CROSS:
								self.handle_play(clicked_sprites, game, CROSS_SYMBOL, CROSS_SQUARE)
								currentPlayer = Player.NOUGHT

							elif currentPlayer == Player.NOUGHT:
								self.handle_play(clicked_sprites, game, NOUGHT_SYMBOL, NOUGHT_SQUARE)
								currentPlayer = Player.CROSS

						

			self.render_visuals(game)			
						
			pygame.display.flip()	

			self.clock.tick(60)		

